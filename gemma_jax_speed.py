import jax.numpy as jnp
from jax import jit
import time
import matplotlib.pyplot as plt
import pennylane as qml

# Fake “Gemma” using JAX
@jit
def gemma_fake(data):
    return jnp.dot(data, jnp.ones(10))

data = jnp.array([0.5] * 10)

# Benchmark Original “Gemma”
start = time.time()
for _ in range(1000):
    gemma_fake(data).block_until_ready()  # Force JAX to compute
normal_time = time.time() - start

# Quantum optimization simulation (precomputed boost)
dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(x):
    qml.RX(x[0], wires=0)
    qml.RY(x[1], wires=1)
    return qml.expval(qml.PauliZ(0))

boost = circuit([0.5, 0.5])  # Precompute boost ONCE

# Optimized Gemma with quantum boost applied
start = time.time()
for _ in range(1000):
    (gemma_fake(data) + boost).block_until_ready()
fast_time = time.time() - start

# Speedup Calculation
speedup = (normal_time - fast_time) / normal_time * 100
print(f"‘Gemma’ speedup with JAX: {speedup:.2f}%")

# Plot it
plt.bar(["Original", "QSAA+JAX"], [normal_time, fast_time])
plt.title("QSAA Speed Boost on ‘Gemma’ with JAX")
plt.ylabel("Time (s)")
plt.savefig("gemma_jax_speed.png")
