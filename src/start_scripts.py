import random
import subprocess
import sys


MUST_HAVE_SCRIPTS = [
    "scheduler.py",
    "cold_database.py",
]

OPTIONAL_SCRIPTS = [
    "journal.py",
    "data_methods_repo.py",
]

optionals = OPTIONAL_SCRIPTS
if len(sys.argv) > 1 and sys.argv[1].startswith("chaos="):
    optionals = random.choices(OPTIONAL_SCRIPTS, k=sys.argv[0].split("=")[1])

to_run = MUST_HAVE_SCRIPTS + optionals
for script in to_run:
    print(script)
    subprocess.Popen(["python3", script])
