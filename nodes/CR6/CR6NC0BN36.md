---
tag: CR6NC0BN36
kind: proof
name: Proof of the density of the rationals
msc: [26A03]
proves: 0STX0WRDNG
uses: [0WH916TJNY, 0YVRNEDSVG, 0R9B0B5458, 0NCJ5WXN6Z, 0QSPNASE50]
sources:
  - url: https://proofwiki.org/wiki/Between_two_Real_Numbers_exists_Rational_Number
---

## Proof

1. Let $x$ and $y$ be real numbers with $x < y$. Then $y - x > 0$.
2. By the [[Archimedean property|0WH916TJNY]], there is a natural number $n \ge 1$ with $1/n < y - x$.
3. Let $k = \floor{n x}$ be the [[floor|0YVRNEDSVG]] of $n x$, and let $m = k + 1$. Then $m$ is an integer.
4. By the [[characterization of the floor|0R9B0B5458]], $k \le n x < k + 1$. That is, $m - 1 \le n x < m$.
5. Divide by $n > 0$, which keeps the order in the [[ordered field|0QSPNASE50]] $\R$. This gives $m/n - 1/n \le x < m/n$.
6. So $x < m/n$. Also $m/n \le x + 1/n < x + (y - x) = y$, by steps 2 and 5.
7. Let $q = m/n$. It is a [[rational number|0NCJ5WXN6Z]], since $m$ and $n$ are integers and $n \ne 0$. By step 6, $x < q < y$.

## Idea

Choose a step size $1/n$ smaller than the gap $y - x$. The grid of fractions $m/n$ cannot jump over the gap, so the first grid point to the right of $x$ is still below $y$.
