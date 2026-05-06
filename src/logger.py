import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = "logs/keystrokes.log"


def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)


def write_log(entry: str):
    ensure_log_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {entry}\n")
