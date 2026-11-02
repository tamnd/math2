---
tag: 827DJ2CVEX
kind: definition
name: Triangle center
msc: [51M04]
defines: WRKFH25NCX
uses: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_center
---

## Definition

Let $T$ be the set of triples $(a, b, c)$ of positive real numbers with $a < b + c$, $b < c + a$ and $c < a + b$.
These are the side lengths of the [[triangles|0CTNFGYMM2]] of the Euclidean plane.
A *triangle center function* is a real function $f$ on $T$, not identically zero, such that:

1. $f$ is homogeneous: there is a real $n$ with $f(ta, tb, tc) = t^n f(a, b, c)$ for all $t > 0$ and $(a, b, c) \in T$.
2. $f$ is bisymmetric: $f(a, c, b) = f(a, b, c)$ for all $(a, b, c) \in T$.

Let $ABC$ be a triangle with $a = BC$, $b = CA$ and $c = AB$.
The *triangle center* given by $f$ is the point of the plane with trilinear coordinates
$$f(a, b, c) : f(b, c, a) : f(c, a, b),$$
whenever these are not all zero.

## Remarks

Trilinear coordinates $\alpha : \beta : \gamma$ describe the point whose signed distances to the lines $BC$, $CA$, $AB$ are in the ratio $\alpha : \beta : \gamma$.
Homogeneity makes the point move with the triangle under scaling, and bisymmetry makes it independent of the labelling of the vertices.

Example: $f(a, b, c) = 1$ is homogeneous of degree $0$ and bisymmetric.
Its center $1 : 1 : 1$ is equidistant from the three sides, so it is the [[incentre|0M9MX8YW0A]].
Similarly $f(a, b, c) = 1/a$ gives the [[centroid|0X7EEWES5G]].

Non-example: $f(a, b, c) = c/b$ is homogeneous but not bisymmetric, since $f(a, c, b) = b/c$.
The point $c/b : a/c : b/a$ is the first Brocard point, which changes into the second Brocard point when two vertices are swapped, so it is not a triangle center.
