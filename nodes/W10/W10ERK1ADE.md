---
tag: W10ERK1ADE
kind: definition
name: Cup product
msc: [55N45]
defines: JX47MS1R1H
uses: [6N7BC70CX0, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Cup_product
---

## Definition

Let $X$ be a topological space and let $R$ be a [[commutative ring|0310REJJY8]] with $1$.
For a singular simplex $\sigma \colon \Delta^{n} \to X$ with vertices $v_0, \ldots, v_n$, write $\sigma|_{[v_i, \ldots, v_j]}$ for its restriction to the face spanned by $v_i, \ldots, v_j$.
For cochains $\varphi \in C^k(X; R)$ and $\psi \in C^l(X; R)$, the *cup product* $\varphi \smile \psi \in C^{k+l}(X; R)$ is
$$(\varphi \smile \psi)(\sigma) = \varphi\big(\sigma|_{[v_0, \ldots, v_k]}\big) \cdot \psi\big(\sigma|_{[v_k, \ldots, v_{k+l}]}\big)$$
for every singular simplex $\sigma \colon \Delta^{k+l} \to X$.
It satisfies $\delta(\varphi \smile \psi) = \delta\varphi \smile \psi + (-1)^k \varphi \smile \delta\psi$.
Hence it induces a bilinear map $\smile \colon H^k(X; R) \times H^l(X; R) \to H^{k+l}(X; R)$ on [[singular cohomology|6N7BC70CX0]], also called the cup product.

## Remarks

The cup product on cohomology is associative, the class of the constant $0$-cochain $1$ is a unit, and $a \smile b = (-1)^{kl}\, b \smile a$ for $a \in H^k$ and $b \in H^l$.
Graded commutativity holds on cohomology but not on cochains.
It is natural: $f^*(a \smile b) = f^*(a) \smile f^*(b)$ for a continuous map $f$.
The same formula gives relative products such as $H^k(X; R) \times H^l(X, A; R) \to H^{k+l}(X, A; R)$.

Example: for the torus $T^2 = S^1 \times S^1$, $H^1(T^2; \Z) \cong \Z^2$ with generators $\alpha$ and $\beta$ dual to the two circles.
Then $\alpha \smile \beta$ generates $H^2(T^2; \Z) \cong \Z$, and $\alpha \smile \alpha = 0$.

Non-example: the pointwise product $(\varphi\psi)(\sigma) = \varphi(\sigma)\psi(\sigma)$ only makes sense when $\varphi$, $\psi$ and $\sigma$ all have the same dimension.
So it does not define a product $C^k \times C^l \to C^{k+l}$.
The cup product avoids this by splitting each simplex into a front face and a back face.
