from pathlib import Path
from typing import Dict, List
import hashlib

from app.safety import ensure_in_sandbox
from app.logger import EventLogger

TARGET_EXTS = {".txt", ".pdf", ".docx", ".jpg", ".png", ".bin"}

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def scan(root: Path, logger: EventLogger) -> List[Dict]:
    ensure_in_sandbox(root, root)
    logger.event("SCAN_START", {"root": str(root)})

    out: List[Dict] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        ensure_in_sandbox(p, root)
        if p.suffix.lower() in TARGET_EXTS and not p.name.endswith(".locked"):
            info = {
                "path": str(p),
                "name": p.name,
                "ext": p.suffix.lower(),
                "size": p.stat().st_size,
                "sha256": sha256_file(p),
            }
            out.append(info)
            logger.event("FILE_FOUND", {"path": str(p), "ext": info["ext"], "size": info["size"]})

    logger.event("SCAN_END", {"count": len(out)})
    return out