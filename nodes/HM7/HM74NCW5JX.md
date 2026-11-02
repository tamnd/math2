---
tag: HM74NCW5JX
kind: definition
name: Prony's method
msc: [65D10, 41A30, 65F20]
defines: 2WSV04QETW
uses: [0NDVHBVBXB, PQ1D8FQB3E, 0JTRMBQ1SA, 019MA1VTR2]
sources:
  - url: https://en.wikipedia.org/wiki/Prony%27s_method
---

## Definition

Let $n \ge 1$, and suppose the numbers $f(0), f(1), \dots, f(2n - 1)$ are samples of $f(k) = \sum_{j=1}^{n} c_j z_j^k$, where $z_1, \dots, z_n$ are distinct nonzero complex numbers and $c_1, \dots, c_n$ are nonzero complex numbers.
*Prony's method* recovers the $z_j$ and $c_j$ in three steps.

1. Solve the [[linear system|0JTRMBQ1SA]] $\sum_{m=0}^{n-1} a_m f(k + m) = -f(k + n)$ for $k = 0, \dots, n - 1$ for $a_0, \dots, a_{n-1}$.
2. Compute the [[roots|019MA1VTR2]] $z_1, \dots, z_n$ of the polynomial $P(z) = z^n + a_{n-1} z^{n-1} + \cdots + a_0$.
3. Solve the Vandermonde system $\sum_{j=1}^{n} c_j z_j^k = f(k)$ for $k = 0, \dots, n - 1$ for $c_1, \dots, c_n$.

## Remarks

The coefficients of $P(z) = \prod_j (z - z_j)$ satisfy step 1, since $f$ obeys the [[linear recurrence|0NDVHBVBXB]] with characteristic polynomial $P$.
The matrix $H = (f(k + m))_{k, m = 0}^{n-1}$ of step 1 is a [[Hankel matrix|PQ1D8FQB3E]].
It factors as $H = V^T C V$ with the Vandermonde matrix $V = (z_j^m)$ and $C = \operatorname{diag}(c_j)$.
So $H$ is invertible under the hypotheses, and step 1 has a unique solution.
Example: samples $2, 3, 5, 9$ with $n = 2$ give $2 a_0 + 3 a_1 = -5$ and $3 a_0 + 5 a_1 = -9$, so $a_0 = 2$, $a_1 = -3$, $P(z) = (z - 1)(z - 2)$, and then $c_1 = c_2 = 1$: $f(k) = 1 + 2^k$.
Non-example: $f(k) = k$ is not such a sum with $n = 1$; the step 1 equation $a_0 f(0) = -f(1)$ reads $0 = -1$ and has no solution.
With noisy data or more samples, one solves steps 1 and 3 in the least squares sense.
The method is then sensitive to noise, and variants such as the matrix pencil method improve it.
