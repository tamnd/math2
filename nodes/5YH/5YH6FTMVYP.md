---
tag: 5YH6FTMVYP
kind: definition
name: Closed monoidal category
msc: [18D15, 18M05]
defines: EKJBDD07TY
uses: [M3MSQ3NKAE, TZHF6ZM92S, BFBNQ36QS8]
sources:
  - url: https://en.wikipedia.org/wiki/Closed_monoidal_category
---

## Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]].
$\mathcal{C}$ is *closed* (more precisely, right closed) if for every object $B$ the functor $- \otimes B \colon \mathcal{C} \to \mathcal{C}$ has a right [[adjoint|TZHF6ZM92S]], written $[B, -] \colon \mathcal{C} \to \mathcal{C}$.
Equivalently, for all objects $A, B, C$ there is a bijection
$$\Hom_{\mathcal{C}}(A \otimes B, C) \cong \Hom_{\mathcal{C}}(A, [B, C]),$$
natural in $A$ and $C$.
The object $[B, C]$ is called the internal hom.

## Remarks

If also every functor $B \otimes -$ has a right adjoint, $\mathcal{C}$ is called biclosed; for a symmetric monoidal category the two notions agree.
Example: $\mathbf{Vect}_k$ with $[B, C]$ the space of linear maps $B \to C$; a linear map $f \colon A \otimes B \to C$ corresponds to $a \mapsto (b \mapsto f(a \otimes b))$.
Non-example: $\mathbf{Set}$ with the disjoint union $\sqcup$ as tensor product and the empty set as unit is monoidal but not closed.
A left adjoint preserves the initial object, but $\emptyset \sqcup B = B$ is not empty when $B$ is nonempty, so $- \sqcup B$ has no right adjoint.
A [[Cartesian closed category|BFBNQ36QS8]] is a closed monoidal category whose tensor product is the categorical product.
