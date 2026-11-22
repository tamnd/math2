---
tag: 0QRBVFJ50X
kind: definition
name: Orthogonal matrix
msc: ["15B10"]
topics: [AZS5BPF5H3]
audience: ug1
defines: 0W02QESPJQ
uses: [0W809K6AW0, 06DW9BAWB1]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.orthogonalGroup
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: lead section
  - book: isbn:9780134860244
    locator: Section 6.5
inventory: [8KHAEVF7HH]
---

## Definition

An orthogonal matrix is a real square matrix whose transpose is its inverse from the left.
Let $n \ge 1$, and let $Q$ be a real $n \times n$ matrix.
The matrix $Q$ is *orthogonal* when
$$Q^T Q = I_n,$$
where $Q^T$ is the [[transpose|0W809K6AW0]] of $Q$ and $I_n$ is the [[identity matrix|06DW9BAWB1]].

## Notation

The set of real orthogonal $n \times n$ matrices is written $O(n)$, $O_n(\R)$ or $O(n, \R)$.
Mathlib writes `Matrix.orthogonalGroup n ℝ` for this set, as a submonoid of the matrices.
Its condition is `star A * A = 1`, and the star of a real matrix is its transpose.

## Remarks

Read the condition entry by entry.
The entry $(j, k)$ of $Q^TQ$ is row $j$ of $Q^T$ times column $k$ of $Q$, which is the dot product $q_j \cdot q_k$ of the columns $j$ and $k$ of $Q$.
So the diagonal entries of $Q^TQ = I_n$ say that each column has length $1$, and the other entries say that two different columns are perpendicular.
In short, the definition asks for orthonormal columns.

The matrix must be real and square.
A $3 \times 2$ matrix with orthonormal columns also has $Q^TQ = I_2$, but it is not invertible, so it is not called orthogonal.
Squareness is what lets the [[equivalent conditions|F7M8ZXB4P7]] give $QQ^T = I_n$, $Q^{-1} = Q^T$ and orthonormal rows as well.

For example, the coordinate swap $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ is orthogonal, because its columns $(0, 1)$ and $(1, 0)$ are orthonormal.
The matrix $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ fails the condition, since its first column has length $2$ and the entry $(1, 1)$ of $Q^TQ$ is $4$.
The word "orthogonal" is traditional, but it undersells the condition: orthogonal columns of other lengths are not enough.
The [[concept page|0W02QESPJQ]] has more examples and non-examples.

## Explanations

### L1 human

A square table of numbers is an orthogonal matrix when its columns are arrows of length $1$ and each two of them meet at a right angle.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the columns $(0, 1)$ and $(1, 0)$.
Both have length $1$, and they are perpendicular.

### L2 human

Check the definition for $Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
The transpose is $Q^T = Q$, and the product is
$$Q^TQ = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = I_2.$$
So $Q$ is orthogonal, and it is the reflection in the line $y = x$.
Watch out: $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has orthogonal columns, but $Q^TQ = \operatorname{diag}(4, 1) \ne I_2$.
