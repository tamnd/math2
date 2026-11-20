---
tag: MRQWBXDZCG
kind: example
name: Change of basis to the basis (1, 1), (1, −1) of the plane
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0MKRHZB3WS]
uses: [0KWXYZPJKN, 0BMVBHTWV2]
sources:
  - url: https://en.wikipedia.org/wiki/Change_of_basis
    locator: Change-of-basis formula
---

## Example

Let $V = \R^2$, let $B = (e_1, e_2)$ be the standard basis, and let $B' = (b'_1, b'_2)$ with $b'_1 = (1, 1)$ and $b'_2 = (1, -1)$.

1. $b'_1 = 1 e_1 + 1 e_2$ and $b'_2 = 1 e_1 - 1 e_2$. By the [[definition|0KWXYZPJKN]], the change of basis matrix from $B$ to $B'$ is $P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
2. $\det P = -1 - 1 = -2 \ne 0$, so $P$ is invertible, and $P^{-1} = \tfrac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$.
3. Check: $P \cdot \tfrac{1}{2} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} = \tfrac{1}{2} \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = I_2$.
4. Let $v = (5, 1)$, so $[v]_B = (5, 1)$. The new [[coordinates|0BMVBHTWV2]] are $[v]_{B'} = P^{-1}(5, 1) = \tfrac{1}{2}(6, 4) = (3, 2)$.
5. Check: $3 b'_1 + 2 b'_2 = (3, 3) + (2, -2) = (5, 1) = v$.
6. Check the other direction: $P(3, 2) = (3 + 2, 3 - 2) = (5, 1)$.

## Remarks

- The matrix from $B'$ to $B$ is $P^{-1}$, whose columns $(\tfrac12, \tfrac12)$ and $(\tfrac12, -\tfrac12)$ are the coordinates of $e_1$ and $e_2$ in $B'$.
- Indeed $e_1 = \tfrac12 b'_1 + \tfrac12 b'_2$, since $\tfrac12(1, 1) + \tfrac12(1, -1) = (1, 0)$.

## Explanations

### L1 human

The new basis vectors are the columns of $P$.
To find the new coordinates of a vector, multiply by $P^{-1}$.

### L2 human

Here $P$ is a multiple of an orthogonal matrix, so $P^{-1} = \tfrac12 P^\top$.
The new coordinates are $\tfrac12(x + y, x - y)$ for $v = (x, y)$.
