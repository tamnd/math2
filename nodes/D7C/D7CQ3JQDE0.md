---
tag: D7CQ3JQDE0
kind: example
name: Two endomorphisms of the plane that do not commute
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [5JA4CYT1TB]
uses: [0E3X2G1ZQB, 4H93XF4RVH, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
---

## Example

Two simple maps of the plane give different results when composed in the two orders, and one order even gives zero.
Let $F$ be a field and consider the [[algebra of endomorphisms|0E3X2G1ZQB]] $\End(F^2)$.
Let $P, N \colon F^2 \to F^2$ be the maps
$$P(x, y) = (x, 0), \qquad N(x, y) = (y, 0).$$
Their matrices in the standard basis are the [[matrix units|4H93XF4RVH]] $E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

1. Both maps are [[linear|0RJF668P1T]], since each coordinate of the value is a linear expression in $x$ and $y$, so $P, N \in \End(F^2)$.
2. We have $(PN)(x, y) = P(y, 0) = (y, 0)$, so $PN = N$.
3. We have $(NP)(x, y) = N(x, 0) = (0, 0)$, so $NP = 0$.
4. Since $N \ne 0$, we get $PN \ne NP$, and $\End(F^2)$ is not commutative.
5. Step 3 also gives zero divisors, since $N \ne 0$ and $P \ne 0$ but $NP = 0$.

Check: $E_{11} E_{12} = E_{12}$ and $E_{12} E_{11} = 0$, as matrix products.

## Remarks

The map $P$ is the projection onto the $x$-axis along the $y$-axis, so $P^2 = P$.
The map $N$ is nilpotent, since $N^2(x, y) = N(y, 0) = (0, 0)$.
For each $n \ge 2$, the same maps acting on the first two coordinates of $F^n$ show that $\End(F^n)$ is not commutative.
If we change the dimension to $1$, the algebra $\End(F)$ is commutative, and no such pair exists.

## Explanations

### L1 human

Project the plane onto the $x$-axis, or move the $y$-coordinate into the $x$-place.
Doing these two steps in different orders gives different results.
So composition of endomorphisms depends on the order.

### L2 human

The example shows the two ways in which $\End(V)$ differs from a field.
Its multiplication is not commutative, and a product of nonzero elements can be zero.
Watch out: from $NP = 0$ you cannot cancel to conclude that $N = 0$ or $P = 0$.
