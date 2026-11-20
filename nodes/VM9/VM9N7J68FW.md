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

Let $a = (1, 2, 2)$ in $\R^3$ with the [[dot product|05HQYM0R4G]], and let $U = \R a$.
We compute the matrix $P$ of the [[orthogonal projection|0Q8HZTJC7G]] onto $U$ and check it.

1. By the [[projection formulas|AK3JJ5HHG2]] with $A = a$ as a $3 \times 1$ matrix, $P = a (a^{\mathsf{T}} a)^{-1} a^{\mathsf{T}}$.
2. $a^{\mathsf{T}} a = 1 + 4 + 4 = 9$, so
$$P = \frac{1}{9} a a^{\mathsf{T}} = \frac{1}{9} \begin{pmatrix} 1 & 2 & 2 \\ 2 & 4 & 4 \\ 2 & 4 & 4 \end{pmatrix}.$$
3. Symmetric: entry $(i, j)$ is $a_i a_j / 9$, which equals entry $(j, i)$. So $P^{\mathsf{T}} = P$.
4. Idempotent: $P^2 = \frac{1}{81} a (a^{\mathsf{T}} a) a^{\mathsf{T}} = \frac{9}{81} a a^{\mathsf{T}} = P$.
5. Take $v = (1, 1, 1)$. Then $a^{\mathsf{T}} v = 5$, so $P v = \frac{5}{9} (1, 2, 2) = (5/9, 10/9, 10/9)$.
6. The error is $v - P v = (4/9, -1/9, -1/9)$, and $(4/9, -1/9, -1/9) \cdot (1, 2, 2) = (4 - 2 - 2)/9 = 0$. So the error is orthogonal to $U$.
7. The trace of $P$ is $(1 + 4 + 4)/9 = 1 = \dim U$.

## Remarks

Every column of $P$ is a multiple of $a$, so $P$ has rank $1$ and image $U$.
For a unit vector $q = a / 3 = (1/3, 2/3, 2/3)$, the same matrix is $q q^{\mathsf{T}}$.
If $a$ is replaced by $ta$ with $t \ne 0$, then $P$ does not change, because $t^2$ cancels in $\frac{(ta)(ta)^{\mathsf{T}}}{(ta)^{\mathsf{T}}(ta)}$.

## Explanations

### L1 human

The projection onto a line keeps only the part of a vector that points along the line.
For $(1, 1, 1)$ and the line through $(1, 2, 2)$, that part is $\frac{5}{9}$ of $(1, 2, 2)$.

### L2 human

The number $\frac{5}{9}$ is $\frac{v \cdot a}{a \cdot a}$, the coefficient of $a$ in the projection.
The matrix $\frac{1}{9} a a^{\mathsf{T}}$ applies this rule to every vector at once.
The typical use is to split a force into a part along a direction and a part across it.
The trap is to divide by $\norm{a} = 3$ instead of $\norm{a}^2 = 9$.
