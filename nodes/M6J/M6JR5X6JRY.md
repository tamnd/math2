---
tag: M6JR5X6JRY
kind: definition
name: Symmetry in quantum mechanics
msc: [81R05, 81Q10, "22E70"]
defines: WN6C2BJDZT
uses: [HM2HHE3J51, MM0EJ2GDE4, VXDEQB46GV, 4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetry_in_quantum_mechanics
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]], and let $P(\mathcal{H})$ be the set of rays $[\psi] = \set{c\psi : c \in \C, \ c \ne 0}$ of nonzero vectors, the pure [[quantum states|4NQN47A92F]].
For unit vectors $\psi, \phi$ the transition probability between $[\psi]$ and $[\phi]$ is $\abs{\ip{\psi}{\phi}}^2$.

1. A *symmetry transformation* is a bijection $T \colon P(\mathcal{H}) \to P(\mathcal{H})$ that preserves all transition probabilities.
2. Let $H$ be the self-adjoint [[Hamiltonian|VXDEQB46GV]] of the system. A *symmetry of the system* is a [[unitary operator|MM0EJ2GDE4]] $U$ on $\mathcal{H}$ with $U D(H) = D(H)$ and $U H U^{-1} = H$, or an antiunitary operator with the same properties.

## Remarks

By Wigner's theorem, every symmetry transformation of rays is induced by a unitary or an antiunitary operator, unique up to a phase.
A unitary $U$ commuting with $H$ commutes with the time evolution: $U e^{-iHt/\hbar} = e^{-iHt/\hbar} U$.
If $U(s) = e^{-isA}$ is a one-parameter group of such symmetries, with $A$ self-adjoint, then $A$ commutes with $H$ and its expectation value is constant in time: $A$ is a conserved quantity.

Example: on $L^2(\R^3)$ let $H = -\frac{\hbar^2}{2m}\Delta + V(\abs{x})$ with a radial potential $V$.
For a rotation $R \in SO(3)$, the operator $(U_R \psi)(x) = \psi(R^{-1}x)$ is unitary and commutes with $H$, since both $\Delta$ and $\abs{x}$ are rotation invariant.
So every rotation is a symmetry of the system, and the generators of these rotations, the components of the orbital angular momentum, are conserved.

Non-example: in the same setting take $V(x) = x_3$, a constant force along the third axis.
A rotation $R$ about the first axis changes $V$ into another linear function.
So $U_R$ does not commute with $H$, and it is not a symmetry of the system.
It is still a symmetry transformation of the rays.
