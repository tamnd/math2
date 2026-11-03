---
tag: DAPD9A8MTD
kind: definition
name: Brillouin zone
msc: [82D25, 82D20]
defines: EKTERAYFJ2
uses: [KNAK0TTVTY, V1R1R88GV6]
sources:
  - url: https://en.wikipedia.org/wiki/Brillouin_zone
---

## Definition

Let $\Lambda \subset \R^n$ be a Bravais lattice and let $\Lambda^*$ be its [[reciprocal lattice|KNAK0TTVTY]].
The *first Brillouin zone* of $\Lambda$ is the set
$$B = \set{k \in \R^n : \abs{k} \le \abs{k - G} \text{ for all } G \in \Lambda^*}.$$
That is, $B$ is the [[Voronoi cell|V1R1R88GV6]] of the point $0$ in $\Lambda^*$.

## Remarks

The translates $B + G$, $G \in \Lambda^*$, cover $\R^n$ and overlap only on their boundaries.
So $B$ is a fundamental domain for $\Lambda^*$, and its volume is $(2\pi)^n / V$, where $V$ is the volume of a primitive cell of $\Lambda$.
Identifying opposite faces, $B$ becomes the torus $\R^n / \Lambda^*$.

Example: for $\Lambda = a\Z$ with $a > 0$, $\Lambda^* = (2\pi/a)\Z$ and $B = [-\pi/a, \pi/a]$.
Check: $\abs{k} \le \abs{k - 2\pi m/a}$ for all integers $m$ holds exactly when $\abs{k} \le \pi/a$.

Non-example: for $\Lambda = a\Z^2$ the square $[0, 2\pi/a]^2$ is a fundamental domain of $\Lambda^*$, but it is not the Brillouin zone.
The point $k = (1.9\pi/a, 0)$ lies in it, yet it is closer to $G = (2\pi/a, 0)$ than to $0$.
The Brillouin zone of $a\Z^2$ is $[-\pi/a, \pi/a]^2$.
