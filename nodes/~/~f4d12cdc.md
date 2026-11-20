---
tag: ~f4d12cdc
kind: example
name: An orthogonal basis that is not orthonormal
msc: ["15A63"]
topics: [1D4JTZ9VS3]
audience: ug1
not_instance_of:
  - target: 0S9GGTR0EX
    note: the vectors (1, 1) and (1, -1) form an orthogonal basis of R^2, but each has norm the square root of 2, not 1
  - target: 0RW9TNNT87
    note: the family (1, 1), (1, -1) is orthogonal, but its vectors are not unit vectors
uses: [0FWJ0VW561, 0TS7VZJBWD, M2FAMD9HZN]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormal_basis
    locator: lead section
---

## Example

In $\mathbb{R}^2$ with the dot product, let $u_1 = (1, 1)$ and $u_2 = (1, -1)$.

1. $u_1 \cdot u_2 = 1 - 1 = 0$, so $u_1$ and $u_2$ are [[orthogonal|0TS7VZJBWD]].
2. They are two independent vectors of $\mathbb{R}^2$, so they form a basis.
3. But $\norm{u_1}^2 = \norm{u_2}^2 = 2 \neq 1$. So the basis is not an [[orthonormal basis|0FWJ0VW561]].
4. Let $v = (3, 1)$. The formula for orthonormal bases would give $v \cdot u_1 = 4$ and $v \cdot u_2 = 2$, and $4u_1 + 2u_2 = (6, 2) = 2v$. This is wrong.
5. The correct coefficients are $\frac{v \cdot u_1}{\norm{u_1}^2} = 2$ and $\frac{v \cdot u_2}{\norm{u_2}^2} = 1$. Indeed $2u_1 + u_2 = (3, 1)$.
6. The [[normalization|M2FAMD9HZN]] $e_j = u_j / \sqrt2$ gives an orthonormal basis, with coordinates $v \cdot e_1 = 2\sqrt2$ and $v \cdot e_2 = \sqrt2$.

## Remarks

The condition that fails is $\norm{u_j} = 1$.
In step 4 the error is the factor $\norm{u_j}^2 = 2$, and it is the same for both vectors, so the wrong result is $2v$.
For an orthogonal basis with different lengths, the wrong formula can give a vector that is not a multiple of $v$.
The matrix with columns $u_1$ and $u_2$ is not an orthogonal matrix, because $U^\top U = 2I_2$.

## Explanations

### L1 human

The arrows $(1, 1)$ and $(1, -1)$ meet at a right angle, but they are longer than $1$.
So they are orthogonal, but not orthonormal.
To make them orthonormal, divide each one by its length $\sqrt2$.

### L2 human

To repair an orthogonal basis, you can normalize it, or you can divide each coefficient by $\norm{u_j}^2$.

1. For $v = (0, 2)$, the dot products are $v \cdot u_1 = 2$ and $v \cdot u_2 = -2$.
2. Divide by $\norm{u_j}^2 = 2$: the coefficients are $1$ and $-1$.
3. Check: $u_1 - u_2 = (0, 2)$.

The typical use of this example is as a warning before the formula $v = \sum_j \ip{v}{e_j} e_j$ is applied.
A trap: "orthogonal set" and "orthonormal set" differ, but an "orthogonal matrix" has orthonormal columns.
