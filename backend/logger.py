import os

# Get current file directory (backend/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create logs folder inside backend
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# Create log file path
LOG_FILE = os.path.join(LOG_DIR, "security_log.txt")


def log_attack(message):
    with open(LOG_FILE, "a") as file:
        file.write(message + "\n")