---
tag: BRFPQM1MMW
kind: proof
name: Proof that the minimal polynomial divides every annihilating polynomial
msc: [15A18]
proves: 0VTAD25A3G
uses: [0V58FPM3EQ, 052M4SX57M, 0BNEXSKNRV, 0MES3KS0ZC, 0BDX4MBKT4]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 4.4
---

## Proof

We divide with remainder and use the minimality of the degree.

1. Let $m_T$ be the [[minimal polynomial|0V58FPM3EQ]] of $T$. It is [[monic|0BDX4MBKT4]], and it satisfies $m_T(T) = 0$. No nonzero polynomial of smaller degree annihilates $T$, since such a polynomial could be scaled to a monic one.
2. Let $p \in F[x]$ with $p(T) = 0$, so $p$ is an [[annihilating polynomial|052M4SX57M]] of $T$.
3. By the [[division algorithm for polynomials|0MES3KS0ZC]], applied with the monic divisor $m_T$, there are $q, r \in F[x]$ with $p = q m_T + r$ and $\deg r < \deg m_T$.
4. The map $f \mapsto f(T)$ of [[evaluation at $T$|0BNEXSKNRV]] respects sums and products, because powers of $T$ commute with each other. So $p(T) = q(T) m_T(T) + r(T)$.
5. Since $p(T) = 0$ and $m_T(T) = 0$, step 4 gives $r(T) = 0$.
6. If $r \ne 0$, then $r$ would be a nonzero annihilating polynomial with $\deg r < \deg m_T$. This contradicts step 1.
7. Hence $r = 0$ and $p = q m_T$. So $m_T$ divides $p$.

## Idea

Divide $p$ by $m_T$. The remainder still kills $T$, but it has smaller degree than $m_T$. The minimal polynomial has the least degree among nonzero annihilating polynomials, so the remainder must be zero.
