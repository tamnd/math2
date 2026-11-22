---
tag: NFHJSAH156
kind: example
name: A complementary subspace that is not the orthogonal complement
msc: [15A63, 15A03]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0M83V17KHX]
not_instance_of:
  - target: 0XJXTBCB2T
    note: the line spanned by (1, 1) is a complement of the x-axis in R2, but (1, 1) · (1, 0) = 1 is not 0, so it is not the orthogonal complement
uses: [079D68S3AW, 041JTZCK9Q, 05HQYM0R4G]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: lead section
---

## Example

In $\R^2$ with the [[dot product|05HQYM0R4G]], let $U = \R(1, 0)$ be the $x$-axis and let $L = \R(1, 1)$ be the diagonal line.
We show that $L$ is a complement of $U$ in the sense of direct sums, but not the orthogonal complement.

1. The lines meet only in $0$. If $a(1, 0) = b(1, 1)$, then the second entries give $b = 0$, and then the first entries give $a = 0$.
2. The lines span the plane. Every vector $(x, y)$ equals $(x - y)(1, 0) + y(1, 1)$, so $U + L = \R^2$.
3. By steps 1 and 2, $\R^2 = U \oplus L$ is a [[direct sum|041JTZCK9Q]], so $L$ is a [[complementary subspace|0M83V17KHX]] of $U$.
4. The dot product $(1, 1) \cdot (1, 0) = 1$ is not $0$, so $(1, 1) \notin U^\perp$.
5. The [[orthogonal complement|079D68S3AW]] of $U$ is the $y$-axis $\R(0, 1)$, because $(x, y) \cdot (1, 0) = x$ is zero exactly when $x = 0$.

So $L$ is a complement of $U$, but $L \ne U^\perp$.

## Remarks

The example shows that "complement" and "orthogonal complement" are different words.
The same two steps show that every line $\R(c, 1)$ with $c \in \R$ is a complement of the $x$-axis, and only $c = 0$ gives the orthogonal one.
So a subspace has infinitely many complements, but exactly one orthogonal complement.

The difference shows up in projections too.
The projection onto $U$ along $L$ sends $(x, y)$ to $(x - y, 0)$, by step 2, so its matrix is
$$P = \begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}.$$
It satisfies $P^2 = P$, but $P^{\mathsf{T}} \ne P$, so it is not an [[orthogonal projection|0B8KZRT28M]].
The projection along the $y$-axis has the symmetric matrix $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$.

## Explanations

### L1 human

The $x$-axis and the diagonal line together fill the plane, and they meet only at the origin.
But the diagonal is not at a right angle to the $x$-axis.
The only line through the origin at a right angle to the $x$-axis is the $y$-axis.

### L2 human

To test whether a complement is orthogonal, take one spanning vector of each part and compute the dot product.
For $(1, 0)$ and $(1, 1)$ it is $1$, so the test fails, while for $(1, 0)$ and $(0, 1)$ it is $0$, so the $y$-axis passes.
Watch out: the shadow of $(0, 1)$ on the $x$-axis along $L$ is $(-1, 0)$, by the formula $(x - y, 0)$.
The orthogonal shadow is $(0, 0)$, so the two projections give different answers for the same vector.
