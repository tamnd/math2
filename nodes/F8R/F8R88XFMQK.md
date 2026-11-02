---
tag: F8R88XFMQK
kind: definition
name: Mathematical formulation of quantum mechanics
msc: [81P05, 46N50, 81Q10]
defines: J1YDW3BE56
uses: [HM2HHE3J51, 0NEGN5CRSC, KRJX5RA0PW, ATGT25E5FF, MM0EJ2GDE4, Z2CP530WDE, EY0X2NKA3S]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_formulation_of_quantum_mechanics
    locator: Postulates of quantum mechanics
---

## Definition

In the mathematical formulation of quantum mechanics, a physical system is described by the following data and rules.

1. States: the system has a complex separable [[Hilbert space|HM2HHE3J51]] $H$. A pure state is a unit vector $\psi \in H$. The vectors $\psi$ and $e^{i\alpha}\psi$ with $\alpha \in \R$ give the same state.
2. Observables: each measurable quantity is a [[self-adjoint operator|0NEGN5CRSC]] $A$ on $H$, possibly [[unbounded|KRJX5RA0PW]], with [[projection-valued measure|ATGT25E5FF]] $P^A$ from the spectral theorem, so that $A = \int_\R \lambda \, dP^A(\lambda)$.
3. Measurement (Born rule): measuring $A$ in the state $\psi$ gives a result in a Borel set $E \subseteq \R$ with probability $\langle P^A(E)\psi, \psi \rangle$. So the possible results lie in the spectrum of $A$. For $\psi$ in the domain of $A$, the expected value is $\langle A\psi, \psi \rangle$.
4. Dynamics: there is a self-adjoint operator $\hat H$, the Hamiltonian. A state evolves by $\psi(t) = e^{-it\hat H/\hbar}\psi(0)$, where $\hbar$ is the reduced Planck constant. The operators $e^{-it\hat H/\hbar}$ form a strongly continuous one-parameter group of [[unitary operators|MM0EJ2GDE4]].
5. Composite systems: the Hilbert space of a system made of two parts with spaces $H_1$ and $H_2$ is the [[tensor product|EY0X2NKA3S]] $H_1 \otimes H_2$.

Mixed states are density operators: positive [[trace class operators|Z2CP530WDE]] $\rho$ with $\operatorname{tr}\rho = 1$; the probability in clause 3 is then $\operatorname{tr}(\rho P^A(E))$.

## Remarks

Example: a spin-$\tfrac12$ system has $H = \C^2$ and spin observable $\sigma_z = \operatorname{diag}(1, -1)$, whose spectral projections are $P(\set{1}) = \operatorname{diag}(1, 0)$ and $P(\set{-1}) = \operatorname{diag}(0, 1)$.
For $\psi = (1, 1)/\sqrt 2$, the two results each have probability $\tfrac12$, and the expected value is $\langle \sigma_z \psi, \psi \rangle = 0$.

Non-example: the matrix $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is not self-adjoint, so clause 2 does not make it an observable.
It has no spectral decomposition into orthogonal projections: its only eigenvalue is $0$, but $N \ne 0$.

When $\psi$ is a unit vector, the pure state $\psi$ corresponds to the density operator $\rho = \langle \cdot, \psi \rangle \psi$, the projection onto $\C\psi$.
By Stone's theorem, every strongly continuous one-parameter unitary group has the form of clause 4 for a unique self-adjoint generator.
