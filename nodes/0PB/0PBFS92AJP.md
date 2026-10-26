---
tag: 0PBFS92AJP
kind: definition
name: Jordan block
msc: [15A21]
defines: 07PH4RX0X5
uses: [0CP7YY6NAG]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_matrix
    locator: Definition
---

## Definition

Let $F$ be a field, let $\lambda \in F$, and let $k \ge 1$.
The *Jordan block* $J_k(\lambda)$ is the $k \times k$ matrix with entries
$$(J_k(\lambda))_{ij} = \begin{cases} \lambda & \text{if } j = i, \\ 1 & \text{if } j = i + 1, \\ 0 & \text{otherwise}. \end{cases}$$

## Remarks

For example, $J_3(\lambda) = \begin{pmatrix} \lambda & 1 & 0 \\ 0 & \lambda & 1 \\ 0 & 0 & \lambda \end{pmatrix}$.
$J_k(\lambda) - \lambda I_k$ is nilpotent of index $k$.
Its only eigenvalue is $\lambda$, with algebraic multiplicity $k$ and geometric multiplicity $1$.
Some authors put the $1$ entries below the diagonal.

## Explanations

### L1 human

A Jordan block is the simplest matrix that is not diagonalisable, when its size is at least $2$.
It has one eigenvalue and only one line of eigenvectors.
Every complex matrix is built from such blocks, by the Jordan normal form.
