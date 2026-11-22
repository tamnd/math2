---
tag: R9Z3W1CFPP
kind: statement
role: theorem
name: The Cayley transform between skew-symmetric and orthogonal matrices
aliases: [cayley-transform-theorem, cayley-parametrization-of-so-n]
msc: ["15B10", "15A16"]
topics: [AZS5BPF5H3]
audience: grad
about: [HKQ5YY027B, 6WBVP2PB1Y, 03RNVFDEAN]
uses: [03RNVFDEAN, 0QRBVFJ50X, 0EB9N0S33C, 0C3CFHDN6R, 0ZND7NQ970]
sources:
  - url: https://en.wikipedia.org/wiki/Cayley_transform
    locator: Matrix map
---

## Statement

One rational formula, used in both directions, matches the skew-symmetric matrices with the rotations that have no eigenvalue $-1$.

For a real $n \times n$ matrix $M$ with $I + M$ [[invertible|0EB9N0S33C]], let $C(M) = (I - M)(I + M)^{-1}$.

1. If $A$ is [[skew-symmetric|03RNVFDEAN]], then $I + A$ and $I - A$ are invertible.
2. If $A$ is skew-symmetric, then $Q = C(A)$ is an [[orthogonal matrix|0QRBVFJ50X]] with $\det Q = 1$, and $-1$ is not an [[eigenvalue|0ZND7NQ970]] of $Q$.
3. If $Q$ is orthogonal and $-1$ is not an eigenvalue of $Q$, then $A = C(Q)$ is skew-symmetric.
4. We have $C(C(M)) = M$ for each $M$ with $I + M$ invertible.
5. So $C$ is a bijection from the real skew-symmetric $n \times n$ matrices onto the set of $Q \in O(n)$ without the eigenvalue $-1$. This set lies in $SO(n)$, and $C$ is its own inverse.

## Remarks

### Both directions on one matrix

Take $A = \frac{1}{3}\begin{pmatrix} 0 & 1 & -1 \\ -1 & 0 & 1 \\ 1 & -1 & 0 \end{pmatrix}$, as in [[the three by three example|TEZ3YS5VTB]].
Then $\det(I + A) = \frac{4}{3}$, and
$$(I + A)^{-1} = \frac{1}{6}\begin{pmatrix} 5 & -1 & 2 \\ 2 & 5 & -1 \\ -1 & 2 & 5 \end{pmatrix}, \qquad Q = C(A) = \frac{1}{3}\begin{pmatrix} 2 & -1 & 2 \\ 2 & 2 & -1 \\ -1 & 2 & 2 \end{pmatrix}.$$
This $Q$ is the [[rotation by sixty degrees|TFWTJ9K6K7]] about the line through $(1, 1, 1)$.
For the way back,
$$I - Q = \frac{1}{3}\begin{pmatrix} 1 & 1 & -2 \\ -2 & 1 & 1 \\ 1 & -2 & 1 \end{pmatrix}, \qquad I + Q = \frac{1}{3}\begin{pmatrix} 5 & -1 & 2 \\ 2 & 5 & -1 \\ -1 & 2 & 5 \end{pmatrix} = 2(I + A)^{-1}.$$
So $(I + Q)^{-1} = \frac{1}{2}(I + A)$, and the first row of $(I - Q)(I + Q)^{-1}$ is $\frac{1}{18}(3 - 1 - 2, \ 1 + 3 + 2, \ -1 + 1 - 6) = \frac{1}{3}(0, 1, -1)$, the first row of $A$.
Check: $\tr Q = 2 = 1 + 2\cos\frac{\pi}{3}$.

### Why each hypothesis is needed

Part 3 needs that $-1$ is not an eigenvalue.
For $Q = -I_2$ the matrix $I + Q = 0$ is not invertible, and $C(Q)$ is not defined.
Part 2 needs a skew-symmetric $A$.
For $A = \operatorname{diag}(1, 0)$ the matrix $I + A$ is invertible, but $C(A) = \operatorname{diag}(0, 1)$ is not orthogonal.
Part 1 needs real entries.
Over $\C$ the matrix $A = \begin{pmatrix} 0 & i \\ -i & 0 \end{pmatrix}$ satisfies $A^{\mathsf{T}} = -A$, but $\det(I + A) = 1 + i^2 = 0$, so $I + A$ is singular.

