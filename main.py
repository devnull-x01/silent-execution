# main.py
import threading
import os
import logging

from app.cli import run
from app.simulation import malware_simulation

# Set up logging to output/logs.txt
os.makedirs('output', exist_ok=True)
logging.basicConfig(filename='output/logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

if __name__ == "__main__":
    # Run malware simulation in background thread
    sim_thread = threading.Thread(target=malware_simulation)
    sim_thread.start()
    
    # Run the CLI (legitimate calculator)
    run()
    
    # Wait for simulation to finish
    sim_thread.join()
    print("Simulation complete. Check output/logs.txt and sandbox/ for details.")