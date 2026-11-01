---
tag: N8ZY3A50HK
kind: definition
name: Sober space
msc: [54D10, 06D22]
defines: 4N4DNDR22Z
uses: [0CQHFPGJ45, 0ZCK8DQYN1, 0QEAJB91GZ, 07SG12TQH3, 0S1FJ8VEX9, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Sober_space
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A subset $C \subseteq X$ is irreducible when $C \ne \varnothing$ and the following holds.
If $C = A \cup B$ with $A$ and $B$ [[closed|0ZCK8DQYN1]] in the subspace $C$, then $A = C$ or $B = C$.
A point $x$ is a generic point of a closed set $C$ when the [[closure|0QEAJB91GZ]] $\overline{\set{x}}$ equals $C$.
$X$ is *sober* when every irreducible closed subset of $X$ has exactly one generic point.

## Remarks

For each point $x$, the closure $\overline{\set{x}}$ is irreducible and closed, with generic point $x$.
So the uniqueness part says that $\overline{\set{x}} = \overline{\set{y}}$ implies $x = y$, and a sober space is [[T0|07SG12TQH3]].
Every [[Hausdorff space|0S1FJ8VEX9]] is sober, because its irreducible subsets are single points.

Example: for a commutative ring $R$, the spectrum $\operatorname{Spec} R$ with the Zariski topology is sober.
An irreducible closed set has the form $V(\mathfrak p) = \set{\mathfrak q : \mathfrak q \supseteq \mathfrak p}$ for a unique [[prime ideal|00MHHZ9SNE]] $\mathfrak p$, and $\mathfrak p$ is its generic point.

Non-example: an infinite set $X$ with the [[cofinite topology|0B906ZBTMZ]] is not sober.
$X$ is irreducible, since two proper closed sets are finite and their union is not $X$.
But each point is closed, so $\overline{\set{x}} = \set{x} \ne X$, and $X$ has no generic point.
