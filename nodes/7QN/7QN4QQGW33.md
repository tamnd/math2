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

We start from the real Schur form, show that normality removes every block above the diagonal, and then find the shape of each $2 \times 2$ block.

1. The real Schur form. Let $A$ be real and normal. By the real form of the [[Schur decomposition|V1JG4C7R7B]], $A = Q M Q^{\mathsf{T}}$ with $Q$ real [[orthogonal|0QRBVFJ50X]] and $M$ block upper triangular, where each diagonal block is $1 \times 1$ or a $2 \times 2$ block with no real eigenvalue.
2. $M$ is [[normal|0XYKE8BE7X]]. From $Q^{\mathsf{T}} Q = I$ we get
$$M M^{\mathsf{T}} = Q^{\mathsf{T}} A Q Q^{\mathsf{T}} A^{\mathsf{T}} Q = Q^{\mathsf{T}} A A^{\mathsf{T}} Q, \qquad M^{\mathsf{T}} M = Q^{\mathsf{T}} A^{\mathsf{T}} A Q,$$
and the two agree because $A A^{\mathsf{T}} = A^{\mathsf{T}} A$.
3. The claim. A normal block upper triangular matrix is block diagonal, and its diagonal blocks are normal. We prove this by induction on the number of diagonal blocks; with one block there is nothing to prove.
4. Splitting off the first block. With more blocks, write $M = \begin{pmatrix} B & C \\ 0 & D \end{pmatrix}$, where $B$ is the first diagonal block and $D$ is block upper triangular with one block fewer.
5. Comparing corners. The upper left block of $M M^{\mathsf{T}}$ is $B B^{\mathsf{T}} + C C^{\mathsf{T}}$, and the upper left block of $M^{\mathsf{T}} M$ is $B^{\mathsf{T}} B$. By step 2 they are equal.
6. Taking traces. By the [[cyclic property of the trace|0Y4NF1DRKD]], $\operatorname{tr}(B B^{\mathsf{T}}) = \operatorname{tr}(B^{\mathsf{T}} B)$, so step 5 gives $\operatorname{tr}(C C^{\mathsf{T}}) = 0$.
7. The block $C$ vanishes. The trace $\operatorname{tr}(C C^{\mathsf{T}})$ is the sum of the squares of all entries of $C$. A sum of real squares is $0$ only when each square is $0$, so $C = 0$.
8. Induction. Now $M M^{\mathsf{T}}$ and $M^{\mathsf{T}} M$ are block diagonal with the blocks $B B^{\mathsf{T}}, D D^{\mathsf{T}}$ and $B^{\mathsf{T}} B, D^{\mathsf{T}} D$. So $B$ and $D$ are normal, and by induction $D$ is block diagonal with normal blocks. This proves the claim.
9. The shape of a $2 \times 2$ block. Let $B = \begin{pmatrix} p & q \\ r & s \end{pmatrix}$ be a normal diagonal block with no real eigenvalue. The $(1, 1)$ entries of $B B^{\mathsf{T}}$ and $B^{\mathsf{T}} B$ are $p^2 + q^2$ and $p^2 + r^2$, so $q^2 = r^2$.
10. The case $r = q$ is impossible. Then $B$ is symmetric, so it has a real eigenvalue by the [[theorem on real eigenvalues|0C4NT4GT3X]], against the choice of $B$.
11. The case $r = -q$. Then $q \neq 0$, since $q = 0$ would give $r = q$. The $(1, 2)$ entries of $B B^{\mathsf{T}}$ and $B^{\mathsf{T}} B$ are
$$pr + qs = q(s - p), \qquad pq + rs = q(p - s).$$
They are equal, so $2q(s - p) = 0$, and $s = p$ because $q \neq 0$.
12. So $B = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = p$ and $b = -q \neq 0$. If $b < 0$, let $S = \operatorname{diag}(1, -1)$; then $S B S = \begin{pmatrix} a & b \\ -b & a \end{pmatrix}$, which has the required form with $-b > 0$ in place of $b$.
13. Fixing the signs. Let $Q'$ be $Q$ with the second column of each block with $b < 0$ multiplied by $-1$. Then $Q'$ is still orthogonal, and $Q'^{\mathsf{T}} A Q'$ is block diagonal with $1 \times 1$ blocks and blocks $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $b > 0$. This proves part 1.
14. Part 2. Choose an orthonormal basis $e_1, \dots, e_n$ of $V$, which [[exists|0Y85GYEGSF]], and let $A$ be the matrix of $T$. By the [[matrix of the adjoint|0DBTE6HVBD]], $T^*$ has the matrix $A^{\mathsf{T}}$, so $A$ is normal. Part 1 gives $Q$, and the vectors $f_j = \sum_i q_{ij} e_i$ form an orthonormal basis, because the columns of $Q$ are orthonormal. The matrix of $T$ in this basis is $Q^{\mathsf{T}} A Q$.
15. Part 3. A [[skew-symmetric|03RNVFDEAN]] $A$ is normal, since $A A^{\mathsf{T}} = -A^2 = A^{\mathsf{T}} A$. Then $M = Q^{\mathsf{T}} A Q$ is skew-symmetric too, because $M^{\mathsf{T}} = Q^{\mathsf{T}} A^{\mathsf{T}} Q = -M$, so each diagonal block is skew-symmetric. A block $(c)$ has $c = -c$, so $c = 0$, and a block $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ has the transpose $\begin{pmatrix} a & b \\ -b & a \end{pmatrix}$, so $a = -a$ and $a = 0$.

## Idea

The real Schur form already has the right diagonal blocks, so the only task is to remove the blocks above the diagonal.
Normality says that $M M^{\mathsf{T}}$ and $M^{\mathsf{T}} M$ agree, and comparing their upper left corners by the trace shows that the entries above the first block have squares that add up to $0$.
Peeling off one block at a time clears the whole upper part.
Finally, a $2 \times 2$ normal block without real eigenvalues has only one possible shape: a rotation times a scale factor.

## Variants

One can complexify instead of using the real Schur form.
A non-real eigenvalue $a + ib$ of $A$ has an eigenvector $x + iy$ in $\mathbb{C}^n$.
For normal $A$, the real vectors $x$ and $y$ are orthogonal and of equal length, and they span a plane that $A$ maps to itself.
The orthogonal complement of that plane is invariant too, because $A^{\mathsf{T}}$ is a polynomial in $A$ by the [[spectral decomposition|D5KVBA1K9R]], and induction on the dimension finishes the proof.

The $1 \times 1$ case of step 3 is the same argument as in the [[proof of the complex spectral theorem from the Schur decomposition|A5M6ZY42WR]], where a normal upper triangular matrix is shown to be diagonal.
