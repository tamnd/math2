---
tag: ZP62TRA4FT
kind: definition
name: Representation ring
msc: [19A22, 20C15]
defines: RKTX9MN7Q3
uses: [G5S1M9, WYGRXCG2RN, 5FDMY7PDYY, F0HQXQ0HCD, FX3NEFYFFN, RMWMYBY8TC, 0310REJJY8]
sources:
  - url: https://en.wikipedia.org/wiki/Representation_ring
---

## Definition

Let $G$ be a finite [[group|G5S1M9]].
Isomorphism classes of finite-dimensional complex [[representations|WYGRXCG2RN]] of $G$ form a commutative monoid under direct sum $[V] + [W] = [V \oplus W]$.
The *representation ring* $R(G)$ is the [[Grothendieck group|5FDMY7PDYY]] of this monoid.
Its multiplication is given on classes by the [[tensor product|F0HQXQ0HCD]] $[V] \cdot [W] = [V \otimes_{\C} W]$ and extended bilinearly.
Here $G$ acts on $V \otimes_{\C} W$ by $g(v \otimes w) = gv \otimes gw$.
It is a [[commutative ring|0310REJJY8]] whose unit is the class of the trivial one-dimensional representation.

## Remarks

By Maschke's theorem every representation is a direct sum of [[irreducible representations|FX3NEFYFFN]], uniquely up to order.
So $R(G)$ is free abelian with basis the classes of the irreducible representations, and its rank is the number of conjugacy classes of $G$.
The [[character|RMWMYBY8TC]] $\chi_V$ satisfies $\chi_{V \oplus W} = \chi_V + \chi_W$ and $\chi_{V \otimes W} = \chi_V \chi_W$, so it gives an injective ring homomorphism from $R(G)$ to the ring of class functions $G \to \C$.
Example: for $G = \Z/3\Z$, the irreducible representations are $1, \rho, \rho^2$, where $\rho$ sends a generator to $e^{2\pi i/3}$, and $R(G) \cong \Z[\rho]/(\rho^3 - 1)$.
Non-example: the element $[1] - [\rho]$ of $R(\Z/3\Z)$ is not the class of a representation, since its multiplicity of $\rho$ is negative.
The same construction works over other fields and for compact groups with continuous finite-dimensional representations.
