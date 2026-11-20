---
tag: 28TDNCN9Z8
kind: example
name: The matrix that exchanges two coordinates is involutory
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [NH2QE3671N]
uses: [1GVCRBXQT8, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: lead section
---

## Example

Let $S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.

1. $S(x, y) = (y, x)$, so $S$ exchanges the two coordinates.
2. $S^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$, so $S$ is [[involutory|1GVCRBXQT8]].
3. $S(1, 1) = (1, 1)$ and $S(1, -1) = (-1, 1) = -(1, -1)$. So the eigenvalues are $1$ and $-1$.
4. $\tfrac12 (I + S) = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, the [[orthogonal projection onto the line y = x|MAP4F54GJW]].

## Remarks

Geometrically, $S$ is the reflection of the plane in the line $y = x$.
The same holds for every matrix that exchanges two coordinates of $F^n$ and fixes the others.

## Explanations

### L1 human

Exchanging two numbers twice puts them back in their places.
So the matrix that exchanges them is its own inverse.

### L2 human

The line $y = x$ is the $+1$ space and the line $y = -x$ is the $-1$ space.
The reflection fixes the first line and reverses the second.
