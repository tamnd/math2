---
tag: NBR81PR7E5
kind: concept
name: Tomita–Takesaki theory
msc: [46L10, 46L40]
sources:
  - url: https://en.wikipedia.org/wiki/Tomita–Takesaki_theory
same_as:
  wikidata: Q7818977
  wikipedia: Tomita–Takesaki theory
---

## Summary

Tomita–Takesaki theory starts from a [[von Neumann algebra|PSFWQVZ0FS]] with a cyclic and separating vector.
It attaches to it a positive self-adjoint modular operator $\Delta$ and an antiunitary modular conjugation $J$.
Its main theorem says that $J$ turns the algebra into its [[commutant|1VC7EJ1ZBZ]].
It also says that the unitaries $\Delta^{it}$ give a one-parameter group of automorphisms, the modular automorphism group.
So every faithful normal state comes with a natural time evolution.
The theory is the basis of Connes' classification of type $\mathrm{III}$ factors and of the use of KMS states in quantum statistical mechanics.

## Explanations

### L1 human

For a trace, the order of a product does not matter: $\tau(xy) = \tau(yx)$.
Most states are not traces, and Tomita–Takesaki theory measures exactly how far a state is from being one.
The answer is a flow $\sigma_t$ of automorphisms of the algebra that repairs the order of a product.
For a matrix algebra with the state $\varphi(x) = \operatorname{tr}(\rho x)$ given by an invertible density matrix $\rho$, this flow is $\sigma_t(x) = \rho^{it} x \rho^{-it}$.
Then $\varphi(xy) = \varphi(y \, \rho x \rho^{-1})$, so moving $x$ to the other side costs the twist $x \mapsto \rho x \rho^{-1}$.
For a trace, $\rho$ is a multiple of the identity and the flow does nothing.
