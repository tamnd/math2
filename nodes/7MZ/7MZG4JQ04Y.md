---
tag: 7MZG4JQ04Y
kind: definition
name: Braided monoidal category
msc: [18M15]
defines: VT8SFWT0XW
uses: [M3MSQ3NKAE, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Braided_monoidal_category
---

## Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]].
A *braiding* on $\mathcal{C}$ is a natural isomorphism $\gamma$ with components $\gamma_{A,B} \colon A \otimes B \to B \otimes A$, natural in $A$ and $B$.
It must satisfy the two hexagon identities for all objects $A, B, C$:

1. $\alpha_{B,C,A} \circ \gamma_{A, B \otimes C} \circ \alpha_{A,B,C} = (\id_B \otimes \gamma_{A,C}) \circ \alpha_{B,A,C} \circ (\gamma_{A,B} \otimes \id_C)$ as morphisms $(A \otimes B) \otimes C \to B \otimes (C \otimes A)$;
2. $\alpha^{-1}_{C,A,B} \circ \gamma_{A \otimes B, C} \circ \alpha^{-1}_{A,B,C} = (\gamma_{A,C} \otimes \id_B) \circ \alpha^{-1}_{A,C,B} \circ (\id_A \otimes \gamma_{B,C})$ as morphisms $A \otimes (B \otimes C) \to (C \otimes A) \otimes B$.

A *braided monoidal category* is a monoidal category with a braiding.

## Remarks

Example: $\mathbf{Vect}_k$ with the usual tensor product and $\gamma_{V,W}(v \otimes w) = w \otimes v$.
On $(u \otimes v) \otimes w$ both sides of the first hexagon give $v \otimes (w \otimes u)$, and both sides of the second hexagon send $u \otimes (v \otimes w)$ to $(w \otimes u) \otimes v$.
Non-example: on $\mathbf{Vect}_k$ with $\operatorname{char} k \ne 2$, the natural isomorphism $\gamma_{V,W}(v \otimes w) = -\, w \otimes v$ is not a braiding.
In each hexagon the left side contains one copy of $\gamma$ and the right side two, so for nonzero spaces the two sides differ by the sign $-1$.
The first hexagon says that moving $A$ past $B \otimes C$ in one step equals moving it past $B$ and then past $C$.
The second says the same for moving $C$ past $A \otimes B$.
