---
tag: P32FQE1H0D
kind: definition
name: Pseudo algebraically closed field
msc: ["12E30", 12L12, 14G05]
defines: 92SQ10PN6J
uses: [04C5ZBG1WT, 0X6AB5P3G1, 0PF6TM8TWT, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo_algebraically_closed_field
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] with [[algebraic closure|0X6AB5P3G1]] $\bar K$.
An affine variety $V \subseteq \bar K^n$ defined over $K$ is the set of common zeros in $\bar K^n$ of a set of polynomials in $K[X_1, \dots, X_n]$.
It is *absolutely irreducible* if it is irreducible as a variety over $\bar K$.
This means that it is not the union of two proper closed subsets defined over $\bar K$.
A point of $V$ is $K$-rational if all its coordinates lie in $K$.
The field $K$ is *pseudo algebraically closed* (PAC) if every nonempty absolutely irreducible affine variety defined over $K$ has a $K$-rational point.

## Remarks

It is equivalent to ask the condition only for curves, that is, for varieties of dimension $1$.

Example: every [[algebraically closed field|0PF6TM8TWT]] $K$ is PAC, since then $\bar K = K$ and every point of a nonempty variety is $K$-rational.
Every infinite algebraic extension of a [[finite field|0ZXZ82FTX2]] is PAC.

Non-example: $\Q$ and $\R$ are not PAC.
The curve $V$ defined by $x^2 + y^2 + 1 = 0$ is absolutely irreducible, since $x^2 + y^2 + 1$ is irreducible over $\C$, and $V$ is nonempty, since it contains $(i, 0)$.
But it has no point with real coordinates, because $x^2 + y^2 + 1 > 0$ for real $x, y$.

Non-example: a finite field $\F_q$ is not PAC.
For instance, the curve $y^q - y = x^{q+1} - x^2 + 1$ is absolutely irreducible, because the degree $q + 1$ of the right side is prime to the characteristic of $\F_q$.
It has no $\F_q$-rational point, because $y^q - y = 0$ for $y \in \F_q$, while $x^{q+1} - x^2 + 1 = 1$ for $x \in \F_q$.
