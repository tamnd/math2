---
tag: 0MPAJRB23T
kind: statement
role: theorem
name: Diagonalisable iff the minimal polynomial has distinct roots
msc: [15A20]
uses: [0Y17PEKF24, 0V58FPM3EQ]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonalizable_matrix
    locator: Characterization
---

## Statement

Let $F$ be a field and let $A$ be an $n \times n$ matrix over $F$ with [[minimal polynomial|03NDVCSHSB]] $m_A$.
Then $A$ is [[diagonalisable|07SQCNV233]] over $F$ if and only if
$$m_A(t) = (t - \lambda_1)(t - \lambda_2) \cdots (t - \lambda_k)$$
for some pairwise distinct $\lambda_1, \dots, \lambda_k \in F$.

## Remarks

In words: $m_A$ splits over $F$ and has no repeated roots.
If $A^2 = A$, then $m_A$ divides $t^2 - t = t(t - 1)$, so each [[projection|033DA1WE8Y]] matrix is diagonalisable.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ has $m_A = (t - 1)^2$, so it is not diagonalisable.

## Explanations

### L1 human

The minimal polynomial decides whether a matrix is diagonalisable.
The matrix is diagonalisable exactly when this polynomial is a product of distinct linear factors.
A repeated factor, like $(t - 1)^2$, signals a Jordan block of size at least $2$.
