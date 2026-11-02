---
tag: 7D47PADY9N
kind: definition
name: Frobenius method
msc: [34M03, 34A25]
defines: W8ZWXC2HQS
uses: [H96HXG6CA0, 0MZB06ST2B, 08RT9GDDPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_method
---

## Definition

Let $z_0$ be a [[regular singular point|H96HXG6CA0]] of $y'' + p(z) y' + q(z) y = 0$.
Write $(z - z_0)\, p(z) = \sum_{k \ge 0} p_k (z - z_0)^k$ and $(z - z_0)^2 q(z) = \sum_{k \ge 0} q_k (z - z_0)^k$ as convergent [[power series|0MZB06ST2B]].
The *Frobenius method* seeks solutions of the form
$$y = (z - z_0)^r \sum_{k \ge 0} a_k (z - z_0)^k, \qquad a_0 \ne 0,$$
with an exponent $r \in \C$ and coefficients $a_k \in \C$, as follows.

1. Put $F(s) = s (s - 1) + p_0 s + q_0$. The exponent $r$ must be a root of the *indicial equation* $F(r) = 0$.
2. The coefficients satisfy, for $k \ge 1$, the recurrence
$$F(r + k)\, a_k = - \sum_{j=0}^{k-1} \left( (r + j)\, p_{k-j} + q_{k-j} \right) a_j.$$
3. When $F(r + k) \ne 0$ for all $k \ge 1$, the recurrence determines all $a_k$ from $a_0$.

## Remarks

The rules come from inserting the series into $(z - z_0)^2 y'' + (z - z_0) \cdot (z - z_0) p\, y' + (z - z_0)^2 q\, y = 0$ and comparing the coefficients of $(z - z_0)^{r + k}$.
The roots of the indicial equation are the *exponents* of the equation at $z_0$.
Fuchs' theorem says when the series converges and how to get a second solution.

Example: for $z^2 y'' + z y' + (z^2 - \frac{1}{4}) y = 0$ at $z_0 = 0$, one has $p_0 = 1$, $q_0 = -\frac{1}{4}$, $q_2 = 1$, and all other $p_k, q_k$ vanish.
So $F(s) = s^2 - \frac{1}{4}$, with roots $r = \pm \frac{1}{2}$.
For $r = \frac{1}{2}$ the recurrence is $k (k + 1) a_k = - a_{k-2}$, with $a_1 = 0$, which gives $y = z^{-1/2} \sin z$ when $a_0 = 1$.

Non-example: at an irregular singular point the method can fail.
For $z^2 y'' + y' = 0$ at $0$, the only solutions of the form above are constants, while $y = \int e^{1/z}\, dz$ is a second solution whose derivative has an essential singularity at $0$.
