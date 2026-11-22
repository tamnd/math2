---
tag: 0KWXYZPJKN
kind: definition
name: Change of basis matrix
msc: ["15A03", "15A04"]
topics: [S6559D61BP]
audience: ug1
defines: 0MKRHZB3WS
uses: [0VTQTPQGAV, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
---

## Definition

The change of basis matrix records the vectors of a new basis in the coordinates of an old basis.
Let $F$ be a field and let $V$ be a vector space over $F$ with two [[bases|0VTQTPQGAV]] $B = (b_1, \dots, b_n)$ and $B' = (b'_1, \dots, b'_n)$.
The *change of basis matrix* from $B$ to $B'$ is the $n \times n$ matrix $P = (p_{ij})$ over $F$ defined by
$$b'_j = \sum_{i=1}^{n} p_{ij}\, b_i \qquad (1 \le j \le n).$$
Equivalently, column $j$ of $P$ is the [[coordinate vector|0BMVBHTWV2]] $[b'_j]_B$.

## Notation

We write $P$, $P_{B \to B'}$ or $[\mathrm{id}_V]_{B, B'}$, the last because $P$ is the matrix of the identity map with $B'$ in the domain and $B$ in the target.
In Mathlib, `Basis.toMatrix e v` has as column $j$ the coordinates of $v_j$ in the basis $e$, so it is $P$ for $B = e$ and $B' = v$.
Lay writes $P_{C \leftarrow B}$ for the matrix with columns $[b_j]_C$, which is the matrix from $C$ to $B$ in our convention.

## Remarks

Each condition has a job.
Both families must be bases: the old basis $B$ makes the coefficients $p_{ij}$ exist and unique, and the new basis $B'$ makes $P$ invertible.
Both bases must be ordered, because the order of $B'$ fixes the order of the columns and the order of $B$ fixes the order of the rows.
The two bases have the same length $n = \dim V$, so $P$ is square.

The defining property in use is $[v]_B = P[v]_{B'}$ for each $v \in V$, so $P$ turns new coordinates into old ones.
Its inverse $P^{-1}$ is the change of basis matrix from $B'$ to $B$, and it turns old coordinates into new ones.
For example, the basis $(1, 1)$, $(1, -1)$ of $\mathbb{R}^2$ gives $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$, as the [[example of the plane|MRQWBXDZCG]] works out.
The family $(1, 2)$, $(2, 4)$ is not a basis, so the matrix with these columns is [[not a change of basis matrix|EX8DT1BY8G]].

Watch out: some authors call $P^{-1}$ the change of basis matrix from $B$ to $B'$.
Before you use a formula from a book, check which coordinates its matrix takes as input.
The [[concept page|0MKRHZB3WS]] compares the conventions.

## Explanations

### L1 human

The change of basis matrix lists the new basis vectors, each written in the old coordinates, as its columns.
It translates new coordinates into old coordinates, and its inverse translates back.

### L2 human

For $V = \mathbb{R}^2$, the standard basis $B$ and $B' = ((1, 1), (1, -1))$, the matrix is $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
The new coordinates $(3, 2)$ give the old coordinates
$$P \begin{pmatrix} 3 \\ 2 \end{pmatrix} = \begin{pmatrix} 3 + 2 \\ 3 - 2 \end{pmatrix} = \begin{pmatrix} 5 \\ 1 \end{pmatrix}.$$
Check: $3(1, 1) + 2(1, -1) = (5, 1)$.
