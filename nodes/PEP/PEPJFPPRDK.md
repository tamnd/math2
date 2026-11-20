---
tag: PEPJFPPRDK
kind: example
name: The plane modulo the line y = x
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
instance_of: [0BR3FY5Q8M]
illustrates: [YYH67TQ9GV]
uses: [0SVR29SV1V, 0XSJ25Z9M4]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)
    locator: Examples
---

## Example

Let $V = \R^2$ and $U = \R(1, 1)$, the line $y = x$.
We describe the [[quotient space|0SVR29SV1V]] $V / U$ and check that it is isomorphic to $\R$.

1. The coset of $(a, b)$ is $(a, b) + U = \{(a + t, b + t) : t \in \R\}$.
2. Every point of this coset has $x - y = a - b$. Conversely, a point with $x - y = a - b$ is $(a, b) + (x - a)(1, 1)$. So the coset is the line $x - y = c$ with $c = a - b$.
3. Two vectors $(a, b)$ and $(a', b')$ have the same coset exactly when $a - b = a' - b'$, which is the condition $(a, b) - (a', b') \in U$.
4. Define $\varphi \colon V / U \to \R$ by $\varphi((x, y) + U) = x - y$. By step 3, the value does not depend on the representative.
5. $\varphi$ is linear: $\varphi\big(((x, y) + U) + ((x', y') + U)\big) = (x + x') - (y + y')$, which is the sum of the two values. Scalars work the same way.
6. $\varphi$ is injective: $\varphi((x, y) + U) = 0$ means $x = y$, so $(x, y) \in U$ and the coset is $0 + U$.
7. $\varphi$ is surjective: $\varphi((c, 0) + U) = c$.
8. So $\varphi$ is an [[isomorphism|0XSJ25Z9M4]] and $V / U \cong \R$.

For instance, $((1, 0) + U) + ((0, -1) + U) = (1, -1) + U$, and $\varphi$ gives $1 + 1 = 2$.

## Remarks

The quotient is the set of parallel lines $x - y = c$, and $c$ is a coordinate on it.
Any line through $0$ other than $U$, such as the $x$-axis, meets each coset in one point, so it is a complement of $U$ isomorphic to $V / U$.
The dimension count $\dim(V / U) = 2 - 1 = 1$ agrees with the [[dimension of a quotient|0SXDQ6TN00]].

## Explanations

### L1 human

Dividing the plane by the diagonal line collapses each line parallel to the diagonal to a point.
The parallel lines are labelled by one number, $x - y$, so the quotient is a line.

### L2 human

The map $(x, y) \mapsto x - y$ from $\R^2$ to $\R$ is linear with kernel $U$.
The quotient map followed by $\varphi$ is this map, which is the factorization of the [[universal property|0ZERJX6PH6]].
