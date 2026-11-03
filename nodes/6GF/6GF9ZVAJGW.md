---
tag: 6GF9ZVAJGW
kind: statement
role: theorem
name: Haag's theorem
msc: [81T05]
uses: [5QTZQV6TNG, 1TJ8TNH331, 74BPYJNZTM, HM2HHE3J51]
about: [W031YNVRE3]
sources:
  - url: https://en.wikipedia.org/wiki/Haag%27s_theorem
same_as:
  wikidata: Q1566372
  wikipedia: Haag's theorem
---

## Statement

Let $\phi_0$ be the free Hermitian scalar field of mass $m > 0$ on [[Fock space|1TJ8TNH331]] $H_0$, with vacuum $\Omega_0$ and conjugate momentum $\pi_0 = \partial_t \phi_0$.
Let $\phi$ be a Hermitian scalar field satisfying the [[Wightman axioms|5QTZQV6TNG]] on a [[Hilbert space|HM2HHE3J51]] $H$, with vacuum $\Omega$ and $\pi = \partial_t \phi$.
Assume the following.

1. At some time $t$, the fields $\phi(t, \cdot)$ and $\pi(t, \cdot)$ exist as operator-valued distributions on $\R^3$, and so do $\phi_0(t, \cdot)$ and $\pi_0(t, \cdot)$.
2. There is a unitary operator $V \colon H_0 \to H$ with $V \phi_0(t, \mathbf{x}) V^{-1} = \phi(t, \mathbf{x})$ and $V \pi_0(t, \mathbf{x}) V^{-1} = \pi(t, \mathbf{x})$.
3. The [[unitary representations|74BPYJNZTM]] $U_0$ and $U$ of the Euclidean group of $\R^3$ in the two theories satisfy $V U_0(g) V^{-1} = U(g)$.
   The vectors $\Omega_0$ and $\Omega$ are, up to a scalar factor, the only vectors invariant under these representations.

Then $V \Omega_0 = c\, \Omega$ for some $c \in \C$ with $\abs{c} = 1$, the two-point functions of $\phi$ and $\phi_0$ coincide, and $\phi$ is a free field of mass $m$.

## Remarks

The vacuum relation follows from the uniqueness of the invariant vectors.
Then the Wightman functions of $\phi$ and $\phi_0$ agree at equal times.
Lorentz covariance with analyticity in the forward tube extends the equality of the two-point functions to all points.
A Wightman field whose two-point function is that of the free field of mass $m$ is itself free; this is the Jost–Schroer theorem.

The theorem says that the interaction picture of perturbation theory cannot exist in the way it is usually written.
An interacting theory cannot live on the Fock space of the free theory with a unitary map that intertwines the fields at a fixed time.
Practical calculations escape the theorem by using cutoffs in space or momentum, which break the Euclidean invariance of hypothesis 3, and by removing them only at the end.

## Explanations

### L1 human

Textbook perturbation theory starts from free particles and turns on the interaction slowly.
Haag's theorem shows that this picture is inconsistent if taken literally.
A theory that looks like the free theory at one instant, with the same vacuum symmetry, must be the free theory.
So an interacting field lives in a different, inequivalent representation of the field operators.

### L2 human

The theorem is a consequence of the infinite number of degrees of freedom of a field.
For finitely many degrees of freedom, the Stone–von Neumann theorem says that all regular irreducible representations of the canonical commutation relations are equivalent, but this fails in infinite dimension.
Haag's theorem is one reason why rigorous constructions in [[constructive quantum field theory|FG51Y62J8Y]] first introduce a finite volume and an ultraviolet cutoff.
Its conclusion does not contradict the success of perturbation theory with renormalization, whose final formulas do not depend on the interaction picture.
