from flask import Flask, jsonify
from flask_cors import CORS
import os

from memory_manager import allocate_memory, get_memory
from process_manager import create_process, get_processes
from access_control import check_access
from attack_detector import detect_attack
from logger import log_attack

app = Flask(__name__)
CORS(app)

# 🏠 Home Route
@app.route('/')
def home():
    return "🔥 Secure Memory Isolation System is Running"


# ⚙️ Create Process
@app.route('/create/<pid>')
def create(pid):
    return create_process(pid)


# 🧠 Allocate Memory
@app.route('/allocate/<pid>/<int:size>')
def allocate(pid, size):
    return allocate_memory(pid, size)


# 📊 View Memory
@app.route('/memory')
def memory():
    return jsonify(get_memory())


# ⚙️ View Processes
@app.route('/processes')
def processes():
    return jsonify(get_processes())


# 🔐 Access Control + Attack Detection
@app.route('/access/<req>/<target>')
def access(req, target):
    if detect_attack(req, target):
        log_attack(f"Unauthorized access from {req} to {target}")
        return f"🚨 ALERT: {req} tried to access {target}'s memory!"
    
    return "✅ Access Granted"


# 📄 Logs Route (FIXED)
@app.route('/logs')
def logs():
    try:
        log_path = os.path.join(os.path.dirname(__file__), "logs", "security_log.txt")

        if not os.path.exists(log_path):
            return "No logs found yet"

        with open(log_path, "r") as f:
            content = f.readlines()

        if not content:
            return "No logs recorded yet"

        return "<br>".join(content)

    except Exception as e:
        return f"Error reading logs: {str(e)}"


# 🚀 Run Server (ALWAYS LAST)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)