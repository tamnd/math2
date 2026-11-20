---
tag: 0PBFS92AJP
kind: definition
name: Jordan block
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: ug2
defines: 07PH4RX0X5
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
  - book: isbn:9780135367971
    locator: Section 7.3
---

## Definition

Let $F$ be a field, let $\lambda \in F$, and let $k \ge 1$.
The *Jordan block* $J_k(\lambda)$ is the $k \times k$ [[square matrix|0CP7YY6NAG]] with entries
$$(J_k(\lambda))_{ij} = \begin{cases} \lambda & \text{if } j = i, \\ 1 & \text{if } j = i + 1, \\ 0 & \text{otherwise}. \end{cases}$$
The number $k$ is the *size* of the block and $\lambda$ is its *eigenvalue*.

## Notation

This is the upper version, with the ones above the diagonal.
Some books use the lower version, the transpose, with the ones below the diagonal.
A direct sum $J_{k_1}(\lambda_1) \oplus \cdots \oplus J_{k_s}(\lambda_s)$ is a *Jordan matrix*.

## Remarks

- For example, $J_3(\lambda) = \begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{pmatrix}$.
- In terms of the standard basis, $J_k(\lambda) e_1 = \lambda e_1$ and $J_k(\lambda) e_i = \lambda e_i + e_{i-1}$ for $2 \le i \le k$.
- $J_k(\lambda) - \lambda I_k = J_k(0)$ is nilpotent of index $k$.
- Its only eigenvalue is $\lambda$, with algebraic multiplicity $k$ and geometric multiplicity $1$.

## Explanations

### L1 human

A Jordan block is a square matrix with one number on the whole diagonal, ones just above the diagonal, and zeros elsewhere.
When its size is at least $2$, it is the simplest matrix that is not diagonalisable.
It has one eigenvalue and only one line of eigenvectors.

### L2 human

1. $J_1(5) = (5)$.
2. $J_2(5) = \begin{pmatrix} 5 & 1 \\ 0 & 5 \end{pmatrix}$, and $J_2(5) e_2 = e_1 + 5 e_2$.
3. $J_2(5) - 5I = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has rank $1$, so the eigenspace of $5$ is the line through $e_1$.

The trap is the convention: check if the book puts the ones above or below the diagonal.
