# main.py
import threading
import os
from app.gui import run_gui
from app.simulation import malware_simulation

def main():
    """
    Main entry point for the Silent Execution application.

    This function performs two primary tasks:
    1. It ensures that all necessary directories for the simulation's output
       and sandboxing are created before the application starts.
    2. It launches the malware simulation in a separate background thread,
       allowing the legitimate GUI to run concurrently and remain responsive.
    """
    # Ensure all necessary directories exist at startup to prevent runtime errors.
    os.makedirs('output', exist_ok=True)
    os.makedirs('sandbox/generated', exist_ok=True)
    os.makedirs('sandbox/text_files_to_encrypt', exist_ok=True)

    # Create and start the simulation thread.
    # Using a daemon thread (or explicitly managing it) ensures the simulation
    # doesn't block the main application from exiting.
    sim_thread = threading.Thread(target=malware_simulation)
    sim_thread.start()

    # Run the legitimate GUI application in the main thread.
    # This will block until the user closes the calculator window.
    run_gui()

if __name__ == "__main__":
    main()

    sim_thread.join()
    print("\nSimulation finished safely. Check output/ and sandbox/ folders.")