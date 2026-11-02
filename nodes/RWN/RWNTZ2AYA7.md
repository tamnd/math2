---
tag: RWNTZ2AYA7
kind: definition
name: Zeilberger's algorithm
msc: [33F10, 05A19, 68W30]
defines: VA7MH05Z3B
uses: [WC0QNABPZ4, NHMJQBS04M, 0FYX44GP92, 0GXKM1R7E4]
sources:
  - url: https://en.wikipedia.org/wiki/Wilf%E2%80%93Zeilberger_pair
---

## Definition

Let $F(n, k)$ be a hypergeometric term in both variables, as in the definition of a [[WZ pair|WC0QNABPZ4]].
*Zeilberger's algorithm* searches, for $J = 0, 1, 2, \ldots$ in turn, for polynomials $a_0(n), \ldots, a_J(n)$, not all zero, and a hypergeometric term $G(n, k)$ with $G/F$ rational, such that
$$\sum_{j=0}^{J} a_j(n)\,F(n + j, k) = G(n, k + 1) - G(n, k).$$
For each $J$ it applies [[Gosper's algorithm|NHMJQBS04M]] to the term $t_k = \sum_{j} a_j(n) F(n + j, k)$ in $k$, with unknown $a_j$.
The polynomial equation of Gosper's method is then linear in the $a_j$ and in the unknown coefficients of $x$.
It stops at the first $J$ for which a solution exists and returns the $a_j$ and $G$.

## Remarks

If $F(n, k)$ vanishes for $k$ outside a finite range depending on $n$, summing the relation over all $k$ makes the right side a [[telescoping sum|0GXKM1R7E4]] equal to $0$.
So $f(n) = \sum_k F(n, k)$ satisfies the [[recurrence|0FYX44GP92]] $\sum_{j=0}^{J} a_j(n) f(n + j) = 0$.
The search terminates when $F$ is a proper hypergeometric term.
Such a term is a polynomial, times a product of factorials of integer-linear forms in $n$ and $k$, times $x^k$.
This termination result is part of the fundamental theorem of Wilf and Zeilberger.
Example: for $F(n, k) = \binom{n}{k}$ the algorithm stops at $J = 1$ with $a_0 = -2$, $a_1 = 1$ and $G(n, k) = -\binom{n}{k - 1}$.
Check by Pascal's rule: $\binom{n + 1}{k} - 2\binom{n}{k} = \binom{n}{k - 1} - \binom{n}{k} = G(n, k + 1) - G(n, k)$, which gives $f(n + 1) = 2f(n)$.
Non-example: for $J = 0$ no solution exists here, since that would need $\sum_{j<k}\binom{n}{j}$ to be a hypergeometric term in $k$, and Gosper's algorithm shows it is not.
