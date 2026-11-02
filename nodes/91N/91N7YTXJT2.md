---
tag: 91N7YTXJT2
kind: definition
name: Formal group law in topology
msc: [55N22, 14L05]
defines: TNHP7XXYZT
uses: [0310REJJY8, 072W67KFYK, H28PSZR7XG, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_group_law
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
A *(one-dimensional, commutative) formal group law* over $R$ is a [[formal power series|072W67KFYK]] $F(x, y) \in R[\![x, y]\!]$ such that:

1. $F(x, y) \equiv x + y$ modulo terms of total degree at least $2$.
2. $F(x, F(y, z)) = F(F(x, y), z)$ in $R[\![x, y, z]\!]$.
3. $F(x, y) = F(y, x)$.

Let $E$ be a multiplicative [[generalized cohomology theory|H28PSZR7XG]] with coefficient ring $E^* = E^*(\mathrm{pt})$.
A *complex orientation* of $E$ is a class $x \in \tilde E^2(\C P^\infty)$ whose restriction to $\tilde E^2(\C P^1) \cong E^0(\mathrm{pt})$ is the unit $1$.
Then $E^*(\C P^\infty) = E^*[\![x]\!]$ and $E^*(\C P^\infty \times \C P^\infty) = E^*[\![x_1, x_2]\!]$, with $x_i$ pulled back from the $i$-th factor.
Let $m \colon \C P^\infty \times \C P^\infty \to \C P^\infty$ classify the tensor product of the two universal line bundles.
The *formal group law of $(E, x)$* is the power series $F$ over $E^*$ with $m^*(x) = F(x_1, x_2)$.
It satisfies the three conditions above, and it is homogeneous of degree $2$ when $x$, $x_1$ and $x_2$ have degree $2$.

## Remarks

Example: in ordinary cohomology $H^*(-; \Z)$ with $x$ the first Chern class of the universal line bundle, $c_1(L_1 \otimes L_2) = c_1(L_1) + c_1(L_2)$, so $F(x, y) = x + y$.
The three conditions are clear for this additive law.

Example: in complex K-theory with Bott class $\beta \in K^{-2}(\mathrm{pt})$, take $x = \beta^{-1}([L] - 1)$ for the universal line bundle $L$.
Since $[L_1 L_2] - 1 = ([L_1] - 1) + ([L_2] - 1) + ([L_1] - 1)([L_2] - 1)$, the law is $F(x, y) = x + y + \beta x y$, the multiplicative formal group law.

Non-example: $G(x, y) = x + y + x^2 y$ over $\Z$ satisfies clause 1 but fails clause 3, since $G(y, x) = x + y + x y^2$.

There is a universal formal group law over the Lazard ring $L$: formal group laws over $R$ correspond to ring maps $L \to R$.
