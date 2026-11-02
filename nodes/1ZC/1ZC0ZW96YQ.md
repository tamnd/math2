---
tag: 1ZC0ZW96YQ
kind: definition
name: Shelf
msc: [20N02, 57K12]
defines: PDFC0MRYR8
uses: [9689SFPVE9, VEFE5WZMS3]
sources:
  - url: https://en.wikipedia.org/wiki/Racks_and_quandles
---

## Definition

A *shelf* is a [[magma|9689SFPVE9]] $(X, \triangleright)$ whose operation is [[left self-distributive|VEFE5WZMS3]]:
$$x \triangleright (y \triangleright z) = (x \triangleright y) \triangleright (x \triangleright z) \quad \text{for all } x, y, z \in X.$$

## Remarks

Equivalently, for every $x \in X$ the left translation $y \mapsto x \triangleright y$ is an endomorphism of $(X, \triangleright)$.
A shelf is a [[rack|X74VY86TSX]] when every left translation is a bijection.

Example: let $X = \set{1, 2}$ with $1 \triangleright y = 2$ and $2 \triangleright y = y$ for all $y$; this is the Laver table $A_1$.
If $x = 2$, both sides equal $y \triangleright z$.
If $x = 1$, the left side is $2$, and the right side is $2 \triangleright 2 = 2$.
So $X$ is a shelf; it is not a rack, since $y \mapsto 1 \triangleright y$ is not injective.

Non-example: $(\Z, +)$, since $x + (y + z) \ne (x + y) + (x + z)$ for $x \ne 0$.

Some authors use right self-distributivity instead, with $(z \triangleleft y) \triangleleft x = (z \triangleleft x) \triangleleft (y \triangleleft x)$; the two conventions are related by $x \triangleright y = y \triangleleft x$.
In Mathlib this structure is the class `Shelf`.
