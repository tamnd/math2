---
tag: MAP4F54GJW
kind: example
name: The orthogonal projection onto the line spanned by (1, 1)
msc: ["15A99"]
topics: [Y1ESNQ2V52, QHKTJ89V6S]
audience: ug1
instance_of: [0KCE8CG86P, 033DA1WE8Y, 0B8KZRT28M]
uses: [0K7TD9BV2D, 0RH4E3CAV9, 076JGP6R3T, 0N28QN4CYA]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_matrix
    locator: Examples
---

## Example

Let
$$P = \frac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$$
over the real numbers.
We check that $P$ is idempotent, find its image and kernel, and see that they are perpendicular.

1. First square the matrix of ones:
$$\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}^2 = \begin{pmatrix} 1 + 1 & 1 + 1 \\ 1 + 1 & 1 + 1 \end{pmatrix} = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}.$$
2. So $P^2 = \tfrac14 \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} = P$, and $P$ is [[idempotent|0K7TD9BV2D]].
3. The matrix is equal to its transpose, so it is [[symmetric|0N28QN4CYA]].
4. For a vector $(x, y)$ we get $P(x, y) = \bigl(\tfrac{x + y}{2}, \tfrac{x + y}{2}\bigr)$, a point on the line $y = x$. Every point $(t, t)$ of that line is fixed, so the image is the line spanned by $(1, 1)$.
5. Since $P(1, -1) = (0, 0)$, the kernel is the line spanned by $(1, -1)$, and $(1, 1) \cdot (1, -1) = 0$, so kernel and image are perpendicular.
6. The trace is $\tfrac12 + \tfrac12 = 1$, which equals the rank $1$.

## Remarks

The example is the case $u = \tfrac{1}{\sqrt 2} (1, 1)$ of a general rule: for a unit vector $u$, the matrix $u u^{\mathsf{T}}$ is the [[orthogonal projection|0B8KZRT28M]] onto the line spanned by $u$.
Indeed $u u^{\mathsf{T}} = \tfrac12 \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}$, and $(u u^{\mathsf{T}})^2 = u (u^{\mathsf{T}} u) u^{\mathsf{T}} = u u^{\mathsf{T}}$ because $u^{\mathsf{T}} u = 1$.

If we keep the image but tilt the kernel, the projection stops being symmetric, as in [[the oblique projection|DZXTTHGFQD]].
If we drop the factor $\tfrac12$, the matrix of ones squares to twice itself and is not idempotent.

## Explanations

### L1 human

The matrix $P$ moves each point of the plane straight to the nearest point on the diagonal line $y = x$.
For example, $(4, 0)$ goes to $(2, 2)$.
A point already on the line, such as $(2, 2)$, stays where it is, so applying $P$ twice is the same as once.

### L2 human

An idempotent matrix is an orthogonal projection exactly when it is symmetric, and then the kernel is the orthogonal complement of the image.
Check it here with $b = (4, 0)$: the projection is $Pb = (2, 2)$ and the error is $b - Pb = (2, -2)$.
The error is perpendicular to the line, since $(2, -2) \cdot (1, 1) = 0$.
This is the typical use: $Pb$ is the closest point of the line to $b$.
