---
tag: EEJR84RYFR
kind: example
name: Standard linear solid model
msc: [74D05]
instance_of: [GCX1B3DAJN]
uses: [PQ8Z5HS2JR, JSSYGY0V87, YFTQJ7VY31]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_linear_solid_model
same_as:
  wikidata: Q4118814
  wikipedia: Standard linear solid model
---

## Example

The *standard linear solid*, also called the Zener model, is a spring of modulus $E_\infty > 0$ in parallel with a [[Maxwell material|PQ8Z5HS2JR]] arm.
The arm consists of a spring of modulus $E_1 > 0$ and a dashpot of viscosity $\eta > 0$ in series.
Write $\sigma = E_\infty \varepsilon + \sigma_1$, where the arm stress satisfies $\dot\varepsilon = \dot\sigma_1 / E_1 + \sigma_1 / \eta$.
Eliminating $\sigma_1$ gives
$$\sigma + \frac{\eta}{E_1} \dot\sigma = E_\infty \varepsilon + \frac{\eta (E_\infty + E_1)}{E_1} \dot\varepsilon.$$
Relaxation: a strain step $\varepsilon_0$ gives $\sigma_1(t) = E_1 \varepsilon_0 e^{-t/\tau}$ with $\tau = \eta/E_1$, so the [[relaxation modulus|JSSYGY0V87]] is
$$G(t) = E_\infty + E_1 e^{-t/\tau}.$$
[[Creep|YFTQJ7VY31]]: a stress step $\sigma_0$ gives $\varepsilon(0^+) = \sigma_0 / (E_\infty + E_1)$, then the first-order equation $E_\infty \varepsilon + \frac{\eta (E_\infty + E_1)}{E_1} \dot\varepsilon = \sigma_0$, so $\varepsilon$ rises exponentially to $\sigma_0 / E_\infty$ with time constant $\eta (E_\infty + E_1)/(E_1 E_\infty)$.

## Remarks

It is the simplest spring–dashpot model that shows both an instantaneous elastic response and bounded creep, and both partial relaxation and a nonzero equilibrium modulus $E_\infty$.
For $E_\infty = 0$ it reduces to the Maxwell material.

## Explanations

### L1 human

The Maxwell model forgets its shape completely, and the Kelvin–Voigt model cannot respond instantly.
Adding one extra spring fixes both problems.
The standard linear solid responds at once when loaded, then creeps a little further, and finally settles at a fixed stretch.
Many solid polymers behave roughly in this way.
