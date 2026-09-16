def detect_attack(request_pid, target_pid):
    if request_pid != target_pid:
        return True
    return False