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

In $\R^2$ with the [[dot product|05HQYM0R4G]], let $U = \R(1, 0)$ be the $x$-axis and $L = \R(1, 1)$.

1. $U \cap L = \set{0}$: if $a(1, 0) = b(1, 1)$, then the second entries give $b = 0$, and then $a = 0$.
2. $U + L = \R^2$: every $(x, y)$ equals $(x - y)(1, 0) + y(1, 1)$.
3. By steps 1 and 2, $\R^2 = U \oplus L$ is a [[direct sum|041JTZCK9Q]], so $L$ is a [[complementary subspace|0M83V17KHX]] of $U$.
4. But $(1, 1) \cdot (1, 0) = 1 \ne 0$, so $(1, 1) \notin U^\perp$.
5. The [[orthogonal complement|079D68S3AW]] is $U^\perp = \R(0, 1)$, the $y$-axis, because $(x, y) \cdot (1, 0) = x$.

So $L$ is a complement of $U$, but it is not the orthogonal complement.

## Remarks

Every line $\R(c, 1)$ with $c \in \R$ is a complement of the $x$-axis, by the same two steps.
Only $c = 0$ gives the orthogonal complement.
So a subspace has many complements, but exactly one orthogonal complement.
The projection onto $U$ along $L$ is $(x, y) \mapsto (x - y, 0)$, with matrix $\begin{pmatrix} 1 & -1 \\ 0 & 0 \end{pmatrix}$; it is idempotent but not symmetric, so it is not an orthogonal projection.

## Explanations

### L1 human

The $x$-axis and the diagonal line together fill the plane, and they meet only at the origin.
But the diagonal line is not at a right angle to the $x$-axis.
The only line at a right angle to the $x$-axis is the $y$-axis.

### L2 human

To test whether a complement is orthogonal, take a spanning vector of each part and compute the dot product.
Here $(1, 0) \cdot (1, 1) = 1$, so the test fails.
For $(1, 0)$ and $(0, 1)$ the dot product is $0$, so the $y$-axis passes.
The trap is to read the word "complement" in "orthogonal complement" as "any complement".
