---
tag: 2PMZ7GS0QY
kind: definition
name: Transfinite diameter
msc: [31A15, 30C85]
defines: VSGTSQ7RY8
uses: [0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$.
For an integer $n \ge 2$, let
$$\delta_n(K) = \max \set{ \prod_{1 \le i < j \le n} \abs{z_i - z_j}^{2/(n(n-1))} : z_1, \dots, z_n \in K }.$$
The *transfinite diameter* of $K$ is $\delta(K) = \lim_{n \to \infty} \delta_n(K)$.

## Remarks

The maximum exists because $K^n$ is compact and the product is continuous.
The sequence $(\delta_n(K))$ is nonincreasing, so the limit exists.
To see this, drop one point from an optimal $(n+1)$-tuple in each of the $n + 1$ possible ways and multiply the resulting $n + 1$ inequalities.
The number $\delta_2(K)$ is the diameter of $K$.

Example: let $K$ be the unit circle and let $\omega = e^{2 \pi i / n}$.
The square of the Vandermonde determinant of $1, \omega, \dots, \omega^{n-1}$ has absolute value $n^n$, so these points give the product $n^{n/2}$.
By Hadamard's inequality no $n$ points of the closed unit disc give more, so $\delta_n(K) = n^{1/(n-1)}$, which tends to $1$.

Non-example: the limit of $\delta_n(K)$ is not the diameter in general.
For the unit circle $\delta_2 = 2$, while $\delta(K) = 1$.

A finite set $K$ has $\delta(K) = 0$, since for $n$ larger than the number of points two of the $z_i$ coincide.
