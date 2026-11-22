---
tag: VM9N7J68FW
kind: example
name: The orthogonal projection onto a line in R3
msc: [15A04]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0B8KZRT28M]
illustrates: [AK3JJ5HHG2, ZJRJNWJ8V1]
uses: [0Q8HZTJC7G, 0W809K6AW0, 05HQYM0R4G]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Formulas
  - book: isbn:9780321982384
    locator: Section 6.3
---

## Example

Let $a = (1, 2, 2)$ in $\R^3$ with the [[dot product|05HQYM0R4G]], and let $U = \R a$ be the line through $a$.
We compute the matrix $P$ of the [[orthogonal projection|0Q8HZTJC7G]] onto $U$, apply it to one vector, and check the result.

1. By the [[projection formulas|AK3JJ5HHG2]] with $A = a$ as a $3 \times 1$ matrix, whose one column is independent because $a \ne 0$, we have $P = a (a^{\mathsf{T}} a)^{-1} a^{\mathsf{T}}$.
2. The middle factor is the number $a^{\mathsf{T}} a = 1 + 4 + 4 = 9$, so
$$P = \frac{1}{9} a a^{\mathsf{T}} = \frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}.$$
3. Entry $(i, j)$ of $P$ is $\frac{a_i a_j}{9}$, which equals entry $(j, i)$, so $P^{\mathsf{T}} = P$.
4. Since $a^{\mathsf{T}} a = 9$ is a number, it moves out of the product, and
$$P^2 = \frac{1}{81} a (a^{\mathsf{T}} a) a^{\mathsf{T}} = \frac{9}{81} a a^{\mathsf{T}} = P.$$
5. Take $v = (1, 1, 1)$; then $a^{\mathsf{T}} v = 1 + 2 + 2 = 5$, so $P v = \frac{5}{9}(1, 2, 2) = \left( \frac{5}{9}, \frac{10}{9}, \frac{10}{9} \right)$.
6. The error is $v - P v = \frac{1}{9}(4, -1, -1)$, and
$$(4, -1, -1) \cdot (1, 2, 2) = 4 - 2 - 2 = 0,$$
so the error is orthogonal to $U$, as the definition requires.
7. The trace of $P$ is $\frac{1 + 4 + 4}{9} = 1$, which is $\dim U$.

## Remarks

Every column of $P$ is a multiple of $a$, so $P$ has rank $1$ and image $U$, as a projection onto a line must.
With the unit vector $q = \frac{a}{3} = \left( \frac{1}{3}, \frac{2}{3}, \frac{2}{3} \right)$, the same matrix is $q q^{\mathsf{T}}$, which is the case $k = 1$ of the formula $Q Q^{\mathsf{T}}$.

What changes if we use another vector on the same line?
Replace $a$ by $t a$ with $t \ne 0$; then $t^2$ appears above and below and cancels:
$$\frac{(ta)(ta)^{\mathsf{T}}}{(ta)^{\mathsf{T}}(ta)} = \frac{t^2 \, a a^{\mathsf{T}}}{t^2 \, a^{\mathsf{T}} a} = P.$$
So $P$ depends only on the line, not on the vector chosen to describe it.
If instead $v$ changes, only the coefficient $\frac{v \cdot a}{9}$ changes, and a vector perpendicular to $a$, such as $(2, -1, 0)$, has projection $0$.

## Explanations

### L1 human

The projection onto a line keeps only the part of a vector that points along the line.
For $(1, 1, 1)$ and the line through $(1, 2, 2)$, that part is $\frac{5}{9}$ of $(1, 2, 2)$.
The leftover part, $\frac{1}{9}(4, -1, -1)$, makes a right angle with the line.

### L2 human

The number $\frac{5}{9}$ is $\frac{v \cdot a}{a \cdot a}$, the coefficient of $a$ in the projection, and the matrix $\frac{1}{9} a a^{\mathsf{T}}$ applies this rule to every vector at once.
In mechanics the same split takes a force and separates the part along a direction of motion from the part across it.
Watch out: the denominator is $\norm{a}^2 = 9$, not $\norm{a} = 3$.
Dividing by $3$ would give $\frac{5}{3}(1, 2, 2)$, and its error $(1, 1, 1) - \frac{5}{3}(1, 2, 2) = \frac{1}{3}(-2, -7, -7)$ has dot product $\frac{1}{3}(-2 - 14 - 14) = -10 \ne 0$ with $a$.
