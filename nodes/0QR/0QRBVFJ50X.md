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

Let $n \ge 1$, and let $Q$ be a real $n \times n$ matrix.
The matrix $Q$ is *orthogonal* when
$$Q^T Q = I_n,$$
where $Q^T$ is the [[transpose|0W809K6AW0]] of $Q$ and $I_n$ is the [[identity matrix|06DW9BAWB1]].

## Notation

- The set of real orthogonal $n \times n$ matrices is written $O(n)$, $O_n(\R)$ or $O(n, \R)$.
- Mathlib writes `Matrix.orthogonalGroup n ℝ` for this set, as a submonoid of the matrices. Its condition is `star A * A = 1`, and the star of a real matrix is its transpose.

## Remarks

- The $(j, k)$ entry of $Q^TQ$ is the dot product of the columns $j$ and $k$ of $Q$. So the definition says that the columns of $Q$ are orthonormal.
- [[The equivalent conditions|F7M8ZXB4P7]] show that $Q^{-1} = Q^T$, that $QQ^T = I_n$, and that the rows are orthonormal too.
- The word "orthogonal" is traditional, but the columns must be orthonormal: orthogonal columns of other lengths are not enough.
- Examples and non-examples are in the node on the [[concept|0W02QESPJQ]].

## Explanations

### L1 human

A square table of numbers is an orthogonal matrix when its columns are arrows of length $1$ and each two of them meet at a right angle.
For example, $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ has the columns $(0, 1)$ and $(1, 0)$.
Both have length $1$, and they are perpendicular.

### L2 human

Worked check for $Q = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$:

1. $Q^T = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = Q$.
2. $Q^TQ = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = I_2$.
3. So $Q$ is orthogonal. It swaps the two coordinates, which is the reflection in the line $y = x$.

A trap: $\begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ has orthogonal columns, but its first column has length $2$, so it is not orthogonal.
