---
tag: QS36GTKQAZ
kind: definition
name: Nonassociative algebra
msc: [17A01]
defines: 60W3THKGA7
uses: [0310REJJY8, 0NZ8JA25WK, YP5TQ6WFVN]
sources:
  - url: https://en.wikipedia.org/wiki/Non-associative_algebra
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with unit.
A *nonassociative algebra* over $R$ is an $R$-[[module|0NZ8JA25WK]] $A$ with a map $A \times A \to A$, $(x, y) \mapsto xy$, that is $R$-bilinear:
$$(rx + sy)z = r(xz) + s(yz) \quad \text{and} \quad z(rx + sy) = r(zx) + s(zy)$$
for all $r, s \in R$ and $x, y, z \in A$.
Neither associativity nor a unit element is required.

## Remarks

With $R = \Z$, a nonassociative algebra is the same as a [[nonassociative ring|YP5TQ6WFVN]].
When $R$ is a field, it is an algebra over a field.
Example: $\R^3$ with the cross product is a nonassociative algebra over $\R$, because the cross product is bilinear.
It is not associative: $(e_1 \times e_1) \times e_2 = 0$, while $e_1 \times (e_1 \times e_2) = e_1 \times e_3 = -e_2$.
Non-example: $\R$ with the product $x * y = x + y$ is not an algebra, because $(2x) * y = 2x + y$ differs from $2(x * y) = 2x + 2y$ when $y \neq 0$.
