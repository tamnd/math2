---
tag: 8XT0ZBM0BN
kind: example
name: The reflection diag(1, −1) and its projection (I + A)/2
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [NH2QE3671N]
uses: [1GVCRBXQT8, 0K7TD9BV2D, 0Q9PGXD9E4]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: Properties
---

## Example

Let $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ over $\mathbb{R}$.

1. $A$ is [[diagonal|0Q9PGXD9E4]], so $A^2 = \begin{pmatrix} 1^2 & 0 \\ 0 & (-1)^2 \end{pmatrix} = I$, and $A$ is [[involutory|1GVCRBXQT8]].
2. $A(x, y) = (x, -y)$, the reflection in the $x$-axis.
3. $P = \tfrac12 (I + A) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, and $P^2 = P$, so $P$ is [[idempotent|0K7TD9BV2D]].
4. $P$ projects onto the $x$-axis, which is the $+1$ space of $A$.
5. $\tfrac12 (I - A) = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$ projects onto the $y$-axis, the $-1$ space of $A$.
6. $A = P - (I - P) = 2P - I$, as the general correspondence predicts.

## Remarks

Over $\mathbb{F}_2$ this matrix is $I$, because $-1 = 1$ there.
So the correspondence between involutions and idempotents needs $2$ to be invertible.

## Explanations

### L1 human

The reflection in the $x$-axis keeps $x$ and changes the sign of $y$.
Half of $I + A$ keeps $x$ and kills $y$, which is a projection.

### L2 human

Every involutory matrix outside characteristic $2$ is similar to a diagonal matrix with entries $\pm 1$.
This example is the simplest case with both signs present.
