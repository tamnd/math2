---
tag: PPC7ZEFPQE
kind: proof
name: Proof that the minimal polynomial divides the characteristic polynomial
msc: [15A18]
proves: 093X6MN6Y6
uses: [0V58FPM3EQ, 039HF58KQ5, 0BNEXSKNRV, 0F765KFC2J, 0VTAD25A3G, 0T233AZ1GE, 0B5Z1EC66J]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Section 4, after Example 4.5
---

## Proof

We combine the Cayley–Hamilton theorem with the divisibility property of the minimal polynomial.

1. Let $p_A$ be the [[characteristic polynomial|039HF58KQ5]] of $A$. It is monic of degree $n$. Let $m_A$ be the [[minimal polynomial|0V58FPM3EQ]] of $A$.
2. Let $L \colon F^n \to F^n$ be the endomorphism $L(x) = A x$. For $p \in F[x]$, the [[value|0BNEXSKNRV]] $p(L)$ is the map $x \mapsto p(A) x$, because $L^k(x) = A^k x$ for all $k$.
3. A matrix $C$ is zero if and only if $C x = 0$ for all $x \in F^n$. So by step 2, $p(L) = 0$ if and only if $p(A) = 0$.
4. By step 3, $L$ and $A$ have the same annihilating polynomials, so $m_A = m_L$.
5. By the [[Cayley–Hamilton theorem|0F765KFC2J]], $p_A(A) = 0$. By step 3, $p_A(L) = 0$.
6. Since [[the minimal polynomial divides every annihilating polynomial|0VTAD25A3G]], $m_L$ divides $p_A$. By step 4, $m_A$ divides $p_A$.
7. Write $p_A = m_A q$ with $q \in F[x]$. Since $p_A \ne 0$, also $q \ne 0$, so $\deg q \ge 0$.
8. The ring $F[x]$ is an [[integral domain|0B5Z1EC66J]], since $F$ is a field. By the [[degree of a product|0T233AZ1GE]], $n = \deg p_A = \deg m_A + \deg q \ge \deg m_A$.
9. So $m_A$ divides $p_A$, and $\deg m_A \le n$.

## Idea

The Cayley–Hamilton theorem says that $p_A$ annihilates $A$. Every annihilating polynomial is a multiple of the minimal polynomial. A nonzero multiple has at least the same degree, which gives $\deg m_A \le n$.
