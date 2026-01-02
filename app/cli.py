import argparse
import json
from pathlib import Path

from app.safety import sandbox_root
from app.logger import EventLogger
from app.scanner import scan

def init_sandbox(root: Path, logger: EventLogger):
    (root / "desktop").mkdir(parents=True, exist_ok=True)
    (root / "documents").mkdir(parents=True, exist_ok=True)

    # create demo files
    (root / "desktop" / "todo.txt").write_text("buy milk\nfinish exam\n", encoding="utf-8")
    (root / "documents" / "notes.txt").write_text("security project notes\n", encoding="utf-8")
    (root / "documents" / "sample.bin").write_bytes(b"A" * 2048)

    logger.event("INIT_SANDBOX", {"root": str(root)})

def write_report(files, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({"files": files}, indent=2), encoding="utf-8")

def run():
    parser = argparse.ArgumentParser(description="Silent Execution - sandbox-only ransomware simulation")
    parser.add_argument("cmd", choices=["init", "scan"])
    args = parser.parse_args()

    root = sandbox_root()
    logger = EventLogger(Path("output/events.jsonl"))

    logger.event("APP_START", {"cmd": args.cmd, "sandbox": str(root)})

    if args.cmd == "init":
        init_sandbox(root, logger)
        print("Sandbox initialized with demo files.")
    elif args.cmd == "scan":
        files = scan(root, logger)
        write_report(files, Path("output/scan_report.json"))
        print(f"Scan complete. Found {len(files)} target files. Report saved to output/scan_report.json")

    logger.event("APP_END", {})