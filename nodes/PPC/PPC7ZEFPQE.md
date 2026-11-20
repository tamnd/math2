---
tag: PPC7ZEFPQE
kind: proof
name: Proof that the minimal polynomial divides the characteristic polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: 093X6MN6Y6
methods: [0NTF6DMVAP, XP5SDYKJX0, DX2H7AD66G]
uses: [0V58FPM3EQ, 039HF58KQ5, 0BZ81AJNWF, 0BNEXSKNRV, 0YYMY95FWS, 05Q1B7MH0M, 0F765KFC2J, 0VTAD25A3G, 0T233AZ1GE, 0B5Z1EC66J, 0Q9EZS90GY, 04CPJ6AF00, 0K1KKMFHYH]
sources:
  - url: https://kconrad.math.uconn.edu/blurbs/linmultialg/minpolyandappns.pdf
    locator: Section 4, after Example 4.5
  - book: isbn:9780135367971
---

## Proof

Reduction to matrices.

1. Choose a basis $B$ of $V$ and let $A = [T]_B$ be the [[matrix of T|0YYMY95FWS]]. By the [[definition of p_T|0BZ81AJNWF]], $p_T = p_A$.
2. The map $S \mapsto [S]_B$ preserves sums and scalar multiples, sends $\id_V$ to $I_n$, and sends composites to products, by the [[matrix of a composition|05Q1B7MH0M]]. So $[q(T)]_B = q(A)$ for every $q \in F[x]$, by the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]].
3. A map is zero if and only if its matrix is zero. So $q(T) = 0$ if and only if $q(A) = 0$. Hence $T$ and $A$ have the same annihilating polynomials and the same [[minimal polynomial|0V58FPM3EQ]].
4. By steps 1 and 3, it suffices to prove both parts for the matrix $A$. Write $m = m_A$ and $p = p_A$.

Part 1.

5. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $p(A) = 0$.
6. Since the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]], $m$ divides $p$. Write $p = mq$.
7. Since $p$ is monic of degree $n$, $p \ne 0$, so $q \ne 0$. The ring $F[x]$ is an [[integral domain|0B5Z1EC66J]], and by the [[degree of a product|0T233AZ1GE]], $n = \deg m + \deg q \ge \deg m$.

Part 2.
This part does not use the Cayley-Hamilton theorem.

8. Write $m(x) = \sum_{k=0}^{d} c_k x^k$ with $c_k \in F$. Then $m(A) = \sum_k c_k A^k = 0$.
9. Work in $M_n(F[x])$, the $n \times n$ matrices over the commutative ring $F[x]$ of [[polynomials|0Q9EZS90GY]]. The scalar $x$ commutes with every matrix.
10. For $k \ge 1$, let $H_k(x) = \sum_{j=0}^{k-1} x^{k-1-j} A^j$. Then
$$(xI - A) H_k(x) = \sum_{j=0}^{k-1} x^{k-j} A^j - \sum_{j=0}^{k-1} x^{k-1-j} A^{j+1} = x^k I - A^k,$$
because the two sums telescope.
11. Let $H(x) = \sum_{k=1}^{d} c_k H_k(x)$. By step 10, $(xI - A)H(x) = \sum_{k=1}^{d} c_k (x^k I - A^k)$.
12. Add $c_0 (x^0 I - A^0) = 0$ to the right side. It becomes $\sum_{k=0}^{d} c_k x^k I - \sum_{k=0}^{d} c_k A^k = m(x) I - m(A) = m(x) I$, by step 8.
13. The [[determinant is multiplicative|04CPJ6AF00]] over the commutative ring $F[x]$. So $\det(xI - A) \det H(x) = \det(m(x) I)$.
14. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det(m(x) I) = m(x)^n$. By the [[definition of the characteristic polynomial|039HF58KQ5]], $\det(xI - A) = p(x)$.
15. So $p \cdot \det H = m^n$ with $\det H \in F[x]$. Hence $p$ divides $m^n$.

## Idea

Part 1: the characteristic polynomial annihilates $A$, and every annihilating polynomial is a multiple of the minimal polynomial.

Part 2: the identity $x^k I - A^k = (xI - A)(x^{k-1} I + \cdots + A^{k-1})$ gives $m(x)I - m(A) = (xI - A)H(x)$.
Since $m(A) = 0$, the matrix $xI - A$ divides the scalar matrix $m(x)I$.
Taking determinants shows that $p$ divides $m^n$.

## Variants

- The same determinant argument with $p$ in place of $m$ cannot prove the Cayley-Hamilton theorem. It needs $m(A) = 0$ as input.
- Part 2 also follows from the invariant factor decomposition of $V$ as an $F[x]$-module, where $p$ is the product of the invariant factors and $m$ is the largest one.
