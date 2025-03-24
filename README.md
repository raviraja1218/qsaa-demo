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




 Why It Matters

- Quantum-Safe Now        : QSAA secures “Gemma” with Kyber—protects against 2030 quantum threats (per Google’s quantum team).  
- Massive Efficiency      : 80.25% speedup with JAX—cuts compute costs, scales for AGI.  
- Quantum Edge            : 5-qubit VQC tease—future-proofs DeepMind’s AI with quantum tech.  
- Built Solo in <12 Hours : Proves I can deliver fast—ready to scale with DeepMind mentors.  
- GSoC Ready              : Linked in my GSoC proposal and shared with DeepMind SQ mentors.

Future Work

 Scale to 10-15% speedup on real “Gemma” in 12 weeks—optimize VQC with DeepMind TPUs.  
 Integrate Kyber into “Gemma”’s full pipeline—end-to-end quantum-safe AI.  
 Publish as an open-source tool and research paper with DeepMind—boost their community impact.


Let’s Collaborate!

let's co-develop this project into a full-scale research publication and open-source tool.


Author

 [Raviraja](https://github.com/raviraja1218)
 [GSoC Profile](https://summerofcode.withgoogle.com/programs/2025/organizations/google-deepmind-sq)
 Email: rhraviraja1812@gmail.com


How to Run
 Clone: `git clone https://github.com/raviraja1218/qsaa-demo.git`  
 Install: `pip install oqs pennylane jax jaxlib matplotlib numpy`  

