---
tag: BRFPQM1MMW
kind: proof
name: Proof that the minimal polynomial divides every annihilating polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 0VTAD25A3G
methods: [0NTF6DMVAP, 0J0XBKG64S]
uses: [0V58FPM3EQ, 052M4SX57M, 0BNEXSKNRV, 0MES3KS0ZC, 0BDX4MBKT4]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Theorem 4.4
  - book: isbn:9780135367971
---

## Proof

We divide $p$ by $m_T$ with remainder and show that the remainder must be zero, because it would otherwise be an annihilating polynomial of too small a degree.

1. Let $m_T$ be the [[minimal polynomial|0V58FPM3EQ]] of $T$.
   It is [[monic|0BDX4MBKT4]] and satisfies $m_T(T) = 0$.
2. No nonzero polynomial $r$ with $\deg r < \deg m_T$ annihilates $T$.
   Indeed, dividing such an $r$ by its leading coefficient $c$ would give a monic polynomial $c^{-1} r$ with $(c^{-1} r)(T) = c^{-1} r(T) = 0$ and smaller degree than $m_T$, which contradicts the definition of $m_T$.
3. Let $p \in F[x]$ with $p(T) = 0$, so $p$ is an [[annihilating polynomial|052M4SX57M]] of $T$.
4. The [[division algorithm for polynomials|0MES3KS0ZC]], applied to $p$ and the monic divisor $m_T$, gives $q, r \in F[x]$ with
$$p = q\, m_T + r, \qquad r = 0 \text{ or } \deg r < \deg m_T.$$
5. Evaluation at $T$, the map $f \mapsto f(T)$ of [[values at T|0BNEXSKNRV]], respects sums and products, because all powers of $T$ commute with each other.
   So step 4 gives
$$p(T) = q(T)\, m_T(T) + r(T).$$
6. In step 5, $p(T) = 0$ by step 3 and $m_T(T) = 0$ by step 1, so $r(T) = 0$.
7. If $r \ne 0$, then $r$ is a nonzero annihilating polynomial with $\deg r < \deg m_T$, which step 2 forbids.
   So $r = 0$.
8. Step 4 now reads $p = q\, m_T$, so $m_T$ divides $p$.
9. Conversely, let $p = q\, m_T$ for some $q \in F[x]$.
   By step 5, $p(T) = q(T)\, m_T(T) = q(T) \circ 0 = 0$, so $p$ annihilates $T$.

Steps 3 to 8 show that every annihilating polynomial is a multiple of $m_T$, and step 9 shows that every multiple of $m_T$ annihilates $T$.

## Idea

Divide $p$ by $m_T$, as you would divide one whole number by another.
The remainder is $p$ minus a multiple of $m_T$, so it still kills $T$, but its degree is smaller than that of $m_T$.
The minimal polynomial has the least degree among the nonzero polynomials that kill $T$, so the only way out is that the remainder is $0$.

## Variants

In the language of ideals, the annihilating polynomials form an ideal of the principal ideal domain $F[x]$, and $m_T$ is its monic generator, so every element of the ideal is a multiple of $m_T$.
The theorem that [[the ideal of annihilating polynomials is nonzero and principal|AH34SFJ8SF]] takes this route.
The two proofs are the same at heart, since $F[x]$ is a principal ideal domain because of the division argument used here.
