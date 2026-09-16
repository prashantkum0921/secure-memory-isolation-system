processes = []

def create_process(pid):
    if pid in processes:
        return f"[!] Process {pid} already exists"
    
    processes.append(pid)
    return f"[+] Process {pid} created"

def get_processes():
    return processes
if __name__ == "__main__":
    print(create_process("P1"))
    print(create_process("P2"))
    print(get_processes())