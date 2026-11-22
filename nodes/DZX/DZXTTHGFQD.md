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

Let
$$P = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$$
over the real numbers.
We show that $P$ is a projection onto the $x$-axis, but not an orthogonal one.

1. Multiply row by column:
$$P^2 = \begin{pmatrix} 1 \cdot 1 + 1 \cdot 0 & 1 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix} = P,$$
so $P$ is [[idempotent|0K7TD9BV2D]].
2. For a vector, $P(x, y) = (x + y, 0)$. So the image is the $x$-axis, and $P$ fixes each point $(x, 0)$.
3. Since $P(1, -1) = (0, 0)$, the kernel is the line spanned by $(1, -1)$.
4. Each vector splits into an image part and a kernel part: $(x, y) = (x + y, 0) + (-y, y)$.
5. The complementary matrix $I - P = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix}$ has square
$$\begin{pmatrix} 0 \cdot 0 + (-1) \cdot 0 & 0 \cdot (-1) + (-1) \cdot 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 0 & 1 \end{pmatrix},$$
so $I - P$ is idempotent too; it is the projection onto the kernel along the image.
6. The kernel direction $(1, -1)$ and the image direction $(1, 0)$ have dot product $1 \ne 0$, so they are not perpendicular, and $P^{\mathsf{T}} \ne P$.
7. The trace is $1$, which equals the rank $1$.

## Remarks

The example shows that "idempotent" and "symmetric" are different conditions.
The matrix $P$ moves points onto the $x$-axis along the slanted direction $(1, -1)$, not straight down.
The orthogonal projection onto the same axis is $\operatorname{diag}(1, 0)$, a different idempotent with the same image and the kernel spanned by $(0, 1)$.

If we change the corner entry $1$ to any number $c$, the matrix $\begin{pmatrix} 1 & c \\ 0 & 0 \end{pmatrix}$ is still idempotent, with kernel spanned by $(c, -1)$.
So there is one projection onto the $x$-axis for each choice of kernel line other than the axis itself, and only $c = 0$ gives the orthogonal one.

## Explanations

### L1 human

Picture light falling on the ground at a slant, at 45 degrees.
The matrix $P$ slides each point along that slanted direction until it reaches the $x$-axis, like the shadow of a point.
Doing this twice gives the same point as doing it once, because a point on the ground casts itself as its shadow.

### L2 human

To find where $P$ sends $(2, 3)$, compute $P(2, 3) = (5, 0)$.
The difference $(2, 3) - (5, 0) = (-3, 3)$ lies on the kernel line, which is the direction of the slide.
Watch out: the difference is not perpendicular to the $x$-axis, so $(5, 0)$ is not the closest point of the axis to $(2, 3)$; the closest point is $(2, 0)$.
