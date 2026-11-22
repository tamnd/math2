---
tag: D6FCM44PQW
kind: proof
name: Proof of the formulas for powers and polynomials of a Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
proves: B9CHNGJV5K
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [0PBFS92AJP, DS9TS6AFMW, 0FCCDXH97W, 0VTAD25A3G, 0W4FSW1TVB, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Functions of matrices
---

## Proof

We first find the powers of the shift $N = J - \lambda I$ on the standard basis, and then we expand $J = \lambda I + N$ with the binomial formula.

1. By the [[definition of a Jordan block|0PBFS92AJP]], column $i$ of $J$ has $\lambda$ in row $i$ and, for $i \ge 2$, a $1$ in row $i - 1$. So $J e_1 = \lambda e_1$ and $J e_i = \lambda e_i + e_{i-1}$ for $i \ge 2$, and subtracting $\lambda e_i$ gives $N e_1 = 0$ and $N e_i = e_{i-1}$.
2. We show by induction on $j$ that $N^j e_i = e_{i-j}$ when $i > j$ and $N^j e_i = 0$ when $i \le j$. The case $j = 0$ is $N^0 e_i = e_i$. For the step, $N^{j+1} e_i = N (N^j e_i)$, which is $N e_{i-j} = e_{i-j-1}$ when $i - j \ge 2$ and $0$ otherwise, by step 1.
3. By step 2, column $i + j$ of $N^j$ is $e_i$ for $1 \le i \le k - j$, and the first $j$ columns are $0$. This is the pattern of part 1.
4. The nonzero columns $e_1, \dots, e_{k-j}$ of $N^j$ are independent, so $\operatorname{rank} N^j = k - j$ for $j \le k$, and $N^k = 0$. This proves part 1.
5. The matrices $\lambda I$ and $N$ commute, since a scalar matrix commutes with every matrix. So the [[binomial theorem for commuting matrices|DS9TS6AFMW]] gives
$$J^m = (\lambda I + N)^m = \sum_{j=0}^{m} \binom{m}{j} \lambda^{m-j} N^j.$$
6. The terms with $j \ge k$ vanish because $N^k = 0$. By step 3, the term with index $j$ contributes $\binom{m}{j} \lambda^{m-j}$ in each position $(i, i + j)$ and nothing elsewhere. This proves part 2.
7. Substituting $J$ for $x$ is a ring homomorphism $F[x] \to M_k(F)$, the [[evaluation homomorphism|0FCCDXH97W]], and it sends $x - \lambda$ to $N$. So $f = \sum_j b_j (x - \lambda)^j$ goes to $f(J) = \sum_j b_j N^j$, and the terms with $j \ge k$ vanish. This proves part 3.
8. The matrices $I, N, \dots, N^{k-1}$ are linearly independent, because by step 3 their nonzero entries lie on different diagonals.
9. By step 7, $(x - \lambda)^k$ sends $J$ to $N^k = 0$. Conversely, if $f(J) = 0$, then $\sum_{j < k} b_j N^j = 0$, so $b_0 = \dots = b_{k-1} = 0$ by step 8, and $(x - \lambda)^k$ divides $f$.
10. So $(x - \lambda)^k$ is the monic polynomial of least degree that kills $J$, and it is the minimal polynomial by the [[divisibility property|0VTAD25A3G]]. This proves the first half of part 4.
11. The matrix $xI - J$ is upper triangular with every diagonal entry equal to $x - \lambda$. The [[determinant|0C3CFHDN6R]] of a triangular matrix is the product of its diagonal entries, so $\det(xI - J) = (x - \lambda)^k$. This proves the second half of part 4.
12. The eigenvalues are the roots of the characteristic polynomial, so $\lambda$ is the only one. By the [[rank-nullity theorem|0W4FSW1TVB]] and step 4, $\dim \ker N^j = k - (k - j) = j$ for $j \le k$, and $\dim \ker N^j = k$ for $j \ge k$ since then $N^j = 0$.
13. For $j = 1$, step 1 shows that $N$ kills $e_1$, so $\ker N = F e_1$ by the dimension count of step 12. This proves part 5.
14. By step 2, $N^j e_k = e_{k-j}$ for $0 \le j \le k - 1$, so the vectors $e_k, N e_k, \dots, N^{k-1} e_k$ are the basis $e_k, \dots, e_1$.
15. Each $J^j e_k = (\lambda I + N)^j e_k$ is a combination of the $N^i e_k$ with $i \le j$, in which $N^j e_k$ has coefficient $1$. So the matrix that expresses $e_k, J e_k, \dots, J^{k-1} e_k$ in the basis of step 14 is triangular with ones on the diagonal, and these vectors form a basis too. This proves part 6.

## Idea

Split the block into its scalar part $\lambda I$ and the shift $N$.
The two parts commute, so the binomial formula applies, and the shift dies after $k$ steps, so every sum stops after $k$ terms.
Every claim then comes from the shape of the powers of $N$: they are ones on a single diagonal that moves up by one each time.

## Variants

In characteristic $0$, part 3 is the Taylor formula $f(J) = \sum_{j < k} f^{(j)}(\lambda) N^j / j!$, and some books prove it by checking it on the monomials $x^m$ with part 2.
The minimal polynomial in part 4 also follows from part 6, because a cyclic matrix has equal minimal and characteristic polynomials.
A third route reads $J$ as multiplication by $x$ on $F[x]/((x - \lambda)^k)$, where the annihilator is visible at once.
