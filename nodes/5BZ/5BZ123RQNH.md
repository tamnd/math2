---
tag: 5BZ123RQNH
kind: proof
name: Proof of Sylvester's criterion by induction and completing the square
msc: [15B57, 15A15]
topics: [SS4EVPKT3A]
audience: ug1
proves: 0WKEF78PMV
methods: [0ASJVEFA9J, TFQ1845T84, 0NTF6DMVAP]
uses: [0QQCG3JWJ4, 0880F9EQCP, 0EKZCX4K3P, 0EX045E2BP, 0SD528P0EK, 0JP0W07Y9A, 053QVHF6N7, 0HYC2RHD3M, 0C2F40MEBC, FBSAPTP1PR, 0K1KKMFHYH, 0J9TVTNB4K, 04CPJ6AF00, 09GK5PS824, 0PPG793642, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: Proof for the case of positive definite matrices
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: Proof for the case of positive semidefinite matrices
---

## Proof

For $1 \le k \le n$, let $A_k$ be the upper left $k \times k$ submatrix of $A$, so that $\Delta_k = \det A_k$ is a leading [[minor|0SD528P0EK]].
For a nonempty $S \subseteq \set{1, \dots, n}$, let $A_S$ be the principal submatrix on $S$.

*Part 1.*

1. Each $A_S$ is [[Hermitian|0EKZCX4K3P]], since its $(i, j)$ entry is $a_{ij} = \overline{a_{ji}}$. In particular each $A_k$ is Hermitian.
2. Let $z \in \C^S$, and let $x \in \C^n$ have the entries of $z$ at the positions in $S$ and zeros elsewhere. Then $x^* A x = z^* A_S z$, where $^*$ is the [[conjugate transpose|0EX045E2BP]], and $x = 0$ only if $z = 0$.
3. Assume that $A$ is [[positive definite|0QQCG3JWJ4]], and fix $k$. By step 2 with $S = \set{1, \dots, k}$, $z^* A_k z > 0$ for every $z \ne 0$. So $A_k$ is positive definite.
4. By the [[fundamental theorem of algebra|0JP0W07Y9A]], the characteristic polynomial of $A_k$ splits over $\C$ as $(t - \lambda_1) \cdots (t - \lambda_k)$.
5. Each $\lambda_i$ is a root of the characteristic polynomial, so it is an [[eigenvalue|053QVHF6N7]] of $A_k$. By the [[eigenvalue test|0HYC2RHD3M]] and step 3, each $\lambda_i$ is a positive real.
6. Since the [[determinant is the product of the eigenvalues|0C2F40MEBC]], $\Delta_k = \lambda_1 \cdots \lambda_k > 0$. This proves one direction of part 1.
7. For the converse we argue by induction on $n$. Assume $\Delta_k > 0$ for all $k$. For $n = 1$, $A = (a)$ with $a = \Delta_1 > 0$, and $x^* A x = a \abs{x}^2 > 0$ for $x \ne 0$.
8. Let $n \ge 2$, and let $A' = A_{n-1}$. The leading minors of $A'$ are $\Delta_1, \dots, \Delta_{n-1}$, which are positive. By step 1 and the induction hypothesis, $A'$ is positive definite.
9. Since $A$ is Hermitian, it has the block form $A = \begin{pmatrix} A' & b \\ b^* & c \end{pmatrix}$ with $b \in \C^{n-1}$ and $c \in \R$.
10. Since $\det A' = \Delta_{n-1} \ne 0$, the matrix $A'$ is [[invertible|FBSAPTP1PR]]. Conjugating $A' A'^{-1} = I$ gives $(A'^{-1})^* A' = I$, using $(XY)^* = Y^* X^*$ from the [[transpose of a product|09GK5PS824]].
11. By step 10, $(A'^{-1})^* = A'^{-1}$, since a matrix has only one inverse.
12. Let $u = A'^{-1} b$ and $s = c - b^* u$. Let $P = \begin{pmatrix} I & -u \\ 0 & 1 \end{pmatrix}$, where $I$ is the $(n-1) \times (n-1)$ identity.
13. Block multiplication gives $AP = \begin{pmatrix} A' & b - A'u \\ b^* & c - b^* u \end{pmatrix} = \begin{pmatrix} A' & 0 \\ b^* & s \end{pmatrix}$.
14. We have $P^* = \begin{pmatrix} I & 0 \\ -u^* & 1 \end{pmatrix}$, and $u^* = b^* (A'^{-1})^* = b^* A'^{-1}$ by step 11. So $u^* A' = b^*$.
15. By steps 13 and 14, $P^* A P = \begin{pmatrix} A' & 0 \\ b^* - u^* A' & s \end{pmatrix} = \begin{pmatrix} A' & 0 \\ 0 & s \end{pmatrix}$.
16. The matrices $P$ and $P^*$ are triangular with all diagonal entries $1$. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det P = \det P^* = 1$.
17. By the [[multiplicativity of the determinant|04CPJ6AF00]] and the [[determinant of a block triangular matrix|0J9TVTNB4K]], $\Delta_n = \det(P^* A P) = \Delta_{n-1}\, s$.
18. So $s = \Delta_n / \Delta_{n-1} > 0$.
19. Let $x \in \C^n$ with $x \ne 0$. By step 16, $P$ is invertible. Let $y = P^{-1} x$, so $y \ne 0$. Write $y = (y', y_n)$ with $y' \in \C^{n-1}$.
20. By step 15, $x^* A x = y^* P^* A P y = y'^* A' y' + s \abs{y_n}^2$.
21. Both terms are at least $0$, by steps 8 and 18. If $y' \ne 0$, the first term is positive. Otherwise $y_n \ne 0$, and the second term is positive.
22. So $x^* A x > 0$ for all $x \ne 0$. As $A$ is Hermitian, $A$ is positive definite. This completes the induction and the proof of part 1.

*Part 2.*

23. Assume that $A$ is [[positive semidefinite|0880F9EQCP]], and let $S$ be nonempty. By step 2, $z^* A_S z = x^* A x \ge 0$ for every $z$. So $A_S$ is positive semidefinite.
24. As in steps 4 to 6, $\det A_S$ is the product of the eigenvalues of $A_S$. By the eigenvalue test and step 23, they are all nonnegative. So $\det A_S \ge 0$.
25. Conversely, assume $\det A_S \ge 0$ for all nonempty $S$. Fix $\varepsilon > 0$ and $k \in \set{1, \dots, n}$. Row $i$ of $A_k + \varepsilon I_k$ is $r_i + \varepsilon e_i^T$, where $r_i$ is row $i$ of $A_k$.
26. The determinant is linear in each row, by the [[multilinearity in rows|0PPG793642]]. Expanding all $k$ rows gives a sum over the sets $T \subseteq \set{1, \dots, k}$ of the rows that take the part $\varepsilon e_i^T$.
27. Fix $T$, and let $M_T$ have row $\varepsilon e_i^T$ for $i \in T$ and row $r_i$ for $i \notin T$. By the [[Laplace expansion|0C08BQ3M05]] along a row $\varepsilon e_i^T$, $\det M_T = \varepsilon \cdot (-1)^{i+i} \det M'$. Here $M'$ is $M_T$ without row $i$ and column $i$.
28. Repeating step 27 for each $i \in T$ gives $\det M_T = \varepsilon^{\abs{T}} \det A_{S}$ with $S = \set{1, \dots, k} \setminus T$. For $T = \set{1, \dots, k}$, we read $\det A_\emptyset = 1$.
29. By steps 26 to 28, $\det(A_k + \varepsilon I_k) = \varepsilon^k + \sum_{\emptyset \ne S \subseteq \set{1, \dots, k}} \varepsilon^{k - \abs{S}} \det A_S$.
30. Every $\det A_S$ in step 29 is a principal minor of $A$, so it is at least $0$ by assumption. So $\det(A_k + \varepsilon I_k) \ge \varepsilon^k > 0$.
31. The upper left $k \times k$ submatrix of $A + \varepsilon I_n$ is $A_k + \varepsilon I_k$. The matrix $A + \varepsilon I_n$ is Hermitian, since $\varepsilon$ is real. By step 30 and part 1, $A + \varepsilon I_n$ is positive definite.
32. Let $x \in \C^n$. By step 31, $x^* A x + \varepsilon \norm{x}^2 = x^* (A + \varepsilon I_n) x \ge 0$ for every $\varepsilon > 0$.
33. Letting $\varepsilon \to 0$ in step 32 gives $x^* A x \ge 0$. So $A$ is positive semidefinite. This proves part 2.

## Idea

Positive definiteness passes to the top left blocks, and a positive definite matrix has positive determinant.
For the converse, a change of variables splits off the last coordinate, and the determinants show that the new coefficient $s = \Delta_n / \Delta_{n-1}$ is positive.
For semidefiniteness, add $\varepsilon I$: the leading minors of $A + \varepsilon I$ are polynomials in $\varepsilon$ with nonnegative coefficients, the principal minors of $A$, so part 1 applies and $\varepsilon \to 0$ finishes.

## Variants

- Part 1 can also be proved with the [[Cholesky decomposition|0WKG8CYY6A]]: Gaussian elimination without row exchanges has the pivots $\Delta_k / \Delta_{k-1}$.
- In part 2, the direction from principal minors to semidefiniteness can also use the characteristic polynomial. Its coefficients alternate in sign, so it has no negative roots, and the eigenvalue test applies.
