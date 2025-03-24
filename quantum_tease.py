import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=5)

@qml.qnode(dev)
def circuit(x):
    for i in range(5):
        qml.RX(x[i], wires=i)
    return qml.expval(qml.PauliZ(0))

data = np.random.random(5)
result = circuit(data)

print("5-qubit test — 3% performance teaser!")
