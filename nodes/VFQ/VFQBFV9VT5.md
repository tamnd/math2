---
tag: VFQBFV9VT5
kind: definition
name: Loop quantum gravity
msc: [83C45, 81S08]
defines: 9C3ECSDRTP
uses: [SH0DEE8P6K, B173ESJ4YX, WHDZ3MK56B, HM2HHE3J51, 7NW2C10YSR, 6XDPXBJGJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Loop_quantum_gravity
---

## Definition

Let $\Sigma$ be a three-manifold.
Describe general relativity on $\R \times \Sigma$ by the [[Ashtekar–Barbero variables|SH0DEE8P6K]]: an $SU(2)$ connection $A$ and a densitized triad $E$ on $\Sigma$.
These are subject to the Gauss, diffeomorphism and Hamiltonian constraints.
*Loop quantum gravity* is the [[canonical quantization|7NW2C10YSR]] of this system in which:

1. the elementary variables are the [[holonomies|WHDZ3MK56B]] $h_e(A) \in SU(2)$ of $A$ along finite curves $e$ in $\Sigma$, and the fluxes of $E$ through surfaces;
2. the kinematical [[Hilbert space|HM2HHE3J51]] is the completion of the functions of finitely many holonomies in the Ashtekar–Lewandowski inner product, built from Haar measure;
3. the Gauss constraint is solved by passing to $SU(2)$-gauge-invariant states, which are spanned by [[spin network|B173ESJ4YX]] states;
4. the diffeomorphism constraint is solved by passing to diffeomorphism classes of spin networks (s-knots), and the Hamiltonian constraint acts as an operator.

## Remarks

Let $S$ be a surface, and let a spin network meet $S$ transversally at points of edges with spins $j_1, \dots, j_n$.
Then its state is an eigenvector of the area operator of $S$, with eigenvalue
$$A = 8 \pi \gamma \, \ell_P^2 \sum_{k=1}^{n} \sqrt{j_k (j_k + 1)},$$
where $\gamma > 0$ is the Barbero–Immirzi parameter and $\ell_P$ is the Planck length.
Example: a single edge of spin $\frac12$ crossing $S$ gives the smallest nonzero area $4 \sqrt{3} \pi \gamma \ell_P^2$.
Non-example: a Fock space of gravitons on flat space is not a representation of this kind, because it uses a background metric.
In loop quantum gravity no background metric is chosen.
The construction of the Hamiltonian constraint operator, due to Thiemann, has ambiguities, and the covariant dynamics is studied through [[spin foams|6XDPXBJGJ7]].
