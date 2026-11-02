---
tag: V7AAT7X2QW
kind: definition
name: Fekete points
msc: [31A15, 30C85]
defines: F0RVAF11K9
uses: [0R6EWFKRCF, VSGTSQ7RY8]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$ with at least $n \ge 2$ points.
An $n$-tuple $(z_1, \dots, z_n)$ of points of $K$ is a system of *Fekete points* of $K$ if
$$\prod_{1 \le i < j \le n} \abs{z_i - z_j} = \max \set{ \prod_{1 \le i < j \le n} \abs{w_i - w_j} : w_1, \dots, w_n \in K }.$$

## Remarks

A system of Fekete points exists for each $n$, since $K^n$ is compact and the product is continuous.
It need not be unique: a rotation of Fekete points of a circle centred at $0$ gives Fekete points again.
The points are distinct, because the maximum is positive.
The maximum equals $\delta_n(K)^{n(n-1)/2}$, where $\delta_n(K)$ is the $n$-th diameter in the definition of the [[transfinite diameter|VSGTSQ7RY8]].

Example: on the unit circle, the $n$-th roots of unity $1, \omega, \dots, \omega^{n-1}$ with $\omega = e^{2\pi i/n}$ are Fekete points.
The product of their mutual distances is the absolute value of their Vandermonde determinant, which equals $n^{n/2}$.
Hadamard's inequality bounds the Vandermonde determinant of any $n$ points of the closed unit disc by $n^{n/2}$, so the maximum is attained.

Non-example: for $n = 2$ on the unit circle, the points $1$ and $i$ are not Fekete points, since $\abs{1 - i} = \sqrt 2 < 2 = \abs{1 - (-1)}$.

Maximizing the product is the same as minimizing the discrete logarithmic energy $\sum_{i < j} \log(1/\abs{z_i - z_j})$.
