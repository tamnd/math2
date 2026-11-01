---
tag: QH84JHCQMY
kind: definition
name: Picard group of a ring
msc: [13C20, 13C10, 14C22]
defines: DZW58R6T2Q
uses: [0310REJJY8, BFFA03GE3V, F0HQXQ0HCD, 0PV74TR5FP, X6JD4AG973, 05QY1VEBYD]
sources:
  - url: https://en.wikipedia.org/wiki/Picard_group
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]].
An $R$-module $P$ is *invertible* if $P$ is a [[finitely generated|05QY1VEBYD]] [[projective module|BFFA03GE3V]] of rank one.
This means that for every [[maximal ideal|0PV74TR5FP]] $\mathfrak{m}$ of $R$, the [[localization|X6JD4AG973]] $P_{\mathfrak{m}}$ is isomorphic to $R_{\mathfrak{m}}$.
The *Picard group* $\operatorname{Pic}(R)$ is the set of isomorphism classes $[P]$ of invertible $R$-modules, with the operation
$$[P] \cdot [Q] = [P \otimes_R Q],$$
where $\otimes_R$ is the [[tensor product|F0HQXQ0HCD]].
The identity element is $[R]$, and the inverse of $[P]$ is $[\Hom_R(P, R)]$.

## Remarks

The operation is well defined, associative and commutative because the tensor product is so up to natural isomorphism.
For invertible $P$, the evaluation map $P \otimes_R \Hom_R(P, R) \to R$ is an isomorphism, since it is one after localization at every maximal ideal.
An $R$-module $P$ is invertible exactly when there is a module $Q$ with $P \otimes_R Q \cong R$.
If $R$ is an integral domain, $\operatorname{Pic}(R)$ is isomorphic to the group of [[invertible fractional ideals|E190TAV2S6]] modulo the principal fractional ideals.

Example: for $R = \Z[\sqrt{-5}]$, the ideal $P = (2, 1 + \sqrt{-5})$ is an invertible module that is not free, while $P \otimes_R P \cong P^2 = (2) \cong R$; in fact $\operatorname{Pic}(R)$ has order $2$.
If $R$ is a [[principal ideal domain|0CMD0BCH8T]] or a [[local ring|MZ02BKPHJA]], then $\operatorname{Pic}(R)$ is trivial.

Non-example: the module $R^2$ is finitely generated and projective, but $(R^2)_{\mathfrak{m}} \cong R_{\mathfrak{m}}^2$ is not isomorphic to $R_{\mathfrak{m}}$ for $R \ne 0$; so $R^2$ is not invertible and has no class in $\operatorname{Pic}(R)$.
