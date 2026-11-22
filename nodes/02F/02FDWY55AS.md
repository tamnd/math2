---
tag: 02FDWY55AS
kind: statement
role: proposition
name: Rank of a product of matrices
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 076JGP6R3T]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.rank_mul_le
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 3.2
---

## Statement

Multiplying matrices can lose rank but can never create it.
Let $F$ be a field, let $A$ be an $m \times n$ matrix over $F$, and let $B$ be an $n \times p$ matrix over $F$.
Then
$$\rank(AB) \le \min(\rank A, \rank B),$$
where $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]] and $AB$ is the [[matrix product|076JGP6R3T]].

## Remarks

### A first check

Take
$$A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}, \qquad B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad AB = \begin{pmatrix} 1 & 3 \\ 2 & 6 \end{pmatrix}.$$
Here $\rank A = 1$ and $\rank B = 2$, and the columns of $AB$ are $(1, 2)$ and $3(1, 2)$, so $\rank(AB) = 1$.
The bound $\min(1, 2) = 1$ is reached, because $B$ is invertible.
The [[proof|YXXTBTMPY5]] explains why: each column of $AB$ is a combination of the columns of $A$.

### When the inequality is strict

The bound can be far from the truth.
For
$$A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix},$$
both factors have rank $1$, but $AB = 0$ has rank $0$.
The image of $B$ is the second axis, and $A$ kills that axis.
So the rank of a product depends on how the image of $B$ meets the null space of $A$, and [[Sylvester's rank inequality|GS8WE1ZYV9]] measures exactly this.

### What it gives you

If $A$ is invertible, then $\rank(AB) = \rank B$, since $B = A^{-1}(AB)$ gives the reverse bound $\rank B \le \rank(AB)$.
In the same way, $\rank(AB) = \rank A$ when $B$ is invertible.
So [[similar matrices|0E89HQATM8]] and [[equivalent matrices|0CMHSGTWXB]] have the same rank, and row operations, which multiply by invertible matrices on the left, never change the rank.
A product of $n \times n$ matrices is invertible only if every factor has rank $n$, because a factor of smaller rank pulls the rank of the product below $n$.

### The other rank inequalities

The upper bound has several companions, and the sub-area proves each of them.
[[Sylvester's rank inequality|GS8WE1ZYV9]] gives the lower bound $\rank A + \rank B - n \le \rank(AB)$, and the Frobenius inequality on the same page compares products of three matrices.
For sums, [[subadditivity|5M6SX7JN01]] gives $\rank(A + B) \le \rank A + \rank B$.
Over $\mathbb{R}$ there is an equality, $\rank(A^{\mathsf{T}} A) = \rank A$, by the [[theorem on the transpose times a matrix|FGPT52R1ZE]], and the [[complex counterexample|AX5JTDETRA]] shows that it needs the real numbers.

### Generalizations

For linear maps $S \colon U \to V$ and $T \colon V \to W$ with $V$ finite-dimensional, $\rank(T \circ S) \le \min(\rank T, \rank S)$.
The image of $T \circ S$ lies in the image of $T$, which gives the first bound.
It is also the image of the subspace $\operatorname{im} S$ under $T$, and a linear map does not raise dimension, which gives the second bound.

## Explanations

### L1 human

A matrix can squash space, but it cannot unsquash it.
If $B$ flattens the plane onto a line, then no matrix $A$ applied afterwards can bring back the lost direction.
So the product $AB$ has rank at most the rank of $B$, and in the same way at most the rank of $A$.
For example, a rank $1$ matrix times anything has rank $0$ or $1$.

### L2 human

Here is a typical use: show that $A = uv^{\mathsf{T}} + wz^{\mathsf{T}}$, for vectors $u, w \in \mathbb{R}^5$ and $v, z \in \mathbb{R}^5$, is not invertible.
Write it as a product:
$$A = \begin{pmatrix} u & w \end{pmatrix} \begin{pmatrix} v^{\mathsf{T}} \\ z^{\mathsf{T}} \end{pmatrix},$$
a $5 \times 2$ matrix times a $2 \times 5$ matrix.
Each factor has rank at most $2$, so $\rank A \le 2 < 5$, and $A$ is singular.
The same argument shows that a product $CR$ with an inner size $k$ has rank at most $k$, which is the idea behind the [[rank factorization|5JGAG62VN8]].
Watch out: the inequality gives no lower bound, and a product of two nonzero matrices can be zero.

### L3 human

The two bounds come from two different inclusions.
The column space of $AB$ lies inside the column space of $A$, and the row space of $AB$ lies inside the row space of $B$.
For linear maps, this is the statement that the image of a composite lies in the image of the last map, while its dimension is at most the dimension of the image of the first map.
In Mathlib the statement is `Matrix.rank_mul_le`.
