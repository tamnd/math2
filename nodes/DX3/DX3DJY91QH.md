---
tag: DX3DJY91QH
kind: definition
name: Degree of a continuous map
msc: [55M25]
defines: TMFG2P912R
uses: [0VGFHTM75Y, T62369RFH6, M0Q5CFJ7ZH, QQQ9B1DK4P, 913WEQERBE, ZEA0PEM3B2]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_a_continuous_mapping
---

## Definition

Let $n \ge 1$ and let $f \colon S^n \to S^n$ be a [[continuous map|0VGFHTM75Y]] of the [[$n$-sphere|T62369RFH6]].
The induced homomorphism $f_\ast \colon H_n(S^n; \Z) \to H_n(S^n; \Z)$ on [[singular homology|M0Q5CFJ7ZH]] is an endomorphism of a group isomorphic to $\Z$.
So $f_\ast(a) = d \, a$ for a unique integer $d$ and all $a$.
This integer is the *degree* of $f$, written $\deg f$.

More generally, let $M$ and $N$ be closed connected [[oriented|913WEQERBE]] [[topological $n$-manifolds|QQQ9B1DK4P]] with [[fundamental classes|ZEA0PEM3B2]] $[M]$ and $[N]$, and let $f \colon M \to N$ be continuous.
The degree of $f$ is the integer $\deg f$ with $f_\ast [M] = (\deg f) [N]$ in $H_n(N; \Z)$.

## Remarks

Homotopic maps have the same degree, and $\deg (g \circ f) = \deg g \cdot \deg f$.

Example: on $S^1 \subset \C$, the map $f(z) = z^k$ has degree $k$.
For a reflection $r$ of $S^n$ in a hyperplane, $\deg r = -1$; the antipodal map $x \mapsto -x$ is a composite of $n + 1$ reflections, so its degree is $(-1)^{n+1}$.

Non-example: a map $S^m \to S^n$ with $m \neq n$ has no degree in this sense, since the source and target manifolds must have the same dimension.

If $f$ is smooth and $y$ is a regular value, then $\deg f = \sum_{x \in f^{-1}(y)} \sgn \det Df(x)$, where the sign is computed in oriented charts.
For $n = 1$, the degree of a map $S^1 \to S^1$ equals its [[winding number|0NQSV2EWDR]] about $0$.
