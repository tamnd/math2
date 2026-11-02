---
tag: 6P1E2FJPSD
kind: statement
role: theorem
name: Whitehead theorem
msc: [55P10, 55Q05]
uses: [5W95QFHXPR, P976WYEFMB, XZG6MTSWCN, 4Q3WY1RX91]
about: [XZG6MTSWCN, 4Q3WY1RX91]
sources:
  - url: https://en.wikipedia.org/wiki/Whitehead_theorem
same_as:
  wikidata: Q3527185
  wikipedia: Whitehead theorem
---

## Statement

Let $X$ and $Y$ be connected [[CW complexes|5W95QFHXPR]], let $x_0 \in X$, and let $f \colon X \to Y$ be a continuous map.
Assume that $f_* \colon \pi_n(X, x_0) \to \pi_n(Y, f(x_0))$ is an isomorphism of [[homotopy groups|P976WYEFMB]] for every $n \ge 1$.
Then $f$ is a [[homotopy equivalence|XZG6MTSWCN]].

## Remarks

Replace $Y$ by the mapping cylinder of $f$, so that $f$ becomes the inclusion of a subcomplex.
The relative homotopy groups of the pair then vanish, and one deforms $Y$ onto $X$ cell by cell, using compression of maps of disks.
In other words, a [[weak homotopy equivalence|4Q3WY1RX91]] between CW complexes is a homotopy equivalence.
The CW hypothesis is needed: the map from the [[Warsaw circle|17VG475BRV]] to a point induces isomorphisms on all homotopy groups, but it is not a homotopy equivalence.
The isomorphisms must be induced by one map: $\R P^2 \times S^3$ and $S^2 \times \R P^3$ have isomorphic homotopy groups, but they are not homotopy equivalent, as their homology differs.

## Explanations

### L1 human

Homotopy groups record how spheres of each dimension sit in a space.
For spaces built from cells, a map that matches all these records perfectly is as good as an equivalence: it can be inverted up to deformation.
So for such spaces, homotopy groups detect sameness of shape, provided a map realises the match.

### L2 human

The theorem justifies working with CW complexes in homotopy theory, where weak and genuine homotopy equivalences coincide.
Combined with the [[Hurewicz theorem|ZA11N5XPZM]], it gives a homology version.
A map between simply connected CW complexes that induces isomorphisms on all integral homology groups is a homotopy equivalence.
For example, a simply connected CW complex with the integral homology of a point is contractible.
