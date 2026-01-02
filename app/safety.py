# app/safety.py
from pathlib import Path

def sandbox_root() -> Path:
    """
    Returns the absolute path to the simulation's 'generated' directory.
    
    This function centralizes the definition of the sandbox's root, ensuring
    that all simulated malware activities are strictly confined to a known,
    safe location.
    
    Returns:
        Path: The absolute path to the 'sandbox/generated' directory.
    """
    return (Path.cwd() / "sandbox" / "generated").resolve()

def ensure_in_sandbox(path: Path, root: Path = None) -> Path:
    """
    Verifies that a given file path is safely within the sandbox directory.

    This is a critical security function that prevents the simulation from
    accidentally affecting files outside of its designated sandbox. It raises
    a ValueError if the path attempts to "escape" the sandbox.

    Args:
        path (Path): The file path to validate.
        root (Path, optional): The root of the sandbox. Defaults to sandbox_root().

    Returns:
        Path: The validated, absolute path if it is safe.

    Raises:
        ValueError: If the path is outside the sandbox.
    """
    if root is None:
        root = sandbox_root()
    
    # Resolve the path to get its absolute, canonical form
    abs_path = path.resolve()
    
    # Check if the resolved path is within the root directory
    if root not in abs_path.parents and abs_path != root:
        raise ValueError(f"Security risk: Path '{abs_path}' is outside the sandbox '{root}'.")
        
    return abs_path