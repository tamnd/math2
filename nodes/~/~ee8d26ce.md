---
tag: ~ee8d26ce
kind: example
name: The basic Weyr matrix of structure (2, 1, 1)
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: research
instance_of: [~ee1d6eec]
uses: [~ee1d6eec, 0PBFS92AJP, 8G3X8MPG7E, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Weyr_canonical_form
    locator: Definitions
  - book: isbn:9780199793730
---

## Example

Let $W = E_{13} + E_{34} = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix}$ over a field $F$, cut into blocks of sizes $2, 1, 1$.

1. Diagonal blocks. $W_{11}$ is the $2 \times 2$ zero matrix, and $W_{22} = W_{33} = (0)$. So $W_{ii} = 0 \cdot I$.
2. Superdiagonal blocks. $W_{12}$ is the $2 \times 1$ block in rows $1, 2$ and column $3$, equal to $(1, 0)^{\mathsf T}$: the identity $I_1$ on top and one zero row below. $W_{23}$ is the entry $(3, 4)$, equal to $1 = I_1$.
3. Other blocks. $W_{13}$, the entries $(1, 4)$ and $(2, 4)$, is $0$, and all blocks below the diagonal are $0$.
4. So $W$ is a basic Weyr matrix with eigenvalue $0$ and Weyr structure $(2, 1, 1)$.
5. Powers. $W e_3 = e_1$, $W e_4 = e_3$, and $W e_1 = W e_2 = 0$. So $W^2 = E_{14}$ and $W^3 = 0$. The ranks of $W^0, W^1, W^2, W^3$ are $4, 2, 1, 0$.
6. Kernel dimensions. By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker W^j = 2, 3, 4$ for $j = 1, 2, 3$, with jumps $2, 1, 1$, which is the Weyr structure.
7. Jordan form. The chain $e_4 \mapsto e_3 \mapsto e_1 \mapsto 0$ and the eigenvector $e_2$ give $W \sim J_3(0) \oplus J_1(0)$.
8. Centralizer. Solving $XW = WX$ entry by entry gives exactly the matrices
$$X = \begin{pmatrix} a & b & c & d \\ 0 & e & 0 & f \\ 0 & 0 & a & c \\ 0 & 0 & 0 & a \end{pmatrix}, \qquad a, b, c, d, e, f \in F.$$
They are block upper triangular for the block sizes $2, 1, 1$, and they form a space of dimension $6 = 2^2 + 1^2 + 1^2$.

## Remarks

The [[commuting matrices|8G3X8MPG7E]] of the Jordan matrix $J_3(0) \oplus J_1(0)$ also form a space of dimension $6$, but it contains $E_{43}$, which lies below the diagonal.
The Weyr basis $e_1, e_4, e_2, e_3$ of $J_3(0) \oplus J_1(0)$ turns that matrix into $W$, and the centralizer becomes triangular.
The diagonal blocks of $X$ are $\begin{pmatrix} a & b \\ 0 & e \end{pmatrix}$, $(a)$ and $(a)$; each one is the upper left corner of the one before.

## Explanations

### L1 human

This $4 \times 4$ matrix has the shape that Weyr chose: zero blocks on the diagonal and identity pieces just above them.
Every matrix that commutes with it is upper triangular.

### L2 human

The blocks have sizes $2, 1, 1$, read from the jumps of the kernel dimensions $2, 3, 4$.
The centralizer has six free parameters, and none of them sits below the diagonal.
For the same nilpotent map in the Jordan basis, one parameter sits below the diagonal.
