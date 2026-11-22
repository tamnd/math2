---
tag: 1MX3PFN4BB
kind: example
name: A nilpotent map of the plane is not a projection
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
not_instance_of:
  - target: 033DA1WE8Y
    note: N(x, y) = (y, 0) satisfies N² = 0, which differs from N, and its image and kernel are both the x-axis
illustrates: [2ZX5Q7V4VN]
uses: [0RH4E3CAV9, 02YFME3RGW, 0JB228DCWB]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Properties and classification
---

## Example

Let $N \colon \R^2 \to \R^2$ be the map $N(x, y) = (y, 0)$, with matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
We check that $N$ is not a [[projection|0RH4E3CAV9]], and that the conclusion of the [[theorem on projections and decompositions|2ZX5Q7V4VN]] fails for it.

1. $N$ is linear, since it is given by a matrix.
2. Apply $N$ twice:
$$N^2(x, y) = N(y, 0) = (0, 0).$$
   So $N^2 = 0$.
3. But $N(0, 1) = (1, 0) \ne (0, 0)$, so $N \ne 0 = N^2$.
   Hence $N$ is not a projection.
4. The [[image|0JB228DCWB]] of $N$ is the set of all $(y, 0)$, which is the $x$-axis.
5. The [[kernel|02YFME3RGW]] of $N$ is the set of $(x, y)$ with $y = 0$, which is also the $x$-axis.
6. So $\operatorname{im} N \cap \ker N$ is the whole $x$-axis, not $\{0\}$, and $\operatorname{im} N + \ker N$ is the $x$-axis, not $\R^2$.
7. Hence $\R^2 \ne \operatorname{im} N \oplus \ker N$, and both conditions of a direct sum fail.

## Remarks

A projection fixes its image, and $N$ does the opposite: it sends its image to $0$.
For example, $(1, 0)$ lies in the image of $N$, and $N(1, 0) = (0, 0)$.

The eigenvalues tell the same story.
The only eigenvalue of $N$ is $0$, since its characteristic polynomial is $\lambda^2$.
A projection with eigenvalue $0$ only is the zero map, and $N$ is not zero, so $N$ cannot be a projection.

A small change of the matrix gives a projection.
The matrix $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ sends $(x, y)$ to $(x + y, 0)$, and its square is
$$\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}^2 = \begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix},$$
so it is the projection onto the $x$-axis along $\R(1, -1)$.
Adding the entry $1$ in the corner makes the map fix the $x$-axis instead of killing it.

## Explanations

### L1 human

The map $N$ takes the vertical part of a vector, lays it down flat, and forgets the horizontal part.
Applying it a second time gives zero, because a flat vector has no vertical part left.
A projection behaves the other way: applying it a second time gives the same result as the first time.

### L2 human

In finite dimension, $\dim \operatorname{im} N + \dim \ker N = \dim V$ holds for every linear map, by rank-nullity.
Here $1 + 1 = 2$, so the dimensions add up, and yet the sum of the image and the kernel is not direct.
So a dimension count alone cannot tell a projection apart from other maps.
The real test is whether the image and the kernel meet only in $0$, which for a projection follows from $P^2 = P$ and fails here.
