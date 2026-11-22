---
tag: 8YDFZV8S5W
kind: example
name: The orthogonal projection onto a plane in R3
msc: [15A04]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0B8KZRT28M]
illustrates: [AK3JJ5HHG2, ZJRJNWJ8V1]
uses: [0Q8HZTJC7G, 0W809K6AW0, 05HQYM0R4G, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Formulas
  - book: isbn:9780321982384
    locator: Section 6.3
---

## Example

Let $U \subseteq \R^3$ be the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$, with the [[dot product|05HQYM0R4G]], and let
$$A = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}$$
have these two vectors as its columns.
The columns are independent, since neither is a multiple of the other.
We compute the matrix $P = A (A^{\mathsf{T}} A)^{-1} A^{\mathsf{T}}$ of the [[orthogonal projection|0Q8HZTJC7G]] onto $U$, given by the [[projection formulas|AK3JJ5HHG2]], and then check it.

1. The [[transpose|0W809K6AW0]] times $A$ is
$$A^{\mathsf{T}} A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \qquad \det(A^{\mathsf{T}} A) = 4 - 1 = 3,$$
so $A^{\mathsf{T}} A$ is [[invertible|0EB9N0S33C]] with $(A^{\mathsf{T}} A)^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$.
2. Multiplying on the left by $A$ gives
$$A (A^{\mathsf{T}} A)^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ 1 & 1 \\ -1 & 2 \end{pmatrix}.$$
3. Multiplying on the right by $A^{\mathsf{T}} = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ gives
$$P = \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}.$$
4. The matrix is symmetric, because the entries in places $(1, 2)$, $(1, 3)$ and $(2, 3)$ are $\frac{1}{3}$, $-\frac{1}{3}$ and $\frac{1}{3}$, and the mirror entries are the same.
5. The vector $n = (1, -1, 1)$ is orthogonal to both columns, since $1 - 1 + 0 = 0$ and $0 - 1 + 1 = 0$, so it is a normal of $U$ with $n^{\mathsf{T}} n = 3$.
6. The matrix agrees with the shortcut through the normal, because
$$I - \frac{1}{3} n n^{\mathsf{T}} = I - \frac{1}{3} \begin{pmatrix} 1 & -1 & 1 \\ -1 & 1 & -1 \\ 1 & -1 & 1 \end{pmatrix} = \frac{1}{3} \begin{pmatrix} 2 & 1 & -1 \\ 1 & 2 & 1 \\ -1 & 1 & 2 \end{pmatrix}.$$
7. The matrix is idempotent, because with $N = n n^{\mathsf{T}}$ we have $N^2 = n (n^{\mathsf{T}} n) n^{\mathsf{T}} = 3N$, and so
$$P^2 = I - \tfrac{2}{3} N + \tfrac{1}{9} \cdot 3N = I - \tfrac{1}{3} N = P.$$
8. For $v = (1, 2, 3)$ the rows of $3P$ give $2 + 2 - 3 = 1$, $1 + 4 + 3 = 8$ and $-1 + 2 + 6 = 7$, so $P v = \frac{1}{3}(1, 8, 7)$.
9. The error is $v - P v = \frac{1}{3}(2, -2, 2) = \frac{2}{3} n$, which is orthogonal to $U$, as the definition requires.
10. The trace of $P$ is $\frac{2 + 2 + 2}{3} = 2$, which is $\dim U$.

## Remarks

The example shows the matrix formula at work on a basis that is not orthogonal.
The two columns meet at an angle, since $(1, 1, 0) \cdot (0, 1, 1) = 1$, and the factor $(A^{\mathsf{T}} A)^{-1}$ corrects for that angle.
Without it, the sum of the two projections onto the lines through the columns is
$$\frac{1}{2} \begin{pmatrix} 1 & 1 & 0 \\ 1 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix} + \frac{1}{2} \begin{pmatrix} 0 & 0 & 0 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix},$$
which has entry $(2, 2)$ equal to $1$, while $P$ has $\frac{2}{3}$ there.

The distance from $v$ to the plane is the length of the error, $\norm{\frac{2}{3} n} = \frac{2}{3} \sqrt{3} = \frac{2}{\sqrt{3}}$.
The point-to-plane formula $\frac{\abs{n \cdot v}}{\norm{n}} = \frac{\abs{1 - 2 + 3}}{\sqrt{3}}$ from [[distances between points, lines and planes|C6GAS92QHX]] gives the same value.
If we replace the two columns by any other basis of the same plane, $P$ does not change, because the projection depends only on $U$.

## Explanations

### L1 human

The projection onto a plane removes the part of a vector that sticks out of the plane.
For $(1, 2, 3)$, the part that sticks out is $\frac{2}{3}$ of the normal direction $(1, -1, 1)$.
What is left, $\frac{1}{3}(1, 8, 7)$, lies flat in the plane.

### L2 human

The matrix formula works in every dimension, but in $\R^3$ the complement of a plane is a line, so $P = I - \frac{n n^{\mathsf{T}}}{n^{\mathsf{T}} n}$ is faster.
That shortcut needs a normal, and step 5 finds one by solving two dot-product equations.
Watch out for a common slip: using $A A^{\mathsf{T}}$ without the inverse factor.
Here
$$A A^{\mathsf{T}} = \begin{pmatrix} 1 & 1 & 0 \\ 1 & 2 & 1 \\ 0 & 1 & 1 \end{pmatrix}$$
has entry $(2, 2)$ equal to $2$, and its square has entry $(1, 1)$ equal to $1 + 1 + 0 = 2$ instead of $1$, so it is not idempotent and not a projection.
