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
We describe the [[quotient space|0SVR29SV1V]] $V / U$ and show that it is isomorphic to $\R$.

1. The coset of $(a, b)$ is
   $$(a, b) + U = \{(a + t, b + t) : t \in \R\}.$$
2. Every point of this coset has $x - y = (a + t) - (b + t) = a - b$.
   Conversely, a point $(x, y)$ with $x - y = a - b$ equals $(a, b) + (x - a)(1, 1)$, since then $y = b + (x - a)$.
   So the coset is the line $x - y = c$ with $c = a - b$.
3. Two vectors $(a, b)$ and $(a', b')$ have the same coset exactly when $a - b = a' - b'$.
   This is the condition $(a, b) - (a', b') \in U$, since a vector $(p, q)$ lies in $U$ exactly when $p = q$.
4. Define $\varphi \colon V / U \to \R$ by $\varphi\bigl((x, y) + U\bigr) = x - y$.
   By step 3, the value does not depend on the representative.
5. The map $\varphi$ is linear, because it comes from the linear map $(x, y) \mapsto x - y$ through representatives:
   $$\varphi\bigl(((x, y) + U) + ((x', y') + U)\bigr) = (x + x') - (y + y') = (x - y) + (x' - y'),$$
   and in the same way $\varphi\bigl(a((x, y) + U)\bigr) = ax - ay = a(x - y)$.
6. The map is injective.
   If $\varphi\bigl((x, y) + U\bigr) = 0$, then $x = y$, so $(x, y) \in U$ and the coset is $0 + U$.
7. The map is surjective, since $\varphi\bigl((c, 0) + U\bigr) = c$.
8. So $\varphi$ is an [[isomorphism|0XSJ25Z9M4]] and $V / U \cong \R$.

For instance, $\bigl((1, 0) + U\bigr) + \bigl((0, -1) + U\bigr) = (1, -1) + U$, and $\varphi$ gives $1 + 1 = 2$ on both sides.

## Remarks

The quotient is the set of parallel lines $x - y = c$, and $c$ is a coordinate on it.
Any line through $0$ other than $U$, such as the $x$-axis, meets each coset in exactly one point.
So such a line is a complement of $U$, and it is isomorphic to $V / U$ without being equal to it.
The count $\dim(V / U) = 2 - 1 = 1$ agrees with the [[dimension of a quotient space|0SXDQ6TN00]].

If $U$ is replaced by the line $\R(1, m)$, the cosets are the lines $mx - y = c$, and $(x, y) + U \mapsto mx - y$ is the isomorphism with $\R$.
If $U$ is replaced by $\{0\}$, every coset is a single point and the quotient is the plane itself.

## Explanations

### L1 human

Dividing the plane by the diagonal line squashes each line parallel to the diagonal to a single point.
These parallel lines are labeled by one number, the difference $x - y$.
So the quotient is a line of labels.

### L2 human

The map $(x, y) \mapsto x - y$ from $\R^2$ to $\R$ is linear and its kernel is exactly $U$.
So the quotient map followed by $\varphi$ is this map, which is the factorization given by the [[universal property|0ZERJX6PH6]].
The typical use of the example is as a model: to understand $V / U$, find a linear map that is zero exactly on $U$.
Watch out: the rule $(x, y) + U \mapsto x$ is not a map on $V / U$, since $(0, 0)$ and $(1, 1)$ are in the same coset but give $0$ and $1$.
