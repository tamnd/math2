---
tag: VAP45DFXW3
kind: statement
role: theorem
name: Yau's conjecture on infinitely many minimal surfaces
msc: ["58E12", 53A10, 49Q05]
uses: [7CBT4SM83Y, 41X0YW2R9N, 6KVJHG1KRZ]
about: [41X0YW2R9N]
sources:
  - url: https://en.wikipedia.org/wiki/Almgren–Pitts_min-max_theory
---

## Statement

Let $(M, g)$ be a closed [[Riemannian manifold|7CBT4SM83Y]] of dimension $n + 1$ with $3 \le n + 1 \le 7$.
Then $M$ contains infinitely many distinct smooth, closed, embedded [[minimal hypersurfaces|41X0YW2R9N]].

## Remarks

Shing-Tung Yau asked in his 1982 list of problems in differential geometry whether every closed $3$-manifold contains infinitely many immersed minimal surfaces.
The statement above, which gives embedded minimal hypersurfaces in all dimensions from $3$ to $7$, was proved by Antoine Song, building on work of Marques and Neves.

The proofs use [[Almgren–Pitts min-max theory|6KVJHG1KRZ]] for $k$-parameter sweepouts.
Marques and Neves showed that the min-max values $\omega_k(M)$ for $k = 1, 2, \dots$ are areas of minimal hypersurfaces with multiplicities; by results of Gromov and Guth they grow like $k^{1/(n+1)}$.
Under positive Ricci curvature this growth forces infinitely many distinct hypersurfaces, which gave the first cases of the conjecture.
Liokumovich, Marques and Neves proved a Weyl law for the $\omega_k$.
With it, Irie, Marques and Neves showed that for generic metrics the union of the closed embedded minimal hypersurfaces is dense in $M$.
Song treated arbitrary metrics with a min-max theory on non-compact manifolds obtained from pieces of $M$ bounded by stable minimal hypersurfaces.

Example: in the round sphere $S^3$ the great $2$-spheres are infinitely many embedded minimal surfaces; the theorem asserts the same for every metric on every closed $3$-manifold.

## Explanations

### L1 human

A minimal surface is a soap-film-like surface that is in balance: it cannot lower its area by small changes.
The theorem says that any closed curved space of dimension three to seven contains infinitely many different such closed surfaces, however irregular the shape of the space is.
In a round sphere one sees infinitely many of them at once, the great spheres; in a bumpy space they are hidden, and min-max methods find them.

### L2 human

The theorem is the analogue for minimal hypersurfaces of the existence of infinitely many closed geodesics on surfaces.
Its proof is a showcase of Almgren–Pitts theory: the sequence of min-max widths behaves like the spectrum of the Laplacian, with a Weyl-type growth law.
The dimension restriction comes from regularity: in dimension $8$ and higher, min-max hypersurfaces may have singular points.
