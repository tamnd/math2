---
tag: 2FE4P23NVC
kind: statement
role: theorem
name: Von Neumann's theorem on self-adjoint extensions
msc: [47B25, 47A20]
uses: [HM2HHE3J51, H971WGMV6C, VM7B38PA87, 86B7HF79PQ, G4GMSNAX8X, 0ZXSF2YQV2, DT49GKR9AS]
about: [G4GMSNAX8X, H971WGMV6C]
sources:
  - url: https://en.wikipedia.org/wiki/Extensions_of_symmetric_operators
---

## Statement

Let $H$ be a complex [[Hilbert space|HM2HHE3J51]], and let $A$ be a [[closed|VM7B38PA87]] [[symmetric operator|H971WGMV6C]] on $H$ with dense domain $D(A)$ and [[adjoint|86B7HF79PQ]] $A^*$.
Let $K_+ = \ker(A^* - iI)$ and $K_- = \ker(A^* + iI)$ be its [[deficiency subspaces|G4GMSNAX8X]], with deficiency indices $n_\pm = \dim K_\pm$.
Then:

1. $D(A^*) = D(A) \dotplus K_+ \dotplus K_-$, a direct sum of subspaces.
2. $A$ has a self-adjoint extension if and only if $n_+ = n_-$.
3. If $n_+ = n_-$, the self-adjoint extensions of $A$ are in bijection with the [[isometric isomorphisms|0ZXSF2YQV2]] $U \colon K_+ \to K_-$. The extension $A_U$ attached to $U$ has domain $D(A_U) = \set{f + k + U k : f \in D(A), \ k \in K_+}$, and $A_U(f + k + U k) = A f + i k - i U k$.

## Remarks

Every self-adjoint extension $B$ of $A$ satisfies $A \subseteq B = B^* \subseteq A^*$, so it is a restriction of $A^*$ to a subspace between $D(A)$ and $D(A^*)$.
On $D(A^*)$, the form $\ip{A^* x}{y} - \ip{x}{A^* y}$ measures the failure of symmetry, and it vanishes on $D(A)$.
Part 1 and a computation of this form on $K_+ \dotplus K_-$ show that the maximal subspaces on which it vanishes are exactly the graphs of the isometric isomorphisms $U \colon K_+ \to K_-$.
In particular, $A$ is self-adjoint if and only if $n_+ = n_- = 0$, and a symmetric operator is [[essentially self-adjoint|DT49GKR9AS]] if and only if its closure has $n_+ = n_- = 0$.
Example: for $A = -i \, d/dx$, closed from the smooth functions with compact support in $(0,1)$ in $L^2([0,1])$, the indices are $(1,1)$.
The isometric isomorphisms from $K_+$ to $K_-$ form a circle, and the self-adjoint extensions are the operators $-i \, d/dx$ with boundary conditions $u(1) = e^{i \theta} u(0)$, $\theta \in [0, 2\pi)$.
On $L^2([0, \infty))$, the same operator has indices $(1, 0)$, so it has no self-adjoint extension.
A symmetric operator that commutes with a conjugation, such as a real differential operator, has $n_+ = n_-$ and so always has self-adjoint extensions.

## Explanations

### L1 human

A symmetric operator can fail to be self-adjoint because its domain is too small.
Von Neumann's theorem says exactly when the domain can be enlarged to give a self-adjoint operator, and lists all the ways to do it.
The answer depends on two numbers, the deficiency indices.
An extension exists when they are equal, and the extensions are then labeled by unitary maps between two spaces.

### L2 human

In quantum mechanics, an observable must be self-adjoint, while a formula such as $-d^2/dx^2$ only gives a symmetric operator on nice functions.
The theorem turns the choice of a self-adjoint realization into linear algebra on the deficiency subspaces, and the choices correspond to boundary conditions.
For Sturm–Liouville operators, the Weyl limit point and limit circle alternative computes the deficiency indices from the behaviour of solutions at the endpoints.
Other constructions, such as the Friedrichs extension, pick out a distinguished self-adjoint extension of a semibounded symmetric operator.
