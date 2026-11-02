---
tag: XFJVAMSAQ2
kind: definition
name: Superalgebra
msc: [17A70, 16W55, 16W50]
defines: 6JZW4JC68Z
uses: [0GYGHKX834, 09VDS2W1E8]
sources:
  - url: https://en.wikipedia.org/wiki/Superalgebra
---

## Definition

Let $K$ be a [[commutative ring|0GYGHKX834]].
Let $A$ be a [[$K$-module|09VDS2W1E8]] with a direct sum decomposition $A = A_0 \oplus A_1$.
Then $A$ with a $K$-bilinear product $A \times A \to A$ is a *superalgebra* over $K$ if
$$A_i A_j \subseteq A_{i + j}$$
for all $i, j \in \Z/2\Z$, with indices added modulo $2$.
Elements of $A_0$ are *even*, elements of $A_1$ are *odd*, and a nonzero element of $A_0 \cup A_1$ is *homogeneous* of parity $\abs{a} \in \{0, 1\}$.
Unless stated otherwise the product is associative with a unit.

## Remarks

A superalgebra is *supercommutative* if $ab = (-1)^{\abs{a}\abs{b}} ba$ for all homogeneous $a, b$.
Example: the exterior algebra $\Lambda(V)$ of a vector space $V$, with $A_0$ the sum of the even powers $\Lambda^{2m} V$ and $A_1$ the sum of the odd powers.
The product maps $\Lambda^p V \times \Lambda^r V$ into $\Lambda^{p+r} V$, and $p + r$ has the parity of the sum, so the condition holds; moreover $\Lambda(V)$ is supercommutative.
Example: the matrix ring $M_2(K)$, with $A_0$ the diagonal matrices and $A_1$ the off-diagonal ones, is a superalgebra that is not supercommutative.
Non-example: $K[x]$ with $A_0 = K$ and $A_1 = xK[x]$ fails the condition, since $x \in A_1$ but $x \cdot x = x^2 \notin A_0$.
Equivalently, a superalgebra is a monoid object in the category of $\Z/2\Z$-graded modules, with the tensor product of graded modules.
