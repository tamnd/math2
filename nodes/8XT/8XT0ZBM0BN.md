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

Let
$$A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
over $\mathbb{R}$.
We check that $A$ is involutory and compute the two projections that it comes from.

1. The matrix $A$ is [[diagonal|0Q9PGXD9E4]], so we square it entry by entry:
$$A^2 = \begin{pmatrix} 1^2 & 0 \\ 0 & (-1)^2 \end{pmatrix} = I,$$
and $A$ is [[involutory|1GVCRBXQT8]].
2. For a vector, $A(x, y) = (x, -y)$, which is the reflection in the $x$-axis.
3. Half of $I + A$ is
$$P = \tfrac12 (I + A) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix},$$
and $P^2 = \operatorname{diag}(1^2, 0^2) = P$, so $P$ is [[idempotent|0K7TD9BV2D]].
4. The projection $P$ maps onto the $x$-axis, which is the $+1$ space of $A$.
5. The complementary matrix $I - P = \tfrac12 (I - A) = \operatorname{diag}(0, 1)$ maps onto the $y$-axis, which is the $-1$ space of $A$.
6. We recover $A$ as $P - (I - P) = 2P - I = \operatorname{diag}(2 - 1, 0 - 1) = A$, as the general correspondence predicts.

## Remarks

The example is the model case: outside characteristic $2$, every involutory matrix is similar to a diagonal matrix with entries $\pm 1$.
In size $2$, the only other diagonal cases are $I$ and $-I$, for which one of the two projections is $0$.

Over $\mathbb{F}_2$ this matrix is $I$, because $-1 = 1$ there.
Also $\tfrac12$ does not exist in $\mathbb{F}_2$, so the step from $A$ to $P$ breaks down.
The correspondence between involutions and idempotents needs $2$ to be invertible.

## Explanations

### L1 human

The reflection in the $x$-axis keeps $x$ and changes the sign of $y$, like a mirror lying on the axis.
For example, $(3, 2)$ goes to $(3, -2)$.
Half of $I + A$ keeps $x$ and erases $y$, so it sends $(3, 2)$ to $(3, 0)$, which is a projection.

### L2 human

Every vector splits into its part on the $x$-axis and its part on the $y$-axis, for example $(3, 2) = (3, 0) + (0, 2)$.
The projection $P$ keeps the first part, $I - P$ keeps the second, and $A$ keeps the first and reverses the second.
So $A(3, 2) = (3, 0) - (0, 2) = (3, -2)$.
