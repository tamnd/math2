---
tag: 5BZ123RQNH
kind: proof
name: Proof of Sylvester's criterion by induction and completing the square
msc: [15B57, 15A15]
proves: 0WKEF78PMV
uses: [0QQCG3JWJ4, 0EKZCX4K3P, 0EX045E2BP, 0SD528P0EK, 0JP0W07Y9A, 053QVHF6N7, 0HYC2RHD3M, 0C2F40MEBC, FBSAPTP1PR, 0K1KKMFHYH, 0J9TVTNB4K, 04CPJ6AF00, 09GK5PS824]
sources:
  - url: https://en.wikipedia.org/wiki/Sylvester's_criterion
    locator: Proof for the case of positive definite matrices
---

## Proof

For $1 \le k \le n$, let $A_k$ be the upper left $k \times k$ submatrix of $A$, so that $\Delta_k = \det A_k$ is a leading [[minor|0SD528P0EK]].

1. Each $A_k$ is [[Hermitian|0EKZCX4K3P]]. Indeed its $(i, j)$ entry is $a_{ij} = \overline{a_{ji}}$, because $A$ is Hermitian.
2. First assume that $A$ is [[positive definite|0QQCG3JWJ4]], and fix $k$. Let $z \in \C^k$ with $z \ne 0$, and let $x \in \C^n$ be $z$ followed by $n - k$ zeros.
3. Then $x \ne 0$, and $x^* A x = z^* A_k z$, where $^*$ is the [[conjugate transpose|0EX045E2BP]]. So $z^* A_k z > 0$, and $A_k$ is positive definite.
4. By the [[fundamental theorem of algebra|0JP0W07Y9A]], the characteristic polynomial of $A_k$ splits over $\C$ as $(t - \lambda_1) \cdots (t - \lambda_k)$.
5. Each $\lambda_i$ is a root of the characteristic polynomial, so it is an [[eigenvalue|053QVHF6N7]] of $A_k$. By [[the positivity of eigenvalues|0HYC2RHD3M]] and step 3, each $\lambda_i$ is a positive real.
6. Since the [[determinant is the product of the eigenvalues|0C2F40MEBC]], $\Delta_k = \lambda_1 \cdots \lambda_k > 0$. This proves one direction.
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
22. So $x^* A x > 0$ for all $x \ne 0$. As $A$ is Hermitian, $A$ is positive definite. This completes the induction and the proof.

## Idea

Positive definiteness passes to the top left blocks, and a positive definite matrix has positive determinant. For the converse, a change of variables splits off the last coordinate. It writes the form as the form of $A_{n-1}$ plus $s \abs{y_n}^2$, and the determinants show that $s = \Delta_n / \Delta_{n-1}$ is positive.
