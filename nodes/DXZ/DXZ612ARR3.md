---
tag: DXZ612ARR3
kind: definition
name: Quantum error correction
msc: [81P73, 81P70]
defines: M4BSARXSCC
uses: [10VZYJ4552, V1JTB52E8C, HM2HHE3J51, TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_error_correction
---

## Definition

Let $H$ be a finite-dimensional complex [[Hilbert space|HM2HHE3J51]].
A *quantum code* in $H$ is a linear subspace $\mathcal{C} \subseteq H$; let $P$ be the orthogonal projection onto $\mathcal{C}$.
Let $\mathcal{N}$ be a [[quantum channel|10VZYJ4552]] on the operators of $H$, the noise.
The code $\mathcal{C}$ *corrects* $\mathcal{N}$ if some quantum channel $\mathcal{R}$ satisfies
$$\mathcal{R}(\mathcal{N}(\rho)) = \rho$$
for every [[density operator|V1JTB52E8C]] $\rho$ on $H$ with $P \rho P = \rho$.
Here $\mathcal{R}$ acts on the operators of $H$, and it is called a recovery.
*Quantum error correction* is the design and use of codes and recoveries that correct given kinds of noise.

## Remarks

Example: let $H = (\C^2)^{\otimes 3}$, $\mathcal{C} = \operatorname{span}\set{\lvert 000 \rangle, \lvert 111 \rangle}$, and let $\mathcal{N}(\rho) = p_0 \rho + \sum_{i=1}^{3} p_i X_i \rho X_i$ with $p_i \ge 0$ and $\sum p_i = 1$, where $X_i$ flips qubit $i$.
The four subspaces $\mathcal{C}$ and $X_i \mathcal{C}$ are orthogonal.
The recovery measures which of them contains the state, which reveals $i$ but nothing about the encoded state, and then applies $X_i$.
So $\mathcal{C}$ corrects $\mathcal{N}$.

Non-example: the same code does not correct the noise $\mathcal{N}'(\rho) = \frac12 \rho + \frac12 Z_1 \rho Z_1$, where $Z_1 = \operatorname{diag}(1, -1)$ acts on qubit $1$.
Let $\lvert \pm_L \rangle = (\lvert 000 \rangle \pm \lvert 111 \rangle)/\sqrt2$; then $Z_1$ swaps $\lvert +_L \rangle$ and $\lvert -_L \rangle$.
So $\mathcal{N}'$ sends both states to the same mixed state, and no recovery can return both.

A code that corrects $\mathcal{N}$ also corrects every channel whose Kraus operators are linear combinations of those of $\mathcal{N}$.
This is why correcting finitely many errors corrects a continuum of them.
