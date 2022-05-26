import subprocess
from time import sleep

while True:
    a = subprocess.run(['python', 'rae.py', 'find'])
    if a.returncode != 0:
        break
