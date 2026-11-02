---
tag: FS2A7G2M6S
kind: definition
name: Thom spectrum
msc: [55P42, 55N22, 55R25]
defines: 6H8AGEN6NY
uses: [1GHF4EKBXS, 5MNYT3AFPH, WSZ40H5E4T, 1HDH716Z24, 2VD7GR64JJ]
sources:
  - url: https://en.wikipedia.org/wiki/Thom_space
---

## Definition

For $n \ge 0$, let $\gamma_n$ be the [[universal $n$-plane bundle|1HDH716Z24]] over the [[classifying space|WSZ40H5E4T]] $BO(n)$, and let $\varepsilon$ be the trivial line bundle.
Let $(B_n, f_n, g_n)_{n \ge 0}$ be a sequence of spaces $B_n$ with maps $f_n \colon B_n \to BO(n)$ and $g_n \colon B_n \to B_{n+1}$ such that $f_{n+1} \circ g_n$ classifies the [[vector bundle|P4DZM975BV]] $\xi_n \oplus \varepsilon$, where $\xi_n = f_n^* \gamma_n$.
Write $\operatorname{Th}(\xi)$ for the [[Thom space|5MNYT3AFPH]] of a bundle $\xi$.
The *Thom spectrum* of this sequence is the [[spectrum|1GHF4EKBXS]] $M$ with spaces $M_n = \operatorname{Th}(\xi_n)$.
Let $\Sigma$ be the reduced [[suspension|2VD7GR64JJ]].
The structure maps of $M$ are the composites $\Sigma \operatorname{Th}(\xi_n) \cong \operatorname{Th}(\xi_n \oplus \varepsilon) \to \operatorname{Th}(\xi_{n+1})$.
Here the second map is induced by the bundle map $\xi_n \oplus \varepsilon \to \xi_{n+1}$ that covers $g_n$.

## Remarks

Example: $B_n = BO(n)$ with $f_n = \id$ gives the spectrum $MO$.
Here $g_n \colon BO(n) \to BO(n+1)$ classifies $\gamma_n \oplus \varepsilon$, so the condition holds by construction.
Taking $B_n = BSO(n)$ gives $MSO$.
For complex bundles one uses $BU(n)$ and the universal complex bundle, whose Thom space is placed in degree $2n$; this gives the spectrum $MU$ of complex cobordism.

Non-example: keep the spaces $\operatorname{Th}(\gamma_n)$ but take all structure maps constant.
This is still a spectrum, but its structure maps are not induced by bundle maps, so it is not the Thom spectrum $MO$.
Indeed, all its stable homotopy groups vanish, while $\pi_0 MO \cong \Z/2$.

More generally one can form the Thom spectrum of a map $f \colon B \to BO$, taking for $B_n$ the preimage of $BO(n)$ under $f$, after replacing $f$ by a fibration.
