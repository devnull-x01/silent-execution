import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict


class EventLogger:
    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def event(self, action: str, details: Dict[str, Any]):
        rec = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "details": details,
        }
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")