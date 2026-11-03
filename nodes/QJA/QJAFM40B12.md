---
tag: QJAFM40B12
kind: definition
name: Strain energy density function
msc: [74B20]
defines: 3E9K1DRNYN
uses: [DV71K7X1JD, HTYRR2WDQ6, Q1MD7W6CT3]
sources:
  - url: https://en.wikipedia.org/wiki/Strain_energy_density_function
---

## Definition

Let $\mathrm{M}^3_+$ be the set of real $3 \times 3$ matrices with positive determinant.
Let a homogeneous [[Cauchy elastic material|DV71K7X1JD]] have the first [[Piola–Kirchhoff stress|Q1MD7W6CT3]] $P = \hat{P}(F)$ as a function of the [[deformation gradient|HTYRR2WDQ6]] $F \in \mathrm{M}^3_+$.
A *strain energy density function* of the material is a differentiable function $W \colon \mathrm{M}^3_+ \to \R$ such that
$$\hat{P}(F) = \frac{\partial W}{\partial F}(F) \quad \text{for all } F \in \mathrm{M}^3_+,$$
that is, $\hat P_{iJ} = \partial W / \partial F_{iJ}$.

## Remarks

$W$ is the stored energy per unit volume of the reference configuration, and it is unique up to an additive constant, usually fixed by $W(I) = 0$.
Frame-indifference of the material holds if $W(QF) = W(F)$ for all rotations $Q$; then $W$ depends on $F$ only through $C = F^T F$, and the second Piola–Kirchhoff stress is $S = 2 \, \partial W / \partial C$.
Example: $W(F) = \frac{\mu}{2}(\tr(F^T F) - 3)$ gives $\hat{P}(F) = \mu F$.
Non-example: fix a nonzero antisymmetric matrix $A$ and let $\hat{P}(F) = \mu F + A F$.
Its derivative is the linear map $H \mapsto \mu H + AH$, and $\tr((AH)^T K) = -\tr(H^T A K)$, so this map is not symmetric for the inner product $\tr(H^T K)$.
The second derivative of a function $W$ is always symmetric, so no strain energy density function exists for this response.
In linear elasticity the strain energy density is $W = \tfrac12 \varepsilon : C : \varepsilon$, with $\varepsilon$ the small strain and $C$ the elasticity tensor.

## Explanations

### L1 human

It is a scalar energy function whose slope with respect to the deformation is the stress.
Knowing the energy for every deformation means knowing the whole elastic behaviour.
