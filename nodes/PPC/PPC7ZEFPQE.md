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

We reduce to a matrix $A$, get part 1 from the Cayley-Hamilton theorem, and get part 2 by taking determinants in a factorization of $m(x) I$.

*Reduction to matrices.*

1. Choose a basis $B$ of $V$ and let $A = [T]_B$ be the [[matrix of T in B|0YYMY95FWS]].
   By the [[definition of the characteristic polynomial of a linear map|0BZ81AJNWF]], $p_T = p_A$.
2. The map $S \mapsto [S]_B$ keeps sums and scalar multiples, sends $\mathrm{id}_V$ to $I_n$, and sends compositions to products by the rule for the [[matrix of a composition|05Q1B7MH0M]].
   So $[q(T)]_B = q(A)$ for every $q \in F[x]$, by the definition of the [[value of a polynomial at an endomorphism|0BNEXSKNRV]].
3. A map is zero exactly when its matrix is zero, so $q(T) = 0$ exactly when $q(A) = 0$.
   Hence $T$ and $A$ have the same annihilating polynomials and the same [[minimal polynomial|0V58FPM3EQ]].
4. By steps 1 and 3 it is enough to prove both parts for $A$.
   Write $m = m_A$ and $p = p_A$.

*Part 1.*

5. By the [[Cayley-Hamilton theorem|0F765KFC2J]], $p(A) = 0$.
6. Since the [[minimal polynomial divides every annihilating polynomial|0VTAD25A3G]], $m$ divides $p$.
   Write $p = mq$ with $q \in F[x]$.
7. The polynomial $p$ is monic of degree $n$, so $p \ne 0$ and hence $q \ne 0$.
   Since $F[x]$ is an [[integral domain|0B5Z1EC66J]], the rule for the [[degree of a product|0T233AZ1GE]] gives $n = \deg m + \deg q \ge \deg m$.

*Part 2, without the Cayley-Hamilton theorem.*

8. Write $m(x) = \sum_{k=0}^{d} c_k x^k$ with $c_k \in F$, so that $m(A) = \sum_k c_k A^k = 0$.
9. We work in the ring of $n \times n$ matrices over the commutative ring $F[x]$ of [[polynomials|0Q9EZS90GY]], where the scalar $x$ commutes with every matrix.
10. For $k \ge 1$ put $H_k(x) = \sum_{j=0}^{k-1} x^{k-1-j} A^j$.
    Multiply out and cancel the terms that appear in both sums:
$$(xI - A) H_k(x) = \sum_{j=0}^{k-1} x^{k-j} A^j - \sum_{j=0}^{k-1} x^{k-1-j} A^{j+1} = x^k I - A^k.$$
11. Let $H(x) = \sum_{k=1}^{d} c_k H_k(x)$.
    By step 10, $(xI - A) H(x) = \sum_{k=1}^{d} c_k (x^k I - A^k)$.
12. The term for $k = 0$ would be $c_0 (I - I) = 0$, so we may add it to the sum.
    By step 8 the right side becomes
$$\sum_{k=0}^{d} c_k x^k I - \sum_{k=0}^{d} c_k A^k = m(x) I - m(A) = m(x) I.$$
13. The [[determinant is multiplicative|04CPJ6AF00]] over the commutative ring $F[x]$, so $\det(xI - A) \det H(x) = \det(m(x) I)$.
14. The matrix $m(x) I$ is diagonal, so by the rule for the [[determinant of a triangular matrix|0K1KKMFHYH]] its determinant is $m(x)^n$.
    By the [[definition of the characteristic polynomial|039HF58KQ5]], $\det(xI - A) = p(x)$.
15. So $p \cdot \det H = m^n$ with $\det H \in F[x]$, and hence $p$ divides $m^n$.

## Idea

Part 1 is two facts in a row: the characteristic polynomial kills $A$, and every polynomial that kills $A$ is a multiple of the minimal one.

Part 2 rests on the factorization $x^k - a^k = (x - a)(x^{k-1} + x^{k-2} a + \cdots + a^{k-1})$, which stays true with a matrix $A$ in place of $a$ because $x$ commutes with $A$.
Adding these with the coefficients of $m$ gives $m(x) I - m(A) = (xI - A) H(x)$, and $m(A) = 0$ leaves $m(x) I = (xI - A) H(x)$.
Taking determinants turns this matrix factorization into the polynomial factorization $m^n = p \cdot \det H$.
For $A = I_2$ and $m = x - 1$, the matrix $H$ is $I$, and the equation reads $(x - 1)^2 = (x - 1)^2 \cdot 1$.

## Variants

The determinant argument of part 2 cannot be turned around to prove the Cayley-Hamilton theorem, because it needs $m(A) = 0$ as its input.
Both parts also follow from the invariant factor decomposition of $V$ as an $F[x]$-module, in which $p$ is the product of the invariant factors and $m$ is the largest of them.
