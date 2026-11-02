---
tag: KJF8Y19BNV
kind: statement
role: theorem
name: Routh–Hurwitz stability criterion
msc: [26C10, 93D20, 34D20]
uses: [9A3TBBHRFA, 019MA1VTR2, 0BT9BYWVRY, 0VSSPAFM2C, 09ZWYRQ41J]
about: [9A3TBBHRFA]
sources:
  - url: https://en.wikipedia.org/wiki/Routh%E2%80%93Hurwitz_stability_criterion
same_as:
  wikidata: Q2621270
  wikipedia: Routh–Hurwitz stability criterion
---

## Statement

Let $p(s) = a_0 s^n + a_1 s^{n-1} + \cdots + a_{n-1} s + a_n$ be a polynomial of degree $n \ge 1$ with real coefficients and $a_0 > 0$.
Put $a_k = 0$ for $k < 0$ and for $k > n$.
Let $H$ be the $n \times n$ Hurwitz matrix with entries $H_{ij} = a_{2j - i}$ for $1 \le i, j \le n$, and let $\Delta_k$ be its leading principal [[minor|0BT9BYWVRY]] of order $k$.
Then every [[root|019MA1VTR2]] of $p$ has negative real part if and only if $\Delta_k > 0$ for $k = 1, \ldots, n$.

## Remarks

The rows of $H$ are $(a_1, a_3, a_5, \ldots)$, $(a_0, a_2, a_4, \ldots)$, $(0, a_1, a_3, \ldots)$, $(0, a_0, a_2, \ldots)$, and so on.
One proof counts the roots of $p$ in the right half-plane by following the argument of $p(i\omega)$ as $\omega$ runs over $\R$.
Routh's array computes the same information by a Euclidean algorithm on the even and odd parts of $p$.

For $n = 2$ and $p(s) = s^2 + a_1 s + a_2$, the conditions are $a_1 > 0$ and $a_1 a_2 > 0$, that is, $a_1 > 0$ and $a_2 > 0$.
For $n = 3$, they are $a_1 > 0$, $a_1 a_2 - a_0 a_3 > 0$ and $a_3 > 0$, since $\Delta_3 = a_3 \Delta_2$.
Positive coefficients are necessary but not sufficient when $n \ge 3$.
For $p(s) = s^3 + s^2 + s + 1 = (s + 1)(s^2 + 1)$, all coefficients are positive, but $\Delta_2 = 1 - 1 = 0$, and indeed $\pm i$ are roots.

## Explanations

### L1 human

To know whether a linear system returns to rest, one must know whether all roots of its characteristic polynomial lie in the left half-plane.
The criterion answers this from the coefficients alone, by checking that some determinants are positive.
No root has to be computed.

### L2 human

Applied to the [[characteristic polynomial|0VSSPAFM2C]] of a real matrix $A$, the criterion tests whether $A$ is [[Hurwitz-stable|9A3TBBHRFA]].
With the [[linearisation|09ZWYRQ41J]] of a nonlinear system, it gives a test for the stability of an equilibrium that uses only arithmetic on the entries of the Jacobian matrix.
It is the standard tool in control engineering for stability with respect to parameters, since the conditions are explicit inequalities.
The analogous test for roots inside the unit disc, used for discrete-time systems, is the Schur–Cohn or Jury test.
