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

Let
$$S = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$
over the real numbers.
We show that $S$ undoes itself and find the line it fixes and the line it reverses.

1. For a vector, $S(x, y) = (y, x)$, so $S$ exchanges the two coordinates.
2. Multiply row by column:
$$S^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot 1 + 1 \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},$$
so $S$ is [[involutory|1GVCRBXQT8]].
3. Since $S(1, 1) = (1, 1)$, the line $y = x$ is fixed, with eigenvalue $1$.
4. Since $S(1, -1) = (-1, 1) = -(1, -1)$, the line $y = -x$ is reversed, with eigenvalue $-1$.
5. Half of $I + S$ is
$$\tfrac12 (I + S) = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix},$$
which is the [[orthogonal projection onto the line y = x|MAP4F54GJW]].

## Remarks

Geometrically, $S$ is the reflection of the plane in the line $y = x$.
The two lines from steps 3 and 4 are perpendicular, and $S$ is symmetric, so this reflection is orthogonal.

The same holds in any size: the matrix that exchanges coordinates $i$ and $j$ of $F^n$ and fixes the others squares to $I$.
A permutation matrix of a longer cycle is not involutory, however.
For the $3$-cycle $(x, y, z) \mapsto (z, x, y)$, applying it twice gives $(y, z, x)$, which is not the starting vector.

## Explanations

### L1 human

Exchanging two numbers twice puts them back in their places.
For example, $(3, 5)$ becomes $(5, 3)$ and then $(3, 5)$ again.
So the matrix that exchanges them is its own inverse.

### L2 human

The line $y = x$ is the $+1$ space of $S$ and the line $y = -x$ is its $-1$ space.
Every vector splits along these lines, for example $(3, 1) = (2, 2) + (1, -1)$.
Then $S(3, 1) = (2, 2) - (1, -1) = (1, 3)$, which agrees with exchanging the coordinates.
