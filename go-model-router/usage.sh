#!/usr/bin/env bash
set -euo pipefail

KEY="${OPENCODE_GO_API_KEY:-$(opencode auth export 2>/dev/null | jq -r '.[] | select(.integrationID=="opencode-go" and .active==true) | .value.key' 2>/dev/null || true)}"
if [ -z "$KEY" ] || [ "$KEY" = "null" ]; then
  echo '{"error":"no_api_key"}'
  exit 1
fi

RESP=$(printf 'header = "Authorization: Bearer %s"\n' "$KEY" | curl -sS -m 15 -w '\n%{http_code}' -K - https://opencode.ai/zen/go/v1/usage 2>/dev/null) || {
  unset KEY
  echo '{"error":"request_failed"}'
  exit 1
}
unset KEY

CODE=$(tail -n1 <<<"$RESP")
BODY=$(sed '$d' <<<"$RESP")

case "$CODE" in
  200)
    printf '%s' "$BODY" | python3 -c '
import json, sys, datetime, math

try:
    raw = json.load(sys.stdin)
except Exception:
    print(json.dumps({"error": "request_failed"}))
    sys.exit(1)

u = raw.get("usage") if isinstance(raw.get("usage"), dict) else raw
now = datetime.datetime.now(datetime.timezone.utc)

def parse_win(name):
    w = u.get(name)
    if not isinstance(w, dict) or not isinstance(w.get("percent"), (int, float)):
        return None
    pct = float(w["percent"])
    sec = w.get("reset_in_sec")
    resets_at = w.get("resetsAt")
    if sec is None and isinstance(resets_at, str):
        try:
            dt = datetime.datetime.fromisoformat(resets_at.replace("Z", "+00:00"))
            sec = max(0, int((dt - now).total_seconds()))
        except Exception:
            sec = None
    return {
        "percent": pct,
        "reset_in_sec": None if pct == 0 else sec,
        "resets_at": None if pct == 0 else resets_at,
        "reset_approx": (pct == 0),
    }

r = parse_win("rolling")
wk = parse_win("weekly")
mo = parse_win("monthly")
if not (r and wk and mo):
    print(json.dumps({"error": "request_failed"}))
    sys.exit(1)

fresh_cycle = (mo["percent"] == 0)
days_left = None if (fresh_cycle or mo["reset_in_sec"] is None) else round(mo["reset_in_sec"] / 86400.0, 1)
days_elapsed = None if days_left is None else round(max(0.1, 30.0 - days_left), 1)

# Burn-rate check (monthly % vs linear pace * 1.25)
running_hot = False
if days_elapsed is not None and mo["percent"] > (days_elapsed / 30.0) * 100.0 * 1.25:
    running_hot = True

# End-of-cycle check (fresh-cycle safe)
eoc = (not fresh_cycle) and (days_left is not None and days_left <= 5.0) and (mo["percent"] < 70.0) and (r["percent"] < 70.0) and (wk["percent"] < 80.0)

# Tightest window
windows = [("5-hour", r["percent"]), ("weekly", wk["percent"]), ("monthly", mo["percent"])]
tightest_name, tightest_pct = max(windows, key=lambda x: x[1])

# Determine routing mode
if max(r["percent"], wk["percent"], mo["percent"]) >= 95.0:
    mode = "exhausted_free_only"
elif r["percent"] >= 80.0 or wk["percent"] >= 80.0 or (not eoc and mo["percent"] >= 85.0):
    mode = "downgrade_t1_only"
elif eoc:
    mode = "end_of_cycle_upgrade"
elif r["percent"] >= 60.0 or wk["percent"] >= 60.0 or mo["percent"] >= 70.0 or running_hot:
    mode = "downgrade_1_tier"
elif r["percent"] <= 20.0 and wk["percent"] <= 25.0 and mo["percent"] <= 35.0 and not running_hot:
    mode = "surplus_upgrade"
else:
    mode = "normal"

rp = r["percent"]
wp = wk["percent"]
mp = mo["percent"]
is_surplus = (mode == "surplus_upgrade")
dl_str = "unknown (fresh cycle 0%)" if days_left is None else str(days_left) + "d"
print("Usage snapshot: 5-hour {:.1f}%, weekly {:.1f}%, monthly {:.1f}%, days left {}".format(rp, wp, mp, dl_str))
print("Tightest window: {} ({:.1f}%); routing_mode={} (surplus_upgrade={}, end_of_cycle_upgrade={}, running_hot={})".format(tightest_name, tightest_pct, mode, is_surplus, eoc, running_hot))
print(json.dumps({
    "rolling": r,
    "weekly": wk,
    "monthly": mo,
    "days_left": days_left,
    "days_elapsed": days_elapsed,
    "fresh_cycle": fresh_cycle,
    "running_hot": running_hot,
    "tightest_window": tightest_name,
    "routing_mode": mode
}))
'
    ;;
  404) echo '{"error":"http_404"}'; exit 1 ;;
  *)   echo '{"error":"request_failed"}'; exit 1 ;;
esac
