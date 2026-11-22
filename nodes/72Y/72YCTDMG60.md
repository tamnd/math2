---
tag: 72YCTDMG60
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
This pair is an orthogonal basis, but it is not an orthonormal basis, and the coordinate formula for orthonormal bases gives a wrong answer on it.

1. The pair is [[orthogonal|0TS7VZJBWD]], because
$$u_1 \cdot u_2 = 1 \cdot 1 + 1 \cdot (-1) = 0.$$
2. The pair is a basis, because two orthogonal nonzero vectors are independent, and two independent vectors span $\mathbb{R}^2$.
3. The lengths are wrong for an [[orthonormal basis|0FWJ0VW561]], since
$$\norm{u_1}^2 = 1 + 1 = 2, \qquad \norm{u_2}^2 = 1 + 1 = 2,$$
   and an orthonormal basis needs $1$ in both places.
4. Take $v = (3, 1)$ and apply the formula $v = \sum_j (v \cdot u_j) u_j$ anyway.
   It gives $v \cdot u_1 = 4$ and $v \cdot u_2 = 2$, and
$$4 u_1 + 2 u_2 = (4, 4) + (2, -2) = (6, 2) = 2v,$$
   which is not $v$.
5. The correct coefficients divide by the squared lengths:
$$\frac{v \cdot u_1}{\norm{u_1}^2} = \frac42 = 2, \qquad \frac{v \cdot u_2}{\norm{u_2}^2} = \frac22 = 1.$$
   Check: $2 u_1 + u_2 = (2, 2) + (1, -1) = (3, 1)$.
6. The [[normalization|M2FAMD9HZN]] $e_j = u_j / \sqrt2$ repairs the basis.
   Then $v \cdot e_1 = \tfrac{4}{\sqrt2} = 2\sqrt2$ and $v \cdot e_2 = \tfrac{2}{\sqrt2} = \sqrt2$, and
$$2\sqrt2 \, e_1 + \sqrt2 \, e_2 = 2 u_1 + u_2 = (3, 1).$$

## Remarks

The condition that fails is $\norm{u_j} = 1$, and only that condition.
In step 4 each term is off by the factor $\norm{u_j}^2 = 2$, and the factor is the same for both vectors, so the wrong answer is exactly $2v$.
When the lengths differ, the error is worse.
For the orthogonal basis $(1, 1)$, $(2, -2)$ with squared lengths $2$ and $8$, the same $v = (3, 1)$ gives $4(1, 1) + 4(2, -2) = (12, -4)$, which is not even a multiple of $v$.

The matrix $U$ with columns $u_1$ and $u_2$ is not an orthogonal matrix, because
$$U^{\mathsf{T}} U = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2 I_2.$$
The off-diagonal zeros record the orthogonality, and the diagonal $2$s record the wrong lengths.

## Explanations

### L1 human

The arrows $(1, 1)$ and $(1, -1)$ meet at a right angle, but each one is longer than $1$.
So they are orthogonal, but they are not orthonormal.
To make them orthonormal, shrink each one by its length $\sqrt2$, which is about $1.41$.

### L2 human

You can repair an orthogonal basis in two ways: normalize it first, or divide each coefficient by $\norm{u_j}^2$.
Take $v = (0, 2)$ and the second way.
The dot products are $v \cdot u_1 = 2$ and $v \cdot u_2 = -2$.
Divide each by $\norm{u_j}^2 = 2$ to get the coefficients $1$ and $-1$.
Check: $u_1 - u_2 = (1, 1) - (1, -1) = (0, 2)$.
This is the formula $v = \sum_j \frac{\ip{v}{u_j}}{\norm{u_j}^2} u_j$ for orthogonal bases, and it reduces to the orthonormal formula when every $\norm{u_j} = 1$.
Watch out for the words: an "orthogonal set" need not be orthonormal, but an "orthogonal matrix" must have orthonormal columns.
