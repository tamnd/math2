---
tag: SDJ4ADZK8M
kind: definition
name: Tensor product of fields
msc: [12F99, 15A69]
defines: ANH16GQJZQ
uses: [0WQ1A8SHTZ, 0G31VJ5YS5, 0GYGHKX834, 0GK1WB9R98]
sources:
  - url: https://en.wikipedia.org/wiki/Tensor_product_of_fields
---

## Definition

Let $K$ be a field and let $E$ and $F$ be [[field extensions|0WQ1A8SHTZ]] of $K$.
The *tensor product* $E \otimes_K F$ is the [[tensor product|0G31VJ5YS5]] of the $K$-vector spaces $E$ and $F$, with the unique $K$-bilinear multiplication such that
$$(a \otimes b)(c \otimes d) = ac \otimes bd \quad \text{for } a, c \in E \text{ and } b, d \in F.$$
It is a [[commutative ring|0GYGHKX834]] with identity $1 \otimes 1$ and a $K$-algebra.

## Remarks

The maps $a \mapsto a \otimes 1$ and $b \mapsto 1 \otimes b$ embed $E$ and $F$ into $E \otimes_K F$.
If $E = K(\alpha)$ is finite and $f$ is the [[minimal polynomial|0GK1WB9R98]] of $\alpha$ over $K$, then $E \otimes_K F \cong F[x]/(f)$.
If moreover $f = g_1 \cdots g_r$ with distinct monic irreducible $g_i \in F[x]$, the Chinese remainder theorem gives $E \otimes_K F \cong \prod_{i=1}^r F[x]/(g_i)$, a product of fields.

Example: $\C \otimes_\R \C \cong \C \times \C$.
Check: $\C = \R(i)$ with $f = x^2 + 1$, and over $F = \C$ one has $x^2 + 1 = (x - i)(x + i)$, so $\C \otimes_\R \C \cong \C[x]/(x - i) \times \C[x]/(x + i) \cong \C \times \C$.

Non-example: $E \otimes_K F$ need not be a field, even when $E$ and $F$ are; $\C \otimes_\R \C$ has the zero divisors $(1, 0)$ and $(0, 1)$ in the product above.
