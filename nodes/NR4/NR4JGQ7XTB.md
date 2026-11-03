---
tag: NR4JGQ7XTB
kind: example
name: XXZ model
msc: [82B23, 82B20, 82B10]
instance_of: [PAEME5EQRM]
uses: [5QG15H8P5J, PAEME5EQRM, S92G5M6X41, 45HEVXM7RD]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_Heisenberg_model
    locator: XXZ model
---

## Example

Let $L \ge 2$ and let $\mathcal{H} = (\C^2)^{\otimes L}$, with spin operators $S^a_j = \tfrac12 \sigma^a_j$ for $a = x, y, z$ and periodic boundary conditions $S^a_{L+1} = S^a_1$.
For $J > 0$ and an anisotropy parameter $\Delta \in \R$, the *XXZ chain* has Hamiltonian
$$H = J \sum_{j=1}^{L} \big( S^x_j S^x_{j+1} + S^y_j S^y_{j+1} + \Delta\, S^z_j S^z_{j+1} \big).$$
It is the anisotropic [[quantum Heisenberg model|5QG15H8P5J]] with couplings $J_x = J_y = J$ and $J_z = J\Delta$, and $\Delta = 1$ gives the isotropic antiferromagnet.
Check: $H$ commutes with the total magnetization $S^z = \sum_j S^z_j$.
Indeed each term $S^x_j S^x_{j+1} + S^y_j S^y_{j+1} = \tfrac12(S^+_j S^-_{j+1} + S^-_j S^+_{j+1})$ moves one unit of $S^z$ between neighbours.
For instance the fully polarized state $\lvert\uparrow\cdots\uparrow\rangle$ is an eigenstate with energy $\tfrac14 J\Delta L$.

## Remarks

The chain is exactly solvable by the [[Bethe ansatz|S92G5M6X41]], and its transfer-matrix description is the [[six-vertex model|45HEVXM7RD]].
Its zero-temperature phases are: for $\Delta > 1$, a gapped antiferromagnet with Néel order; for $-1 < \Delta \le 1$, a gapless critical phase described by a Luttinger liquid; for $\Delta \le -1$, a ferromagnet.
The case $\Delta = 0$ is the XX chain, which the Jordan–Wigner transformation maps to free fermions.
The parametrization $\Delta = \cos\gamma$ in the critical phase and $\Delta = \cosh\eta$ in the gapped phase is standard in the Bethe ansatz literature.

## Explanations

### L1 human

The XXZ chain is a row of quantum spins in which the coupling along one axis is tuned separately from the coupling in the plane.
Turning the dial $\Delta$ moves the chain between an ordered antiferromagnet, a fluctuating critical state, and a ferromagnet.
It is one of the few interacting quantum many-body systems whose energy levels can be found exactly.
That makes it a testing ground for ideas about quantum magnetism and one-dimensional physics.
