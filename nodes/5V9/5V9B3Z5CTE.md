---
tag: 5V9B3Z5CTE
kind: definition
name: Eshelby energy-momentum tensor
msc: [74A45, 74B20, 74R10]
defines: Q94SK7PRN9
uses: [ZHK2EVRD90, 3E9K1DRNYN, HTYRR2WDQ6, Q1MD7W6CT3]
sources:
  - url: https://en.wikipedia.org/wiki/Configurational_mechanics
---

## Definition

Let a body with reference configuration $\Omega \subset \R^3$ be made of a [[hyperelastic material|ZHK2EVRD90]] with [[strain energy density|3E9K1DRNYN]] $W(X, F)$ per unit reference volume.
Let $y \colon \Omega \to \R^3$ be a deformation with [[deformation gradient|HTYRR2WDQ6]] $F = \nabla y$, and let $P = \partial W / \partial F$ be the first [[Piola–Kirchhoff stress|Q1MD7W6CT3]].
The *Eshelby energy-momentum tensor* is the field
$$b = W(X, F) \, I - F^T P,$$
with components $b_{KL} = W \delta_{KL} - F_{iK} P_{iL}$.
In linear elasticity with displacement $u$, strain energy density $W(\varepsilon)$ and Cauchy stress $\sigma$, the corresponding tensor is $b_{kl} = W \delta_{kl} - u_{i,k} \sigma_{il}$.

## Remarks

If $y$ is a smooth equilibrium deformation without body forces, so that $\operatorname{Div} P = 0$, then $\operatorname{Div} b = \partial W / \partial X$ at fixed $F$.
Check: by the chain rule, $\partial_L (W \delta_{KL}) = \partial W/\partial X_K + P_{iL} \, \partial_K F_{iL}$, and, by $\operatorname{Div} P = 0$, $\partial_L (F_{iK} P_{iL}) = \partial_L F_{iK} \, P_{iL}$, and these two second terms agree because $\partial_K F_{iL} = \partial_L F_{iK} = \partial_K \partial_L y_i$.
Hence $b$ is divergence-free in a homogeneous material, where $W$ does not depend on $X$.
Example: for a uniform deformation $F$ of a homogeneous body, $b$ is constant, so each of its partial derivatives is zero and $\operatorname{Div} b = 0$.
Non-example: the Cauchy stress $\sigma$ itself is divergence-free at equilibrium, but it is not an energy-momentum tensor: its flux gives the force on the material, not on a defect.

## Explanations

### L1 human

The Eshelby tensor is the energy density times the identity minus the deformation gradient transpose times the stress.
In a uniform material its divergence is zero, and its flux around a defect gives the force that pushes the defect.
