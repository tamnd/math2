---
tag: DVP2D04EZD
kind: example
name: Two complements of a plane in R³
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0M83V17KHX]
illustrates: [0P9T8WHNMH]
uses: [04C3BAHV03, 0VTQTPQGAV, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Complemented_subspace
    locator: Algebraic direct sum
  - book: isbn:9780134860244
    locator: Section 1.6
---

## Example

Let $U = \{(x, y, z) \in \R^3 : x + y + z = 0\}$, a plane through $0$.
We build a [[complement|04C3BAHV03]] of $U$ by extending a basis, as in the [[existence theorem|0P9T8WHNMH]], and then we check a second complement.

1. The vectors $u_1 = (1, -1, 0)$ and $u_2 = (0, 1, -1)$ satisfy $x + y + z = 0$, so they lie in $U$.
   They are independent, since neither is a multiple of the other.
   The plane $U$ has dimension $2$, so $u_1, u_2$ is a basis of $U$.
2. We add $e_1 = (1, 0, 0)$ and compute the determinant of the matrix with columns $u_1, u_2, e_1$:
$$\det \begin{pmatrix} 1 & 0 & 1 \\ -1 & 1 & 0 \\ 0 & -1 & 0 \end{pmatrix} = 1 \cdot \det \begin{pmatrix} -1 & 1 \\ 0 & -1 \end{pmatrix} = 1 \cdot 1 = 1,$$
   expanding along the third column, whose only nonzero entry is in the first row.
   The determinant is not $0$, so $u_1, u_2, e_1$ is a [[basis|0VTQTPQGAV]] of $\R^3$.
3. Let $W = \R e_1$, the $x$-axis.
   By the basis extension recipe, $\R^3 = U \oplus W$.
4. Check of the [[intersection|0V33SPH7RR]]: the vector $t e_1 = (t, 0, 0)$ has entry sum $t$, so it lies in $U$ only when $t = 0$.
5. Check of the sum: every vector splits as
$$(x, y, z) = (x + y + z) e_1 + (-y - z, y, z),$$
   and the second vector lies in $U$ because $(-y - z) + y + z = 0$.

A second complement is the line $W' = \R(1, 1, 1)$.

6. The vector $t(1, 1, 1)$ has entry sum $3t$, so it lies in $U$ only when $t = 0$, and $U \cap W' = \{0\}$.
7. With $m = (x + y + z)/3$, every vector splits as
$$(x, y, z) = m(1, 1, 1) + (x - m, y - m, z - m),$$
   and the second vector lies in $U$ because its entry sum is $x + y + z - 3m = 0$.

## Remarks

The two complements split the same vector in different ways.
For $v = (3, 0, 0)$, the complement $W$ gives $v = 3 e_1 + 0$, so $v$ lies in $W$ and its $U$-part is $0$.
The complement $W'$ gives $m = 1$ and $v = (1, 1, 1) + (2, -1, -1)$, so its $U$-part is $(2, -1, -1)$.

Both complements are lines, as the formula $\dim W = \dim \R^3 - \dim U = 3 - 2 = 1$ requires.
The line $W'$ is the [[orthogonal complement|0XJXTBCB2T]] of $U$ for the standard inner product, since $(1, 1, 1) \cdot (x, y, z) = x + y + z$.
The line $W$ is not, since $e_1 \cdot u_1 = 1 \ne 0$.

If we add $e_3 = (0, 0, 1)$ in step 2 instead of $e_1$, we get the $z$-axis as a third complement.
A plane through $0$ never works in place of $W$, because two planes through $0$ in $\R^3$ always share a line.

## Explanations

### L1 human

Any line through the origin that does not lie in the plane is a complement of the plane.
The $x$-axis is one such line, and the line through $(1, 1, 1)$, which stands straight up from the plane, is another.
Each one gives its own way to split a vector into a part in the plane and a part on the line.

### L2 human

Step 2 is the heart of the recipe.
Any vector outside $U$ would do in place of $e_1$, because a vector outside a plane through $0$ always completes a basis of that plane to a basis of $\R^3$.
So the choice of the added vector is exactly the choice of a complement.
The typical use is in a proof: choose a complement once, and then every vector has a definite part in $U$.
The trap is to think that the result depends only on $U$; the vector $(3, 0, 0)$ above has $U$-part $0$ for one complement and $(2, -1, -1)$ for the other.
