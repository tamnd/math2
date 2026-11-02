---
tag: WJQ2C6SKX5
kind: definition
name: Morphism of varieties
msc: [14A10]
defines: CDS1VWB7A3
uses: [HV6YBS0YDH, 4M94FZH9Y8, 0VGFHTM75Y, 02BH3MCBQB, G9WB27VWP7, 0VTH8KPCG2, JERVQT4C12]
sources:
  - url: https://en.wikipedia.org/wiki/Morphism_of_algebraic_varieties
---

## Definition

Let $k$ be an algebraically closed field and let $X$ and $Y$ be [[algebraic varieties|HV6YBS0YDH]] over $k$.
A *morphism* $\varphi \colon X \to Y$ is a [[continuous map|0VGFHTM75Y]] for the Zariski topologies with the following property.
For every [[open set|02BH3MCBQB]] $V \subseteq Y$ and every [[regular function|4M94FZH9Y8]] $f \colon V \to k$, the function $f \circ \varphi \colon \varphi^{-1}(V) \to k$ is regular.
An *isomorphism* is a morphism that has an inverse morphism.

## Remarks

If $X \subseteq k^m$ and $Y \subseteq k^n$ are [[affine varieties|JERVQT4C12]], a map $\varphi \colon X \to Y$ is a morphism if and only if $\varphi = (\varphi_1, \dots, \varphi_n)$ with each $\varphi_i$ a polynomial function on $X$.
A morphism $\varphi$ gives the [[ring homomorphism|0VTH8KPCG2]] $\varphi^* \colon k[Y] \to k[X]$, $f \mapsto f \circ \varphi$, on [[coordinate rings|G9WB27VWP7]].
This gives a bijection between morphisms $X \to Y$ and $k$-algebra homomorphisms $k[Y] \to k[X]$.

Example: $\varphi \colon k \to V(y - x^2)$, $t \mapsto (t, t^2)$, is an isomorphism with inverse $(x, y) \mapsto x$.

Non-example: $\psi \colon k \to C = V(y^2 - x^3)$, $t \mapsto (t^2, t^3)$, is a bijective morphism but not an isomorphism.
Its comorphism $k[C] \to k[t]$ has image $k[t^2, t^3]$, which does not contain $t$, so $\psi^*$ is not surjective and $\psi$ has no inverse morphism.
