memory = {}

def allocate_memory(pid, size):
    if pid in memory:
        return f"[!] Memory already allocated for {pid}"
    
    memory[pid] = {
        "size": size,
        "data": [0] * size
    }
    
    return f"[+] {size} units allocated to {pid}"

def get_memory():
    return memory
if __name__ == "__main__":
    print(allocate_memory("P1", 5))
    print(get_memory())