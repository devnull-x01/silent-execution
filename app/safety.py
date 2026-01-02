from pathlib import Path

def sandbox_root() -> Path:
    # sandbox is always: <project>/sandbox
    return (Path.cwd() / "sandbox").resolve()

def ensure_in_sandbox(path: Path, root: Path) -> Path:
    rp = path.resolve()
    rr = root.resolve()
    if rp != rr and rr not in rp.parents:
        raise PermissionError(f"BLOCKED: outside sandbox -> {rp}")
    return rp