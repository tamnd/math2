---
tag: 7QN4QQGW33
kind: proof
name: Proof of the normal form of a real normal operator
msc: ["15A21", "47B15"]
topics: [3YM9EK6VMB]
audience: grad
proves: G6T1FNE3JC
uses: [V1JG4C7R7B, 0XYKE8BE7X, 0QRBVFJ50X, 0Y4NF1DRKD, 0C4NT4GT3X, 0DBTE6HVBD, 0Y85GYEGSF, 03RNVFDEAN]
methods: [0ASJVEFA9J, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Skew-symmetric_matrix
    locator: Spectral theory
  - book: isbn:9783319110790
    locator: Section 9.B
---

## Proof

We start from the real Schur form and show that normality kills all blocks above the diagonal.

1. Let $A$ be real and normal. By part 3 of [[the Schur decomposition|V1JG4C7R7B]], $A = Q M Q^T$ with $Q$ real [[orthogonal|0QRBVFJ50X]]. Here $M$ is block upper triangular, and each diagonal block is $1 \times 1$ or a $2 \times 2$ block with no real eigenvalue.
2. $M$ is [[normal|0XYKE8BE7X]]: $M M^T = Q^T A Q Q^T A^T Q = Q^T A A^T Q$, and in the same way $M^T M = Q^T A^T A Q$. These agree, because $A A^T = A^T A$.
3. Claim: a normal block upper triangular matrix is block diagonal, and its diagonal blocks are normal. We use induction on the number of diagonal blocks. One block is already block diagonal.
4. For more blocks, write $M = \begin{pmatrix} B & C \\ 0 & D \end{pmatrix}$, where $B$ is the first diagonal block. Then $D$ is block upper triangular with one block fewer.
5. The upper left block of $M M^T$ is $B B^T + C C^T$. The upper left block of $M^T M$ is $B^T B$. By step 2 they are equal.
6. Take traces. By the [[cyclic property of the trace|0Y4NF1DRKD]], $\operatorname{tr}(B B^T) = \operatorname{tr}(B^T B)$. So $\operatorname{tr}(C C^T) = 0$.
7. $\operatorname{tr}(C C^T)$ is the sum of the squares of all entries of $C$. These squares are real and nonnegative, so all entries are $0$, and $C = 0$.
8. Then $M M^T = \begin{pmatrix} B B^T & 0 \\ 0 & D D^T \end{pmatrix}$ and $M^T M = \begin{pmatrix} B^T B & 0 \\ 0 & D^T D \end{pmatrix}$. So $B$ and $D$ are normal. By induction, $D$ is block diagonal with normal blocks. This proves the claim.
9. Now let $B = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ be a normal $2 \times 2$ diagonal block with no real eigenvalue. The $(1, 1)$ entries of $B B^T$ and $B^T B$ are $p^2 + q^2$ and $p^2 + r^2$. So $q^2 = r^2$.
10. Case $r = q$. Then $B$ is symmetric, so it has a real eigenvalue by [[the theorem on real eigenvalues|0C4NT4GT3X]]. This is impossible.
11. Case $r = -q$. Then $q \neq 0$, since $q = 0$ would give $r = q$. The $(1, 2)$ entries of $B B^T$ and $B^T B$ are $pr + qs = q(s - p)$ and $pq + rs = q(p - s)$. They are equal, so $2q(s - p) = 0$, and $s = p$.
12. So $B = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = p$ and $b = -q \neq 0$. If $b < 0$, let $S = \operatorname{diag}(1, -1)$. Then $S B S = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$, which has the required form with $-b > 0$.
13. Let $Q'$ be $Q$ with the second column of each such block multiplied by $-1$. Then $Q'$ is orthogonal, and $Q'^T A Q'$ is block diagonal with $1 \times 1$ blocks and blocks $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $b > 0$. This proves part 1.
14. Part 2. Take an orthonormal basis $e_1, \dots, e_n$ of $V$, by [[the existence of orthonormal bases|0Y85GYEGSF]]. Let $A$ be the matrix of $T$. By [[the matrix of the adjoint|0DBTE6HVBD]], $T^*$ has the matrix $A^T$, so $A$ is normal.
15. Part 1 gives $Q$. The vectors $f_j = \sum_i q_{ij} e_i$ form an orthonormal basis, because the columns of $Q$ are orthonormal. The matrix of $T$ in this basis is $Q^T A Q$.
16. Part 3. A [[skew-symmetric|03RNVFDEAN]] $A$ is normal, since $A A^T = -A^2 = A^T A$. The matrix $M = Q^T A Q$ is skew-symmetric too, because $M^T = Q^T A^T Q = -M$.
17. So each diagonal block of $M$ is skew-symmetric. A $1 \times 1$ block $(c)$ has $c = -c$, so $c = 0$. A block $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ has the transpose $\begin{pmatrix} a & b \\ -b & a \end{pmatrix}$, so $a = -a$ and $a = 0$.

## Idea

The real Schur form is block triangular, and the trace identity $\operatorname{tr}(B B^T) = \operatorname{tr}(B^T B)$ forces each block above the diagonal to vanish.
A normal $2 \times 2$ block without real eigenvalues must be a rotation times a scale factor.

## Variants

- One can complexify instead. A non-real eigenvalue $a + ib$ of $A$ has an eigenvector $x + iy$ in $\mathbb{C}^n$. For normal $A$, the vectors $x$ and $y$ are orthogonal and of equal length, and they span an invariant plane. Its orthogonal complement is invariant too, because $A^T$ is a polynomial in $A$ by [[the spectral decomposition|D5KVBA1K9R]].
- The $1 \times 1$ case of step 3 is the step of [[the proof of the complex spectral theorem|A5M6ZY42WR]] that compares diagonal entries of $U U^*$ and $U^* U$.
