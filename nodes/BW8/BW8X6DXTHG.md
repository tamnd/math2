---
tag: BW8X6DXTHG
kind: definition
name: Connected sum
msc: [57N99, 57R65]
defines: Y0K0K5NGWW
uses: [QQQ9B1DK4P, 0V032VWTHD, 00ZG9Y9TR4, 0Q0H13G8ZB, 0NQ1H2X495, 702SNFQG0W]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_sum
---

## Definition

Let $n \ge 1$ and let $M$ and $N$ be [[connected|0V032VWTHD]] [[topological manifolds|QQQ9B1DK4P]] of dimension $n$.
Let $D^n$ be the [[closed unit ball|0Q0H13G8ZB]] of $\R^n$, with interior $B^n$ and boundary sphere $S^{n-1}$.
Let $2D^n$ be the closed ball of radius $2$.
Let $f \colon 2D^n \to M$ and $g \colon 2D^n \to N$ be [[topological embeddings|00ZG9Y9TR4]] onto subsets of the interiors.
The *connected sum* $M \# N$ is the [[quotient space|0NQ1H2X495]] of the disjoint union
$$\bigl(M \setminus f(B^n)\bigr) \sqcup \bigl(N \setminus g(B^n)\bigr)$$
by the relation that identifies $f(x)$ with $g(x)$ for every $x \in S^{n-1}$.
If $M$ and $N$ are [[oriented|702SNFQG0W]], one takes $f$ preserving and $g$ reversing orientation.
Then $M \# N$ gets an orientation that extends those of both pieces.

## Remarks

For two tori $T^2 \# T^2$ is the closed orientable surface of genus $2$.
Each torus minus an open disk is a torus with one boundary circle, and gluing the two circles gives a connected surface with two handles.

The disjoint union $M \sqcup N$ is not a connected sum: no balls are removed and no spheres are glued, and the result is not connected.

The result is a connected topological $n$-manifold.
Up to homeomorphism, it does not depend on the choice of the embeddings when $M$ and $N$ are oriented and the orientation rule above is followed.
Without orientations the choice can matter: $\mathbb{CP}^2 \# \mathbb{CP}^2$ and $\mathbb{CP}^2 \# \overline{\mathbb{CP}^2}$ are not homotopy equivalent, since their intersection forms differ.
The sphere is a unit: $M \# S^n$ is homeomorphic to $M$.
The real projective plane gives $\mathbb{RP}^2 \# \mathbb{RP}^2$ homeomorphic to the [[Klein bottle|6J4C2P3ZHC]].
