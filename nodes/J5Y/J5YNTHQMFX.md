---
tag: J5YNTHQMFX
kind: statement
role: theorem
name: Hilbert projection theorem
msc: [46C05]
uses: [HM2HHE3J51, 02AS45T3H9, 0ZCK8DQYN1, 026HPGYGS4, 0XJXTBCB2T, 0MCDDSCB9Z]
about: [HM2HHE3J51, 0B8KZRT28M]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_projection_theorem
same_as:
  wikidata: Q3527215
  wikipedia: Hilbert projection theorem
---

## Statement

Let $H$ be a real or complex [[Hilbert space|HM2HHE3J51]].
Let $C$ be a nonempty [[closed|0ZCK8DQYN1]] [[convex|02AS45T3H9]] subset of $H$, and let $x \in H$.
Then there is exactly one $y \in C$ such that
$$\norm{x - y} = \inf_{z \in C} \norm{x - z}.$$
This point $y$ is the only point of $C$ with $\operatorname{Re} \ip{x - y}{z - y} \le 0$ for all $z \in C$.

## Remarks

The idea of the proof: let $d$ be the infimum and take $z_n \in C$ with $\norm{x - z_n} \to d$.
The [[parallelogram law|026HPGYGS4]] gives $\norm{z_n - z_m}^2 = 2 \norm{x - z_n}^2 + 2 \norm{x - z_m}^2 - 4 \norm{x - (z_n + z_m)/2}^2$.
By convexity the midpoint lies in $C$, so the last norm is at least $d$, and $(z_n)$ is a Cauchy sequence.
Completeness and closedness give a limit $y \in C$, and the same identity gives uniqueness.

When $C$ is a closed linear subspace $M$, the condition becomes $x - y \perp M$.
Then $y$ is the [[orthogonal projection|0B8KZRT28M]] of $x$ on $M$, and $H = M \oplus M^\perp$ with the [[orthogonal complement|0XJXTBCB2T]] $M^\perp$.
For finite-dimensional $M$ this is the [[closest point property|0MCDDSCB9Z]].

The hypotheses matter.
If $C$ is not closed, such as an open ball not containing $x$, there may be no nearest point.
If $C$ is not convex, such as a circle in $\R^2$ and $x$ its center, the nearest point need not be unique.
In the Banach space $\R^2$ with the max norm, the nearest point of the line $\set{(t, 1)}$ to $0$ is not unique.

## Explanations

### L1 human

From any point there is exactly one nearest point in a closed convex set.
The segment from the point to its nearest point meets the set at a right angle or wider.
This is what makes orthogonal projection work in infinite dimensions.

### L2 human

The theorem is the base of Hilbert space geometry.
It gives the orthogonal decomposition $H = M \oplus M^\perp$, the existence of orthogonal projections and the Riesz representation theorem.
In optimisation and approximation it shows that least squares problems over closed convex sets have unique solutions.
