---
tag: N09E4TZJNQ
kind: example
name: Ogden hyperelastic model
msc: [74B20]
instance_of: [ZHK2EVRD90]
uses: [3E9K1DRNYN]
sources:
  - url: https://en.wikipedia.org/wiki/Ogden_hyperelastic_model
same_as:
  wikidata: Q7079901
  wikipedia: Ogden hyperelastic model
---

## Example

The incompressible *Ogden model* is the isotropic [[hyperelastic material|ZHK2EVRD90]] whose [[strain energy density function|3E9K1DRNYN]] is
$$W = \sum_{p=1}^{N} \frac{\mu_p}{\alpha_p}\left(\lambda_1^{\alpha_p} + \lambda_2^{\alpha_p} + \lambda_3^{\alpha_p} - 3\right),$$
subject to $\lambda_1 \lambda_2 \lambda_3 = 1$.
Here $\lambda_1, \lambda_2, \lambda_3$ are the principal stretches, the square roots of the eigenvalues of $F^T F$, and $N \ge 1$, $\mu_p$, $\alpha_p \ne 0$ are material constants.
$W$ is a symmetric function of the principal stretches, so it defines an isotropic stored energy, and $W = 0$ when all stretches are $1$.
The shear modulus at small strain is $\mu = \tfrac12 \sum_p \mu_p \alpha_p$.
Check of two special cases: $N = 1$, $\alpha_1 = 2$ gives $\frac{\mu_1}{2}(I_1 - 3)$, the [[neo-Hookean solid|WABEBSH4Z4]].
$N = 2$, $\alpha_1 = 2$, $\alpha_2 = -2$ gives the [[Mooney–Rivlin solid|EGE0E3QXYG]], because $\lambda_1^{-2} + \lambda_2^{-2} + \lambda_3^{-2} = I_2$ when $\lambda_1\lambda_2\lambda_3 = 1$.

## Explanations

### L1 human

The Ogden model writes the energy of rubber as a sum of powers of the principal stretches.
The powers need not be whole numbers, and with two or three terms the model fits test data on rubber up to very large stretches.
Simpler models such as the neo-Hookean and Mooney–Rivlin ones are special cases.
