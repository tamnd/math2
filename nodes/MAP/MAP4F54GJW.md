---
tag: MAP4F54GJW
kind: example
name: The orthogonal projection onto the line spanned by (1, 1)
msc: ["15A99"]
topics: [Y1ESNQ2V52, QHKTJ89V6S]
audience: ug1
instance_of: [0KCE8CG86P, 033DA1WE8Y]
uses: [0K7TD9BV2D, 0RH4E3CAV9, 076JGP6R3T, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Examples
---

## Example

Let $P = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$.

1. $\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}^2 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}$, so $P^2 = \tfrac14 \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = P$.
2. So $P$ is [[idempotent|0K7TD9BV2D]], and it is [[symmetric|0N28QN4CYA]].
3. $P(x, y) = \left(\tfrac{x + y}{2}, \tfrac{x + y}{2}\right)$, a point on the line $y = x$.
4. $P(1, -1) = (0, 0)$, so the kernel is the line spanned by $(1, -1)$, which is perpendicular to $(1, 1)$.
5. $\operatorname{tr} P = \tfrac12 + \tfrac12 = 1$, and the rank of $P$ is $1$.

## Remarks

In general, for a unit vector $u$, the matrix $u u^{\mathsf{T}}$ is the orthogonal projection onto the line spanned by $u$.
Here $u = \tfrac{1}{\sqrt2} (1, 1)$.

## Explanations

### L1 human

$P$ moves each point straight to the nearest point of the line $y = x$.
A point already on the line stays where it is.

### L2 human

An idempotent matrix is an orthogonal projection exactly when it is symmetric.
Then the kernel is the orthogonal complement of the image.
