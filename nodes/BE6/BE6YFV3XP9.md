---
tag: BE6YFV3XP9
kind: definition
name: Yang–Baxter equation
msc: [16T25, 81R12, 82B23]
defines: 663BP8ZHS5
uses: [05EGHEQZAW, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Yang%E2%80%93Baxter_equation
---

## Definition

Let $V$ be a [[vector space|05EGHEQZAW]] over a field $k$ and let $R \colon V \otimes V \to V \otimes V$ be a linear map, where $\otimes$ is the [[tensor product|0BF2DE2SYK]] over $k$.
Define linear maps of $V \otimes V \otimes V$ by $R_{12} = R \otimes \id_V$ and $R_{23} = \id_V \otimes R$.
Let $R_{13}$ act as $R$ on the first and third factors and as the identity on the second.
If $\tau_{23}$ swaps the second and third factors, then $R_{13} = \tau_{23} R_{12} \tau_{23}$.
The map $R$ satisfies the *(quantum) Yang–Baxter equation* if
$$R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}.$$

## Remarks

Let $\tau \colon V \otimes V \to V \otimes V$ be the flip $u \otimes v \mapsto v \otimes u$ and $c = \tau \circ R$.
Then $R$ satisfies the Yang–Baxter equation if and only if $c$ satisfies the *braid relation* $c_{12} c_{23} c_{12} = c_{23} c_{12} c_{23}$, with $c_{12} = c \otimes \id_V$ and $c_{23} = \id_V \otimes c$.
Example: $R = \tau$.
On $u \otimes v \otimes w$, the left side sends it through $u \otimes w \otimes v$ and $v \otimes w \otimes u$ to $w \otimes v \otimes u$.
The right side sends it through $v \otimes u \otimes w$ and $w \otimes u \otimes v$ to $w \otimes v \otimes u$, so the two sides agree.
Example and non-example: let $R = A \otimes B$ for linear maps $A, B \colon V \to V$.
Then $R_{12} R_{13} R_{23} = A^2 \otimes BA \otimes B^2$ and $R_{23} R_{13} R_{12} = A^2 \otimes AB \otimes B^2$.
If $AB = BA$ the equation holds.
If $A, B$ are invertible and $AB \ne BA$, it fails, because $A^2 \otimes (BA - AB) \otimes B^2 \ne 0$.
Versions with a spectral parameter, $R(u)$ depending on $u \in \C$, are also called Yang–Baxter equations.
