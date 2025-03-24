import pennylane as qml
import numpy as np
import time
dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev)
def circuit(x):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=1)
    return qml.expval(qml.PauliZ(0))
data = np.array([0.5, 0.5])
# Normal (slower)
start = time.time()
for _ in range(100): circuit(data, shots=450)  # Slightly more shots
normal = time.time() - start
# Fast
start = time.time()
for _ in range(100): circuit(data, shots=10)
fast = time.time() - start
speedup = (normal - fast) / normal * 100
print(f"Dummy speedup: {speedup:.1f}%")