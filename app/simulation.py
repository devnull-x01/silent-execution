# app/simulation.py
import os
import time
import logging

def malware_simulation():
    """Simulates malware behaviors in a safe sandbox."""
    logging.info("Malware simulation started.")
    
    # Simulate persistence: Log attempt to add to startup
    startup_path = os.path.join('sandbox', 'startup_simulation')
    os.makedirs(startup_path, exist_ok=True)
    sim_copy_path = os.path.join(startup_path, 'malware_copy.py')
    with open(sim_copy_path, 'w') as f:
        f.write("# Simulated malware copy for persistence\nprint('Persistent execution simulated!')")
    logging.info(f"Simulated persistence: Copied to startup path {sim_copy_path}")
    time.sleep(0.5)  # Short delay for realism
    
    # Simulate duplication to strategic locations
    strategic_locations = [
        os.path.join('sandbox', 'desktop_sim'),
        os.path.join('sandbox', 'documents_sim')
    ]
    for loc in strategic_locations:
        os.makedirs(loc, exist_ok=True)
        dup_path = os.path.join(loc, 'duplicated_malware.py')
        with open(dup_path, 'w') as f:
            f.write("# Simulated duplicated malware\nprint('Duplication simulated!')")
        logging.info(f"Simulated duplication: Copied to {dup_path}")
    time.sleep(0.5)
    
    # Simulate analysis of user files
    user_files_dir = os.path.join('sandbox', 'user_files_sim')
    os.makedirs(user_files_dir, exist_ok=True)
    # Create dummy files to "scan" (if not exist)
    for i in range(3):
        dummy_path = os.path.join(user_files_dir, f'file_{i}.txt')
        if not os.path.exists(dummy_path):
            with open(dummy_path, 'w') as f:
                f.write(f"Dummy content {i}")
    
    scanned_files = os.listdir(user_files_dir)
    for file in scanned_files:
        logging.info(f"Simulated file analysis: Scanned {os.path.join(user_files_dir, file)}")
    time.sleep(0.5)
    
    # Simulate ransomware behavior
    for file in scanned_files:
        sim_encrypted = file + '.encrypted_sim'
        logging.info(f"Simulated ransomware: Would encrypt/rename {file} to {sim_encrypted} (logical lock applied)")
        # Create a dummy "encrypted" file (no real change to original)
        with open(os.path.join(user_files_dir, sim_encrypted), 'w') as f:
            f.write("Simulated encrypted content")
    time.sleep(0.5)
    
    # Simulate propagation
    propagation_dir = os.path.join('sandbox', 'propagation_sim')
    os.makedirs(propagation_dir, exist_ok=True)
    for i in range(2):
        prop_path = os.path.join(propagation_dir, f'propagated_copy_{i}.py')
        with open(prop_path, 'w') as f:
            f.write(f"# Simulated propagated copy\nprint('Propagation to node {i} simulated!')")
        logging.info(f"Simulated propagation: Copied to {prop_path}")
    
    # Simple state graph in logs
    logging.info("Propagation graph simulation: Start -> Duplicate -> Infect Node1 -> Infect Node2 -> End")
    
    logging.info("Malware simulation ended.")