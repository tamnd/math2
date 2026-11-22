---
tag: 6NZCDBCSKQ
kind: example
name: A unitary matrix written as a phase times a special unitary matrix
msc: ["15B57", "20G20"]
topics: [AZS5BPF5H3]
audience: ug2
instance_of: [VW5H9XFNJB, 0AR68JTMDT]
uses: [0D6RMJ10M9, 0C3CFHDN6R, ZRYYPHWESP]
sources:
  - url: https://en.wikipedia.org/wiki/Unitary_group
    locator: Properties
---

## Example

Let $U = \begin{pmatrix} 0 & i \\ 1 & 0 \end{pmatrix}$.
We check that $U$ lies in the [[unitary group|VW5H9XFNJB]] $U(2)$, and we write it as a diagonal phase matrix times an element of the [[special unitary group|ZRYYPHWESP]] $SU(2)$.

1. Transpose and conjugate to get $U^* = \begin{pmatrix} 0 & 1 \\ -i & 0 \end{pmatrix}$, and then multiply:
$$U^*U = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 1 & 0 \cdot i + 1 \cdot 0 \\ (-i) \cdot 0 + 0 \cdot 1 & (-i) \cdot i + 0 \cdot 0 \end{pmatrix} = I_2.$$
So $U$ is [[unitary|0D6RMJ10M9]].
2. The determinant is $\det U = 0 \cdot 0 - i \cdot 1 = -i$. It has absolute value $1$, but it is not $1$, so $U \notin SU(2)$.
3. To remove the phase $-i$, multiply $U$ on the left by $\operatorname{diag}(i, 1)$, whose determinant is $i = \overline{-i}$. This multiplies the first row by $i$:
$$V = \operatorname{diag}(i, 1)\, U = \begin{pmatrix} 0 & i \cdot i \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
4. The matrix $V$ is a product of two unitary matrices, so it is unitary, and $\det V = 0 \cdot 0 - (-1) \cdot 1 = 1$. So $V \in SU(2)$.
5. The inverse of $\operatorname{diag}(i, 1)$ is $\operatorname{diag}(-i, 1)$, so
$$U = \operatorname{diag}(-i, 1)\, V = \operatorname{diag}(\det U, 1)\, V.$$

Check: $\operatorname{diag}(-i, 1) V$ multiplies the first row $(0, -1)$ of $V$ by $-i$, which gives $(0, i)$, the first row of $U$.

## Remarks

The same method works for every $U \in U(n)$.
Multiply on the left by $\operatorname{diag}(\overline{\det U}, 1, \dots, 1)$, and the product has determinant $\overline{\det U} \det U = \abs{\det U}^2 = 1$.
So every unitary matrix is $\operatorname{diag}(\det U, 1, \dots, 1)$ times an element of $SU(n)$, and the first factor is fixed by $U$.

A second method uses a scalar in place of the diagonal phase.
Since $\det(cU) = c^2 \det U$ for a $2 \times 2$ matrix, the choice $c = e^{i\pi/4}$ gives $c^2 = i$ and $\det(cU) = i \cdot (-i) = 1$.
So $U = \overline{c}\,(cU)$ with $cU \in SU(2)$.
This factorization is not unique, because $-c$ works as well, and $(-c)U = -(cU)$ is a different element of $SU(2)$.

The factor $V$ here is the quarter turn $R(\pi/2)$ of the real plane, so it lies even in $SO(2) \subseteq SU(2)$.

## Explanations

### L1 human

Every unitary matrix splits into two parts.
One part only turns the first coordinate in the complex plane, by the angle of the determinant.
The other part is a unitary matrix whose determinant is exactly $1$.
Here the first part multiplies by $-i$, and the second part is the ordinary quarter turn of the plane.

### L2 human

Here is the typical use: a question about $U(n)$ often reduces to a question about $SU(n)$ and one phase.
For example, to list all $U \in U(2)$ with $\det U = -i$, take the elements $V$ of $SU(2)$ and form $\operatorname{diag}(-i, 1) V$.
Watch out: the phase factor and $V$ need not commute.
Here
$$V \operatorname{diag}(-i, 1) = \begin{pmatrix} 0 & -1 \\ -i & 0 \end{pmatrix} \ne \begin{pmatrix} 0 & i \\ 1 & 0 \end{pmatrix} = \operatorname{diag}(-i, 1) V,$$
so the side on which you put the phase matters.
