---
tag: VY2TTB854G
kind: definition
name: Spherical code
msc: [52C17, 94B65, 05B40]
defines: SDCX4WDP4F
uses: [0S52TNNTH9, 0ZEHZY85E6]
sources:
  - url: https://en.wikipedia.org/wiki/Spherical_code
---

## Definition

Let $n \ge 1$ and let $S^{n-1} = \set{x \in \R^n : x \cdot x = 1}$ be the unit sphere, where $x \cdot y$ is the [[dot product|0S52TNNTH9]].
A *spherical code* in $\R^n$ is a finite nonempty subset $C \subset S^{n-1}$.
Let $0 < \theta \le \pi$.
The code $C$ has *minimal angle* at least $\theta$ if $x \cdot y \le \cos \theta$ for all distinct $x, y \in C$.
Equivalently, every two distinct points of $C$ make an [[angle|0ZEHZY85E6]] at least $\theta$ at the origin.
The largest size of a spherical code in $\R^n$ with minimal angle at least $\theta$ is denoted $A(n, \theta)$.

## Remarks

Example: the $2n$ points $\pm e_1, \dots, \pm e_n$, where $e_i$ are the standard basis vectors, form a spherical code with minimal angle $\pi/2$.
Two distinct points among them have dot product $0$ or $-1$, both at most $\cos(\pi/2) = 0$.
Non-example: in $\R^2$, the points $(1, 0)$, $(0, 1)$ and $(1/\sqrt 2, 1/\sqrt 2)$ do not have minimal angle at least $\pi/2$, since the dot product of the first and the third is $1/\sqrt 2 > 0$.
The [[kissing number|B408FZYXF9]] is $\tau(n) = A(n, \pi/3)$.
