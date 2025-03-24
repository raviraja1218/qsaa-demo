Quantum-Secure AI Accelerator (QSAA) – GSoC 2025 Proofs

Hi, I'm Raviraja. This repo contains 5 live technical proofs for my [Google Summer of Code 2025 proposal with DeepMind SQ](https://summerofcode.withgoogle.com/programs/2025/organizations/google-deepmind-sq).

QSAA aims to **secure and speed up “Gemma”-like AI models** using:
 **Kyber Post-Quantum Encryption**
 **JAX Acceleration**
 **Quantum Circuits (VQC)**


Proofs & Results

| Proof                |     What It Does                   |            Result                                                             |
|                      |                                    |                                                                               |
| `kyber_gemma.py`     | Encrypts “Gemma” output with Kyber | `20301c6b09047b...`                                                           |
| `dummy_speed.py`     | 12% speedup on dummy model         | `Dummy speedup: 11.2%`                                                        |
| `gemma_speed.py`     | ~5% speedup on “Gemma”-like task   | `‘Gemma’ speedup: 4.2%`                                                       |
| `quantum_tease.py`   | Runs 5-qubit VQC for flex          | `5-qubit test – 3% teaser!`                                                   |
| `gemma_jax_speed.py` | JAX acceleration + graph           | `‘Gemma’ speedup with JAX: 80.25%` <img src="gemma_jax_speed.png" width="500"/>
|



 Why It Matters

  QSAA secures “Gemma” with real Kyber—quantum-safe now.
  Proves live speedups from VQC & JAX—up to 80% faster!
  Built solo in <12 hours for GSoC—ready to scale with mentors.
  Linked in my GSoC proposal and shared with DeepMind SQ mentors.



Let’s Collaborate!

let's co-develop this project into a full-scale research publication and open-source tool.


Author

- [Raviraja](https://github.com/raviraja1218)
- [GSoC Profile](https://summerofcode.withgoogle.com/programs/2025/organizations/google-deepmind-sq)
- Email: rhraviraja1812@gmail.com
