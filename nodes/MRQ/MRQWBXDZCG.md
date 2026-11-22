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

We change from the standard basis of the plane to a basis tilted by $45$ degrees.
Let $V = \mathbb{R}^2$, let $B = (e_1, e_2)$ be the standard basis, and let $B' = (b'_1, b'_2)$ with $b'_1 = (1, 1)$ and $b'_2 = (1, -1)$.

1. We write the new vectors in the old basis: $b'_1 = 1 e_1 + 1 e_2$ and $b'_2 = 1 e_1 - 1 e_2$.
   By the [[definition|0KWXYZPJKN]], these coefficients are the columns of the change of basis matrix:
   $$P = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
2. The determinant is $\det P = (1)(-1) - (1)(1) = -2 \ne 0$, so $P$ is invertible, and the formula for a $2 \times 2$ inverse gives
   $$P^{-1} = \frac{1}{-2} \begin{pmatrix} -1 & -1 \\ -1 & 1 \end{pmatrix} = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}.$$
3. Check: $P \cdot \tfrac12 P = \tfrac12 \begin{pmatrix} 1 + 1 & 1 - 1 \\ 1 - 1 & 1 + 1 \end{pmatrix} = I_2$.
4. Let $v = (5, 1)$, so $[v]_B = (5, 1)$.
   The new [[coordinates|0BMVBHTWV2]] are
   $$[v]_{B'} = P^{-1} \begin{pmatrix} 5 \\ 1 \end{pmatrix} = \frac12 \begin{pmatrix} 6 \\ 4 \end{pmatrix} = \begin{pmatrix} 3 \\ 2 \end{pmatrix}.$$
5. Check: $3 b'_1 + 2 b'_2 = (3, 3) + (2, -2) = (5, 1) = v$.

## Remarks

The matrix from $B'$ back to $B$ is $P^{-1}$, and its columns $(\tfrac12, \tfrac12)$ and $(\tfrac12, -\tfrac12)$ are the coordinates of $e_1$ and $e_2$ in $B'$.
For instance $\tfrac12(1, 1) + \tfrac12(1, -1) = (1, 0) = e_1$.

For a general vector $v = (x, y)$, the same product gives $[v]_{B'} = \bigl(\tfrac12(x + y), \tfrac12(x - y)\bigr)$.
The two new vectors are perpendicular and both have length $\sqrt 2$, so $P^{\mathsf{T}} P = 2I$ and $P^{-1} = \tfrac12 P^{\mathsf{T}}$.
If we scale them to length $1$, so that $B'$ becomes $\tfrac{1}{\sqrt 2}(1, 1)$, $\tfrac{1}{\sqrt 2}(1, -1)$, then $P$ becomes orthogonal and $P^{-1} = P^{\mathsf{T}}$.

## Explanations

### L1 human

The new basis vectors are the columns of $P$.
To find how many steps along $(1, 1)$ and along $(1, -1)$ reach the point $(5, 1)$, multiply by $P^{-1}$.
The answer is $3$ steps along the first and $2$ along the second.

### L2 human

Watch out for the direction.
Multiplying the old coordinates by $P$ instead gives $P(5, 1) = (6, 4)$, and $6 b'_1 + 4 b'_2 = (10, 2)$, which is not $v$.
The matrix $P$ takes new coordinates as input, so old coordinates must go through $P^{-1}$.
