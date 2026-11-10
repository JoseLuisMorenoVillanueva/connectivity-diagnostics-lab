"""Print a fictional connectivity event. No real network check is performed."""
import json
from datetime import datetime, timezone


def main():
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "device_id": "device-001",
        "operation_id": "op-001",
        "event_type": "connectivity_check",
        "result": "success",
        "duration_ms": 125,
    }
    print(json.dumps(event, indent=2))


if __name__ == "__main__":
    main()
