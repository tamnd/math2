---
tag: ZDZ6FAAGAF
kind: example
name: Spin factor
msc: [17C20, 17C90, 17C65]
instance_of: [6C2MCVB8C7, WYE4E80T43]
uses: [6C2MCVB8C7, WYE4E80T43, 0QVNCJXRY3]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_operator_algebra
---

## Example

Let $V$ be a real [[inner product space|0QVNCJXRY3]] with inner product $\ip{\cdot}{\cdot}$ and norm $\abs{u} = \ip{u}{u}^{1/2}$.
The *spin factor* is $J = \R \oplus V$ with the product
$$(a, u)(b, v) = \big(ab + \ip{u}{v},\ av + bu\big), \qquad a, b \in \R,\ u, v \in V.$$
It is a [[Jordan algebra|6C2MCVB8C7]] with unit $1 = (1, 0)$, and it is [[formally real|WYE4E80T43]].

Check of commutativity: the formula is symmetric under exchanging $(a, u)$ and $(b, v)$.

Check of the Jordan identity: for $x = (a, u)$ one computes $x^2 = (a^2 + \abs{u}^2, 2au)$.
Hence $x^2 = 2a\, x - (a^2 - \abs{u}^2)\, 1$, so $x^2$ lies in the span of $1$ and $x$.
Write $L_z$ for the map $w \mapsto zw$; then $L_{x^2} = 2a L_x - (a^2 - \abs{u}^2) \id$ commutes with $L_x$.
Applied to $y$, this gives $x^2(xy) = x(x^2 y)$, which is the Jordan identity $(xy)x^2 = x(yx^2)$ by commutativity.

Check of formal reality: the first coordinate of $x_1^2 + \cdots + x_n^2$, with $x_k = (a_k, u_k)$, is $\sum_k (a_k^2 + \abs{u_k}^2)$.
If the sum of squares is $0$, then every $a_k$ and every $u_k$ is $0$.

## Remarks

For $V = \R^n$ the spin factor has dimension $n + 1$, and it is simple when $n \ge 2$.
For $n = 1$ it is isomorphic to $\R \oplus \R$ with componentwise product, through $(a, u) \mapsto (a + u, a - u)$.
Spin factors are special: they embed in the Clifford algebra of $V$, where $u^2 = \abs{u}^2$ for $u \in V$.
The spin factor on $\R^n$ is one of the families in the [[Jordan–von Neumann–Wigner classification|AE979FBMPD]].

## Explanations

### L1 human

The spin factor adds a real number to a vector, and multiplies such pairs by a rule that mixes the dot product with scalar multiplication.
Each element satisfies a quadratic equation, much like a complex number.
This is enough to make the product a Jordan product.
The name comes from physics: the Pauli spin matrices span a copy of it inside the $2 \times 2$ complex matrices.
