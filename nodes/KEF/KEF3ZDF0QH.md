---
tag: KEF3ZDF0QH
kind: conjecture
name: Novikov conjecture
msc: [57R67, 19J25, 20F65]
uses: [WA796ZCNRX, XZG6MTSWCN, WDVVEYD6AT, DN11FKWN63, TEG1ZX1AGJ, 6N7BC70CX0, ZEA0PEM3B2, JWJ8YPR7EB]
about: [WA796ZCNRX]
sources:
  - url: https://en.wikipedia.org/wiki/Novikov_conjecture
same_as:
  wikidata: Q7064908
  wikipedia: Novikov conjecture
history:
  posed_by: "Sergei Novikov"
---

## Statement

Let $G$ be a discrete group and let $BG$ be its [[classifying space|WA796ZCNRX]].
Let $M$ be a closed oriented smooth manifold with [[fundamental class|ZEA0PEM3B2]] $[M]$, and let $f \colon M \to BG$ be a continuous map.
Let $L(M) \in H^*(M; \Q)$ be its Hirzebruch $L$-class, a polynomial in the rational [[Pontryagin classes|DN11FKWN63]].
For $x \in H^*(BG; \Q)$, the higher signature is
$$\operatorname{sign}_x(M, f) = \ip{L(M) \smile f^*(x)}{[M]} \in \Q,$$
computed in rational [[singular cohomology|6N7BC70CX0]].
The conjecture states that higher signatures are oriented homotopy invariants.
That is, for every orientation-preserving [[homotopy equivalence|XZG6MTSWCN]] $h \colon N \to M$ of closed oriented smooth manifolds and every $x \in H^*(BG; \Q)$,
$$\operatorname{sign}_x(N, f \circ h) = \operatorname{sign}_x(M, f).$$

## Remarks

For $x = 1$, the higher signature is the ordinary [[signature|WDVVEYD6AT]] of $M$ by the [[Hirzebruch signature theorem|TEG1ZX1AGJ]].
It is a homotopy invariant because it is defined from the cup product pairing on $H^*(M; \Q)$.
The individual Pontryagin classes are not homotopy invariants, so the conjecture singles out special combinations of them.

The conjecture is open in general.
It is known for many classes of groups.
Among them are free abelian groups, discrete subgroups of connected Lie groups (Kasparov), and [[hyperbolic groups|JWJ8YPR7EB]] (Connes and Moscovici).
Yu proved it for groups that coarsely embed into a Hilbert space and have a classifying space with a finite model; the finiteness hypothesis was later removed.
The main methods go through operator K-theory: injectivity of the rational assembly map in the Baum–Connes conjecture, or of the coarse assembly map, implies the conjecture.

## Explanations

### L1 human

The signature is a number attached to a manifold that does not change when the manifold is deformed by a homotopy equivalence.
For manifolds with a complicated fundamental group, there are further "higher" signatures, obtained by combining the Pontryagin classes with cohomology classes coming from the group.
Novikov conjectured that these higher signatures are also unchanged by homotopy equivalences.
This would mean that part of the smooth structure of a manifold is already determined by its homotopy type.
