---
tag: TWP1EP7FR1
kind: definition
name: Étale fundamental group
msc: [14F35, "14E20"]
defines: KJ11DAXMR0
uses: [5A35TYZD02, H84VHC8PX2, N9C4X7XKE4, VABPHNZAVV, DPFMXS71D1, 218WAD58W3]
sources:
  - url: https://en.wikipedia.org/wiki/%C3%89tale_fundamental_group
---

## Definition

Let $X$ be a connected [[scheme|5A35TYZD02]] and let $\bar{x} \colon \operatorname{Spec} \Omega \to X$ be a geometric point, with $\Omega$ an algebraically closed field.
A *finite étale cover* of $X$ is a morphism $Y \to X$ that is [[finite|N9C4X7XKE4]] and [[étale|H84VHC8PX2]].
Let $\mathrm{FEt}_X$ be the category of finite étale covers of $X$, with morphisms over $X$.
The *fiber functor* $F_{\bar{x}} \colon \mathrm{FEt}_X \to \mathrm{Set}$ sends $Y$ to the finite set of geometric points of $Y$ over $\bar{x}$, that is, of morphisms $\operatorname{Spec} \Omega \to Y$ that lift $\bar{x}$.
The *étale fundamental group* is the automorphism group of this functor:
$$\pi_1^{\text{ét}}(X, \bar{x}) = \Aut(F_{\bar{x}}).$$

## Remarks

The group $\pi_1^{\text{ét}}(X, \bar{x})$ is a [[profinite group|VABPHNZAVV]], as a closed subgroup of $\prod_Y \operatorname{Sym}(F_{\bar{x}}(Y))$.
By [[Grothendieck's Galois theory|218WAD58W3]], $F_{\bar{x}}$ is an equivalence between $\mathrm{FEt}_X$ and the category of finite sets with a continuous action of $\pi_1^{\text{ét}}(X, \bar{x})$.
Example: for $X = \operatorname{Spec} k$ with $k$ a field, the finite étale covers are finite products of finite separable extensions of $k$.
Choosing $\bar{x}$ amounts to choosing a separable closure $k^{s}$, and $\pi_1^{\text{ét}}(X, \bar{x}) \cong \Gal(k^{s}/k)$, the [[absolute Galois group|DPFMXS71D1]].
Non-example: the exponential map $\C \to \C^{*}$ is a covering space with infinitely many sheets, so it is not a finite étale cover and does not enter $\mathrm{FEt}_X$.
Therefore $\pi_1^{\text{ét}}$ of the complex punctured line is $\widehat{\Z}$, the profinite completion of the topological fundamental group $\Z$, and not $\Z$ itself.
For a variety $X$ over $\C$, the Riemann existence theorem gives $\pi_1^{\text{ét}}(X) \cong \widehat{\pi_1(X(\C))}$.
In characteristic $p > 0$ the affine line has nontrivial finite étale covers, such as the Artin–Schreier covers $y^p - y = x$.
