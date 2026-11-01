---
tag: VA3DY2YX83
kind: statement
role: theorem
name: Grothendieck's local duality
msc: [13D45, 13H10]
uses: [N1QJQEGBFC, MZ02BKPHJA, NJ3APQ8BHH, W5ECXPM6FW, QCJN05GN64, 6JB30BXDA2, 4P7GBWJ4RR, 05QY1VEBYD]
about: [6JB30BXDA2, W5ECXPM6FW]
sources:
  - url: https://en.wikipedia.org/wiki/Local_cohomology
---

## Statement

Let $(R, \mathfrak{m}, k)$ be a [[Cohen–Macaulay|N1QJQEGBFC]] [[local ring|MZ02BKPHJA]] of dimension $d$ with [[residue field|NJ3APQ8BHH]] $k$, and assume that $R$ has a [[canonical module|W5ECXPM6FW]] $\omega_R$.
Let $E = E_R(k)$ be the [[injective hull|QCJN05GN64]] of $k$.
Let $M$ be a [[finitely generated|05QY1VEBYD]] $R$-module and let $i$ be an integer.
Then there is an isomorphism, natural in $M$,
$$H^i_{\mathfrak{m}}(M) \cong \Hom_R\left(\operatorname{Ext}^{d-i}_R(M, \omega_R), E\right),$$
where $H^i_{\mathfrak{m}}$ is [[local cohomology|6JB30BXDA2]] and $\operatorname{Ext}$ is the [[Ext functor|4P7GBWJ4RR]].

## Remarks

If $R$ is Gorenstein, then $\omega_R = R$ and the formula reads $H^i_{\mathfrak{m}}(M) \cong \Hom_R(\operatorname{Ext}^{d-i}_R(M, R), E)$.
For $M = R$ and $i = d$ it gives $H^d_{\mathfrak{m}}(R) \cong \Hom_R(\omega_R, E)$.
Example: for $R = K[\![x]\!]$, one has $d = 1$, $\omega_R = R$ and $E = K[\![x]\!]_x / K[\![x]\!]$, and indeed $H^1_{\mathfrak{m}}(R) = R_x / R \cong E = \Hom_R(R, E)$.
When $R$ is complete, [[Matlis duality|2V9BR5XX6A]] turns the formula around: $\operatorname{Ext}^{d-i}_R(M, \omega_R) \cong \Hom_R(H^i_{\mathfrak{m}}(M), E)$.

## Explanations

### L1 human

Local cohomology modules are large and hard to see directly.
Local duality says that they are the duals of Ext modules, which are finitely generated and computable.
It is an algebraic analogue of Serre duality for projective varieties.

### L2 human

Combined with the vanishing pattern of local cohomology, local duality shows that $M$ is Cohen–Macaulay of dimension $t$ exactly when $\operatorname{Ext}^{d-i}_R(M, \omega_R) = 0$ for all $i \ne t$.
It also identifies the canonical module as the Matlis dual of the top local cohomology $H^d_{\mathfrak{m}}(R)$ when $R$ is complete.
