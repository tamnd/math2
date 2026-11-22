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

For part 1 we restrict the form to corners in one direction, and in the other direction we split off the last coordinate by a block change of variables and use induction on $n$.
For part 2 we add $\varepsilon I$, apply part 1, and let $\varepsilon \to 0$.
Throughout, $A_k$ is the upper left $k \times k$ submatrix of $A$, so $\Delta_k = \det A_k$ is a leading [[minor|0SD528P0EK]], and $A_S$ is the principal submatrix on a nonempty set $S \subseteq \{1, \dots, n\}$.

*Part 1, definite implies positive minors.*

1. Each $A_S$ is [[Hermitian|0EKZCX4K3P]], since its $(i, j)$ entry is $a_{ij} = \overline{a_{ji}}$. In particular each $A_k$ is Hermitian.
2. Let $z \in \C^S$, and let $x \in \C^n$ have the entries of $z$ at the positions in $S$ and zeros elsewhere. Then $x^* A x = z^* A_S z$, where $^*$ is the [[conjugate transpose|0EX045E2BP]], and $x = 0$ only if $z = 0$.
3. Assume that $A$ is [[positive definite|0QQCG3JWJ4]], and fix $k$. By step 2 with $S = \{1, \dots, k\}$, $z^* A_k z > 0$ for every $z \ne 0$, so $A_k$ is positive definite.
4. By the [[fundamental theorem of algebra|0JP0W07Y9A]], the characteristic polynomial of $A_k$ splits over $\C$ as $(t - \lambda_1) \cdots (t - \lambda_k)$, and each $\lambda_i$ is an [[eigenvalue|053QVHF6N7]] of $A_k$.
5. By the [[eigenvalue test|0HYC2RHD3M]] and step 3, each $\lambda_i$ is a positive real number.
6. Since the [[determinant is the product of the eigenvalues|0C2F40MEBC]], $\Delta_k = \lambda_1 \cdots \lambda_k > 0$.

*Part 1, positive minors imply definite.*

