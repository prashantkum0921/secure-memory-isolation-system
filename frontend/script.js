import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

// 🌌 Particles
tsParticles.load("particles-js", {
    particles: {
        number: { value: 60 },
        color: { value: "#38bdf8" },
        size: { value: 2 },
        move: { enable: true, speed: 1 }
    }
});

// Get PID
function getPID() {
    let pid = document.getElementById("pid").value.trim();
    if (!pid) {
        show("⚠ Please enter a Process ID");
        return null;
    }
    return pid;
}

// Create
function createProcess() {
    let pid = getPID();
    if (!pid) return;

    fetch(`${API}/create/${pid}`)
    .then(res => res.text())
    .then(data => show(data));
}

// Allocate
function allocateMemory() {
    let pid = getPID();
    if (!pid) return;

    fetch(`${API}/allocate/${pid}/10`)
    .then(res => res.text())
    .then(data => show(data));
}

// View Memory
function viewMemory() {
    fetch(`${API}/memory`)
    .then(res => res.json())
    .then(data => {
        document.getElementById("memory-visual").innerHTML = "";
        show(JSON.stringify(data, null, 2));
        drawMemory(data);
    });
}

// Attack
function simulateAttack() {
    let attacker = getPID();
    if (!attacker) return;

    let target = prompt("Enter target process (e.g. P1):");

    if (!target) {
        show("⚠ No target entered");
        return;
    }

    fetch(`${API}/access/${attacker}/${target}`)
    .then(res => res.text())
    .then(data => show(data));
}

// Logs
function viewLogs() {
    fetch(`${API}/logs`)
    .then(res => res.text())
    .then(data => show(data));
}

// Output + Alert
function show(msg) {
    document.getElementById("output").innerHTML = msg;

    if (msg.toLowerCase().includes("alert") || msg.toLowerCase().includes("unauthorized")) {
        let alertBox = document.getElementById("alertBox");
        alertBox.innerText = msg;
        alertBox.classList.remove("hidden");

        setTimeout(() => {
            alertBox.classList.add("hidden");
        }, 3000);
    }
}

// Draw Memory
function drawMemory(memory) {
    const container = document.getElementById("memory-visual");

    for (let pid in memory) {
        let processDiv = document.createElement("div");
        processDiv.style.margin = "10px";

        let title = document.createElement("h3");
        title.innerText = pid;

        let blocks = document.createElement("div");
        blocks.style.display = "flex";
        blocks.style.flexWrap = "wrap";
        blocks.style.justifyContent = "center";

        memory[pid].data.forEach(() => {
            let block = document.createElement("div");
            block.className = "block";
            blocks.appendChild(block);
        });

        processDiv.appendChild(title);
        processDiv.appendChild(blocks);
        container.appendChild(processDiv);
    }
}