---
tag: DZXTTHGFQD
kind: example
name: An oblique projection of the plane onto a line
msc: ["15A99"]
topics: [Y1ESNQ2V52, QHKTJ89V6S]
audience: ug1
instance_of: [0KCE8CG86P, 033DA1WE8Y]
not_instance_of:
  - target: 0B8KZRT28M
    note: P is idempotent but not symmetric; its kernel R(1, -1) is not orthogonal to its image, the x-axis
uses: [0K7TD9BV2D, 0RH4E3CAV9, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Examples
---

## Example

Let $P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$.

1. $P^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = P$, so $P$ is [[idempotent|0K7TD9BV2D]].
2. $P(x, y) = (x + y, 0)$, so the image of $P$ is the $x$-axis, and $P$ fixes each point $(x, 0)$.
3. $P(1, -1) = (0, 0)$, so the kernel is the line spanned by $(1, -1)$.
4. Each $(x, y)$ is $(x + y, 0) + (-y, y)$, a point of the image plus a point of the kernel.
5. $I - P = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix}$, and $(I - P)^2 = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix}$, so $I - P$ is idempotent too.
6. $\operatorname{tr} P = 1$, and the rank of $P$ is $1$.

## Remarks

$P$ is not symmetric, and the kernel is not perpendicular to the image.
So $P$ projects onto the $x$-axis along the direction $(1, -1)$, not straight down.

## Explanations

### L1 human

$P$ slides each point along a slanted line until it reaches the $x$-axis.
Doing this twice gives the same point as doing it once.

### L2 human

An idempotent matrix is fixed by its image and its kernel, and here they are two lines that are not perpendicular.
The orthogonal projection onto the $x$-axis is $\operatorname{diag}(1, 0)$, a different idempotent with the same image.
