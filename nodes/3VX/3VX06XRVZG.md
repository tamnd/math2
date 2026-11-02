---
tag: 3VX06XRVZG
kind: statement
role: theorem
name: Schoenflies theorem
msc: [57N50, 57N45]
uses: [687RGCHBTP, 00ZG9Y9TR4, 0QT00PB5G2, 0Q0H13G8ZB, T62369RFH6]
about: [687RGCHBTP]
sources:
  - url: https://en.wikipedia.org/wiki/Schoenflies_problem
same_as:
  wikidata: Q495412
  wikipedia: Schoenflies problem
---

## Statement

1. Let $C \subset \R^2$ be a [[Jordan curve|687RGCHBTP]]. Then there is a [[homeomorphism|0QT00PB5G2]] $h \colon \R^2 \to \R^2$ with $h(C) = S^1$, the unit circle. In particular, the closure of the bounded component of $\R^2 \setminus C$ is homeomorphic to the [[closed disk|0Q0H13G8ZB]] $D^2$.
2. (Generalized Schoenflies theorem.) Let $n \ge 2$ and let $e \colon S^{n-1} \times [-1, 1] \to S^n$ be a [[topological embedding|00ZG9Y9TR4]], where $S^n$ is the [[$n$-sphere|T62369RFH6]]. Let $\Sigma = e(S^{n-1} \times \set{0})$. Then $S^n \setminus \Sigma$ has two components, and the closure of each is homeomorphic to the closed ball $D^n$.

## Remarks

The hypothesis in part 2 says that the sphere $\Sigma$ is bicollared.
For a codimension-one sphere this is equivalent to being locally flat.
It cannot be dropped for $n = 3$: the Alexander horned sphere is an embedded $2$-sphere one of whose complementary regions is not simply connected, so its closure is not a ball.
In the plane no such hypothesis is needed, because every Jordan curve is tame.
One proof of part 1 uses the Riemann mapping theorem and Carathéodory's extension theorem for the interior; part 2 was proved by Morton Brown in 1960.
For smooth embedded spheres in $\R^4$, whether the closed inside is always a smooth ball is open.

## Explanations

### L1 human

The Jordan curve theorem says a loop in the plane has an inside and an outside.
The Schoenflies theorem says more: the inside, with the loop added, is just a deformed disk.
One can straighten the whole plane so that the loop becomes a round circle.

### L2 human

In higher dimensions, the naive analogue fails: there are wild embeddings of $S^2$ in $\R^3$ whose outside is not the outside of a ball.
The generalized theorem shows that all such wildness lives at points where the sphere is not locally flat.
It is a basic tool in topological manifold theory, for example for the annulus theorem and for showing that the connected sum is well defined.
