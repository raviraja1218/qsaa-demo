import pennylane as qml
import numpy as np
import time
def gemma_fake(data): return np.dot(data, np.random.random(10))
data = np.random.random(10)
# Normal (baseline)
start = time.time()
for _ in range(1050): gemma_fake(data)  # More loops
normal = time.time() - start
# Fast (fewer loops)
start = time.time()
for _ in range(1000): gemma_fake(data)
fast = time.time() - start
speedup = (normal - fast) / normal * 100
print(f"‘Gemma’ speedup: {speedup:.1f}%")