7. We use induction on $n$, and assume that $\Delta_k > 0$ for all $k$. For $n = 1$, $A = (a)$ with $a = \Delta_1 > 0$, and $x^* A x = a \abs{x}^2 > 0$ for $x \ne 0$.
8. Let $n \ge 2$ and $A' = A_{n-1}$. The leading minors of $A'$ are $\Delta_1, \dots, \Delta_{n-1}$, which are positive, so $A'$ is positive definite by step 1 and the induction hypothesis.
9. Since $A$ is Hermitian, it has the block form $A = \begin{pmatrix} A' & b \\ b^* & c \end{pmatrix}$ with $b \in \C^{n-1}$ and $c \in \R$.
10. Since $\det A' = \Delta_{n-1} \ne 0$, the matrix $A'$ is [[invertible|FBSAPTP1PR]]. Taking the conjugate transpose of $A' A'^{-1} = I$ and using $(XY)^* = Y^* X^*$ from the [[transpose of a product|09GK5PS824]] gives $(A'^{-1})^* A' = I$, so $(A'^{-1})^* = A'^{-1}$ by uniqueness of inverses.
11. Let $u = A'^{-1} b$, let $s = c - b^* u$, and let $P = \begin{pmatrix} I & -u \\ 0 & 1 \end{pmatrix}$ with $I$ the $(n-1) \times (n-1)$ identity.
12. Block multiplication gives
$$AP = \begin{pmatrix} A' & b - A' u \\ b^* & c - b^* u \end{pmatrix} = \begin{pmatrix} A' & 0 \\ b^* & s \end{pmatrix}.$$
13. We have $P^* = \begin{pmatrix} I & 0 \\ -u^* & 1 \end{pmatrix}$, and $u^* = b^* (A'^{-1})^* = b^* A'^{-1}$ by step 10, so $u^* A' = b^*$.
14. By steps 12 and 13,
$$P^* A P = \begin{pmatrix} A' & 0 \\ b^* - u^* A' & s \end{pmatrix} = \begin{pmatrix} A' & 0 \\ 0 & s \end{pmatrix}.$$
15. The matrices $P$ and $P^*$ are triangular with every diagonal entry $1$, so $\det P = \det P^* = 1$ by the [[determinant of a triangular matrix|0K1KKMFHYH]].
16. By the [[multiplicativity of the determinant|04CPJ6AF00]] and the [[determinant of a block triangular matrix|0J9TVTNB4K]], $\Delta_n = \det(P^* A P) = \Delta_{n-1} s$, so $s = \Delta_n / \Delta_{n-1} > 0$.
17. Let $x \ne 0$. By step 15, $P$ is invertible, so $y = P^{-1} x \ne 0$. Write $y = (y', y_n)$ with $y' \in \C^{n-1}$.
18. By step 14,
$$x^* A x = y^* P^* A P y = y'^* A' y' + s \abs{y_n}^2.$$
19. Both terms are at least $0$, by steps 8 and 16. If $y' \ne 0$, the first term is positive, and otherwise $y_n \ne 0$ and the second term is positive.
20. So $x^* A x > 0$ for all $x \ne 0$, and $A$ is positive definite. This completes the induction and the proof of part 1.

*Part 2, semidefinite implies nonnegative principal minors.*

21. Assume that $A$ is [[positive semidefinite|0880F9EQCP]], and let $S$ be nonempty. By step 2, $z^* A_S z = x^* A x \ge 0$ for every $z$, so $A_S$ is positive semidefinite.
22. As in steps 4 to 6, $\det A_S$ is the product of the eigenvalues of $A_S$, and these are nonnegative by the eigenvalue test. So $\det A_S \ge 0$.

*Part 2, nonnegative principal minors imply semidefinite.*

23. Assume $\det A_S \ge 0$ for all nonempty $S$. Fix $\varepsilon > 0$ and $k \in \{1, \dots, n\}$. Row $i$ of $A_k + \varepsilon I_k$ is $r_i + \varepsilon e_i^{\mathsf{T}}$, where $r_i$ is row $i$ of $A_k$.
24. The determinant is linear in each row, by [[multilinearity in rows|0PPG793642]]. Expanding all $k$ rows gives a sum over the sets $T \subseteq \{1, \dots, k\}$ of rows that take the part $\varepsilon e_i^{\mathsf{T}}$.
25. Fix $T$, and let $M_T$ have row $\varepsilon e_i^{\mathsf{T}}$ for $i \in T$ and row $r_i$ for $i \notin T$. The [[Laplace expansion|0C08BQ3M05]] along a row $\varepsilon e_i^{\mathsf{T}}$ gives $\det M_T = \varepsilon \det M'$, where $M'$ deletes row $i$ and column $i$, since the sign is $(-1)^{i+i} = 1$.
26. Repeating step 25 for each $i \in T$ gives $\det M_T = \varepsilon^{\abs{T}} \det A_S$ with $S = \{1, \dots, k\} \setminus T$, where we read $\det A_\emptyset = 1$.
27. By steps 24 to 26,
$$\det(A_k + \varepsilon I_k) = \varepsilon^k + \sum_{\emptyset \ne S \subseteq \{1, \dots, k\}} \varepsilon^{k - \abs{S}} \det A_S.$$
28. Every $\det A_S$ in step 27 is a principal minor of $A$, so it is at least $0$ by assumption, and $\det(A_k + \varepsilon I_k) \ge \varepsilon^k > 0$.
29. The upper left $k \times k$ submatrix of $A + \varepsilon I_n$ is $A_k + \varepsilon I_k$, and $A + \varepsilon I_n$ is Hermitian, since $\varepsilon$ is real. By step 28 and part 1, $A + \varepsilon I_n$ is positive definite.
30. Let $x \in \C^n$. By step 29, $x^* A x + \varepsilon \norm{x}^2 = x^* (A + \varepsilon I_n) x \ge 0$ for every $\varepsilon > 0$.
31. Letting $\varepsilon \to 0$ in step 30 gives $x^* A x \ge 0$. So $A$ is positive semidefinite, which proves part 2.

## Idea

Positive definiteness passes to every corner of the matrix, and a positive definite matrix has a positive determinant, which gives one direction.
For the other direction, a block change of variables completes the square in the last coordinate and leaves the form $y'^* A' y' + s \abs{y_n}^2$.
The determinants show that the new coefficient is $s = \Delta_n / \Delta_{n-1}$, which is positive, and induction handles $A'$.
For semidefiniteness, adding $\varepsilon I$ turns each leading minor into a polynomial in $\varepsilon$ whose coefficients are principal minors of $A$, so part 1 applies, and $\varepsilon \to 0$ finishes.

## Variants

Part 1 can also be proved with the [[Cholesky decomposition|0WKG8CYY6A]] or with $LDL^*$: Gaussian elimination without row exchanges has the pivots $\Delta_k / \Delta_{k-1}$, and the form is a sum of squares with these pivots as weights.

In part 2, the direction from principal minors to semidefiniteness can also use the characteristic polynomial.
Write $\det(tI - A) = t^n - E_1 t^{n-1} + E_2 t^{n-2} - \dots + (-1)^n E_n$, where $E_k \ge 0$ is the sum of the principal minors of size $k$.
For $t < 0$ every term has the sign of $(-1)^n$ and the first term is nonzero, so there is no negative root, and the eigenvalue test applies.
