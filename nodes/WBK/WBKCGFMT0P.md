---
tag: WBKCGFMT0P
kind: statement
role: theorem
name: Delzant's theorem on toric manifolds
msc: [53D20, 14M25, 52B20]
uses: [ZARM34FZ6Z, CAN490EPRT, 5CTHC6612N, SBJVATVH44]
about: [ZARM34FZ6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Toric_manifold
---

## Statement

A *symplectic toric manifold* is a compact connected [[symplectic manifold|CAN490EPRT]] $(M, \omega)$ of dimension $2n$ with two data.
These are an effective action of the torus $T^n = (S^1)^n$ and a [[moment map|ZARM34FZ6Z]] $\mu \colon M \to \R^n$ for it.
A *Delzant polytope* in $\R^n$ is a [[convex polytope|300K6CB1KH]] $\Delta$ such that at each vertex $v$:

1. exactly $n$ edges meet at $v$;
2. the edges at $v$ have the form $v + t u_i$, $t \ge 0$, with $u_1, \ldots, u_n \in \Z^n$;
3. these vectors $u_1, \ldots, u_n$ can be chosen to form a basis of the lattice $\Z^n$.

Then the image $\mu(M)$ of a symplectic toric manifold is a Delzant polytope.
The map $(M, \omega, \mu) \mapsto \mu(M)$ is a bijection from symplectic toric manifolds onto Delzant polytopes in $\R^n$.
Here toric manifolds are taken up to $T^n$-equivariant symplectomorphisms that intertwine the moment maps.

## Remarks

That $\mu(M)$ is a convex polytope is the [[Atiyah–Guillemin–Sternberg convexity theorem|5CTHC6612N]]; the local normal form at fixed points gives the three conditions.
For surjectivity, Delzant builds $M$ from $\Delta$ as a [[symplectic reduction|SBJVATVH44]] of $\C^d$ by a subtorus of $T^d$, where $d$ is the number of facets of $\Delta$.
Injectivity uses the local structure near each orbit and a gluing argument.

Example: the simplex with vertices $0, e_1, \ldots, e_n$ is a Delzant polytope, and it corresponds to $\mathbb{CP}^n$; the square $[0,1]^2$ corresponds to $S^2 \times S^2$.
The triangle with vertices $(0,0)$, $(1,0)$, $(0,2)$ is not Delzant.
At $(1,0)$ the primitive edge vectors are $(-1,0)$ and $(-1,2)$, with determinant $-2$, so they do not form a basis of $\Z^2$.

## Explanations

### L1 human

A toric manifold is a symplectic manifold with as much torus symmetry as its dimension allows.
Delzant's theorem says that such a manifold is completely described by a polytope with integer edge directions, its moment polytope.
So questions about these manifolds can be turned into questions about polytopes.

### L2 human

The theorem gives a dictionary: faces of the polytope correspond to orbit closures, and vertices to fixed points of the torus.
Every symplectic toric manifold has a compatible complex structure that makes it a smooth [[toric variety|YWB981MEF2]].
Rational simple polytopes with a positive integer label on each facet correspond in the same way to toric orbifolds, by work of Lerman and Tolman.
