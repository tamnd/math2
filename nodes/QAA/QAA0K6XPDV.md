---
tag: QAA0K6XPDV
kind: definition
name: Quantum chaos
msc: [81Q50, 58J51, 37D40]
defines: G9SVGHXR2Z
uses: [F4NWZNTRMD, VF43FTDA1H, AZRPHS478B, 7CBT4SM83Y, B8TYKV7AA1]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_chaos
---

## Definition

Let $(M, g)$ be a compact connected [[Riemannian manifold|7CBT4SM83Y]] without boundary, and let $\Delta_g$ be its [[Laplace–Beltrami operator|F4NWZNTRMD]].
The quantum system is $-\Delta_g$ on $L^2(M)$, whose classical limit is the [[geodesic flow|VF43FTDA1H]] on the unit cotangent bundle $S^*M$.
The system is called *quantum chaotic* when this geodesic flow is chaotic.
Here chaotic means [[ergodic|AZRPHS478B]] for the Liouville measure, or a stronger property such as being Anosov.
*Quantum chaos* is the study of the [[spectrum|B8TYKV7AA1]] and the eigenfunctions of such systems in the high-energy limit.
More generally it studies semiclassical operators such as $-\hbar^2 \Delta + V$ as $\hbar \to 0$ when the classical Hamiltonian flow is chaotic.

## Remarks

Example: a compact hyperbolic surface, of constant curvature $-1$, has an Anosov and ergodic geodesic flow, so the Laplacian on it is quantum chaotic.
Quantum ergodicity holds for it, and for arithmetic surfaces quantum unique ergodicity has been proved for the joint eigenfunctions of the Laplacian and the Hecke operators.

Non-example: on the flat torus $\R^2 / 2\pi\Z^2$ the geodesic flow keeps the direction of motion fixed, so it is not ergodic on $S^*M$.
Its eigenfunctions $e^{i(kx + ly)}$ are not chaotic, and its eigenvalues $k^2 + l^2$ have high multiplicities.

The Bohigas–Giannoni–Schmit conjecture predicts that the local spacings of the eigenvalues of chaotic systems follow the statistics of random matrices.
The Berry–Tabor conjecture predicts Poisson statistics for generic integrable systems.
Both are supported by extensive numerical evidence and remain open in general.
