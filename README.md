# silent-execution
Malware simulation in a safe contained environment for the security P3-C1
# Setup
Ativate venv : 'source .venv/bin/activate'
run 'python3 main.py'

# features
legitimate app ; simple cli calculator 
simulated malware : persistence, duplication, file analysis , ransomware-like actions , propagation.
All actions logged to 'output/log.txt' and confined to 'sandbox/'

# Testing
Run 'python3 main.py' and interact with calculator 
check output/log.txt and 'sandbox/' for simulations.