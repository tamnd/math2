---
tag: FDF5C62DBD
kind: definition
name: Iterated kernel
msc: [45B05, 45P05]
defines: 9QNBFERMHD
uses: [ZM5G144PZG, GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%E2%80%93Neumann_series
---

## Definition

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]].
The *iterated kernels* of $K$ are the functions $K_n \colon [a, b] \times [a, b] \to \C$, for $n \ge 1$, defined by $K_1 = K$ and
$$K_{n}(x, s) = \int_a^b K(x, t) \, K_{n-1}(t, s) \, dt \quad \text{for } n \ge 2.$$
The function $K_n$ is the $n$-th iterated kernel of $K$.

## Remarks

Example: $K(x, s) = x s$ on $[0, 1]$.
Then $K_2(x, s) = \int_0^1 x t^2 s \, dt = x s / 3$, and by induction $K_n(x, s) = x s / 3^{n-1}$.

Non-example: the pointwise power $K(x, s)^2 = x^2 s^2$ is not the second iterated kernel $x s / 3$; iteration composes the integral operators, it does not multiply kernel values.

Each $K_n$ is continuous, and $K_n$ is the kernel of the $n$-th power of the integral operator of $K$.
More generally $K_{n + m}(x, s) = \int_a^b K_n(x, t) K_m(t, s) \, dt$ for $n, m \ge 1$.
If $\abs{K} \le M$, then $\abs{K_n(x, s)} \le M^n (b - a)^{n - 1}$, by induction on $n$.
The same definition is used for square-integrable kernels, with equality almost everywhere.
For a Volterra kernel, which vanishes for $s > x$, the integral runs over $s \le t \le x$.
