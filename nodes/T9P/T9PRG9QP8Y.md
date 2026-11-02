---
tag: T9PRG9QP8Y
kind: definition
name: Bilateral Z-transform
msc: [44A55, 94A12]
defines: 3DBAMXA80B
uses: [5FY0JQGHYZ, 0G9EKM0E15, 0GXMPDNYX3, 1P8WX3EGHF]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Bilateral Z-transform
---

## Definition

Let $x = (x_n)_{n \in \Z}$ be a two-sided [[sequence|0G9EKM0E15]] of complex numbers.
The *bilateral Z-transform* of $x$ is the [[Laurent series|0GXMPDNYX3]]
$$X(z) = \sum_{n = -\infty}^{\infty} x_n z^{-n}.$$
It is a function on its [[region of convergence|1P8WX3EGHF]], the set of nonzero complex $z$ where the series converges absolutely.

## Remarks

Example: let $x_n = 2^{-\abs{n}}$.
The part $\sum_{n \ge 0} (2z)^{-n}$ converges for $\abs{z} > 1/2$ and the part $\sum_{n \ge 1} (z/2)^n$ converges for $\abs{z} < 2$.
So $X(z) = \dfrac{2z}{2z - 1} + \dfrac{z}{2 - z}$ on the annulus $1/2 < \abs{z} < 2$.
Example with the same formula: for $a \ne 0$, $x_n = a^n$ for $n \ge 0$ (and $0$ otherwise) gives $z/(z - a)$ on $\abs{z} > \abs{a}$, while $x_n = -a^n$ for $n \le -1$ (and $0$ otherwise) gives $z/(z - a)$ on $\abs{z} < \abs{a}$.
Non-example: $x_n = 1$ for all $n$ has an empty region of convergence, so the transform is not a function.
The notation $X(z) = \mathcal{Z}\{x\}(z)$ is standard; signal processing texts write $x[n]$ for $x_n$.