### What it gives you

Part 5 is the rational parametrization of $SO(n)$.
Each $Q \in SO(n)$ without the eigenvalue $-1$ is given by $\frac{n(n - 1)}{2}$ free real numbers, the entries of $A$ above the diagonal.
If $A$ has rational entries, then so does $C(A)$, so rational rotations are easy to produce.
For $n = 2$ and $A = \begin{pmatrix} 0 & -t \\ t & 0 \end{pmatrix}$ we get $C(A) = R(-\theta)$ with $t = \tan\frac{\theta}{2}$, so the image is $SO(2)$ without the half turn $R(\pi)$.
The first columns $\frac{1}{1 + t^2}(1 - t^2, -2t)$ with $t \in \mathbb{Q}$ are then all rational points of the unit circle except $(-1, 0)$, and they give the [[Pythagorean triples|0M7ARED5Q7]].
No element of $O(n)$ with determinant $-1$ is in the image, because part 2 gives $\det C(A) = 1$.

### The converse

The image of $C$ is not all of $SO(n)$ for $n \ge 2$.
The rotation $\operatorname{diag}(-1, -1, 1, \dots, 1)$ lies in $SO(n)$ and has the eigenvalue $-1$, as in [[the half turn example|KFMTND2HXZ]].
Still, each $Q \in SO(n)$ is a product of two elements of the image.
By [[the normal form|QTY3VMFGY1]], $Q$ has a square root $Q_0 \in SO(n)$ whose angles are half those of $Q$, so they lie in $(0, \frac{\pi}{2}]$, and $Q_0$ has no eigenvalue $-1$.

### Generalizations

For a complex skew-Hermitian matrix $A$, with $A^* = -A$, the matrix $C(A)$ is unitary without the eigenvalue $-1$, and $C$ is again a bijection onto these unitary matrices.
For a nondegenerate symmetric bilinear form with matrix $J$, the same formula sends the matrices with $A^{\mathsf{T}}J = -JA$ to the matrices with $Q^{\mathsf{T}}JQ = J$, whenever $I + A$ is invertible.

## History

Cayley published the transform in 1846.

## Explanations

### L1 human

The recipe $(I - A)(I + A)^{-1}$ turns each skew-symmetric table of numbers into a rotation.
The same recipe, used on the rotation, gives the table back.
Only the rotations that send some direction to its opposite are missed.

### L2 human

Here is a typical use: find the skew-symmetric matrix behind the rotation $Q = \frac{1}{5}\begin{pmatrix} 3 & 4 \\ -4 & 3 \end{pmatrix}$.
First check that $-1$ is not an eigenvalue: $\det(I + Q) = \frac{1}{25}(64 + 16) = \frac{16}{5} \neq 0$.
Then $I - Q = \frac{1}{5}\begin{pmatrix} 2 & -4 \\ 4 & 2 \end{pmatrix}$ and $(I + Q)^{-1} = \frac{1}{16}\begin{pmatrix} 8 & -4 \\ 4 & 8 \end{pmatrix}$, so
$$C(Q) = \frac{1}{80}\begin{pmatrix} 0 & -40 \\ 40 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -\frac{1}{2} \\ \frac{1}{2} & 0 \end{pmatrix}.$$
This is the matrix of [[the two by two example|QFJZBPVV00]], as part 4 predicts.
Watch out: for the half turns the test fails, since $\det(I + Q) = 0$, and the formula for $C(Q)$ gives nothing.

### L3 human

The map $C$ is a birational isomorphism between the vector space $\mathfrak{so}(n)$ and the group variety $SO(n)$.
Its derivative at $0$ is $-2$ times the identity, so it is a chart of $SO(n)$ near $I$ with the tangent space $\mathfrak{so}(n)$.
The algebra of parts 2 to 4 works over any field of characteristic not $2$, whenever $I + A$ is invertible.
