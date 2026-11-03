---
tag: EGE0E3QXYG
kind: example
name: Mooney–Rivlin solid
msc: [74B20]
instance_of: [ZHK2EVRD90]
uses: [3E9K1DRNYN, N5G8WNQFC3]
sources:
  - url: https://en.wikipedia.org/wiki/Mooney–Rivlin_solid
same_as:
  wikidata: Q6907763
  wikipedia: Mooney–Rivlin solid
---

## Example

The incompressible *Mooney–Rivlin solid* is the [[hyperelastic material|ZHK2EVRD90]] with [[strain energy density function|3E9K1DRNYN]]
$$W = C_{10}(I_1 - 3) + C_{01}(I_2 - 3),$$
subject to $\det F = 1$.
Here $F$ is the deformation gradient, $C = F^T F$ is the right [[Cauchy–Green tensor|N5G8WNQFC3]], $I_1 = \tr C$ and $I_2 = \tfrac12\left((\tr C)^2 - \tr(C^2)\right)$, and $C_{10}, C_{01}$ are material constants.
Check that it is hyperelastic: $W$ is a differentiable function of $F$ through $C$, so the stress $P = \partial W / \partial F - pF^{-T}$ is defined by a stored energy.
At $F = I$ one has $I_1 = I_2 = 3$, so $W(I) = 0$.
Linearising at $F = I$ gives the shear modulus $\mu = 2(C_{10} + C_{01})$.
With $C_{01} = 0$ it reduces to the [[neo-Hookean solid|WABEBSH4Z4]].
In terms of the principal stretches, $I_1 = \lambda_1^2 + \lambda_2^2 + \lambda_3^2$ and, when $\lambda_1\lambda_2\lambda_3 = 1$, $I_2 = \lambda_1^{-2} + \lambda_2^{-2} + \lambda_3^{-2}$.

## Explanations

### L1 human

The Mooney–Rivlin model adds a second term to the neo-Hookean energy of rubber.
The new term depends on how areas, rather than lengths, are stretched.
The two constants can be fitted to experiments, and the model fits rubber better than the neo-Hookean one at moderate stretches.
