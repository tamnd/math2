---
tag: KJ6AAHKJ91
kind: statement
role: proposition
name: Boltzmann superposition principle
msc: [74D05]
uses: [GCX1B3DAJN, JSSYGY0V87, 2Z29JN3VES, 0V49JEZW06, PQ8Z5HS2JR]
about: [GCX1B3DAJN, JSSYGY0V87]
sources:
  - url: https://en.wikipedia.org/wiki/Viscoelasticity
---

## Statement

Let a material be linear [[viscoelastic|GCX1B3DAJN]] with [[relaxation modulus|JSSYGY0V87]] $G$.
So its stress response is linear in the strain history and invariant under shifts of time.
Assume also that the response is continuous under uniform convergence of strain histories, and that $G$ is continuous on $[0, \infty)$.
Let the strain history $\varepsilon$ vanish for $t < 0$ and be continuously differentiable on $(0, \infty)$, with a possible jump to $\varepsilon(0^+)$ at $t = 0$.
Then the stress at every time $t > 0$ is
$$\sigma(t) = G(t) \, \varepsilon(0^+) + \int_0^t G(t - s) \, \dot\varepsilon(s) \, ds.$$

## Remarks

The idea is to approximate the strain history by a staircase of small steps $\Delta\varepsilon_i$ at times $s_i$.
By time invariance each step produces the stress $G(t - s_i) \Delta\varepsilon_i$, and by linearity the stresses of all steps add up.
Letting the steps become small turns the sum into the integral, a [[convolution|2Z29JN3VES]] of $G$ with $\dot\varepsilon$.
Example: for a [[Maxwell material|PQ8Z5HS2JR]] with $G(t) = E e^{-t/\tau}$ and a constant strain rate $\dot\varepsilon = r$ from $\varepsilon(0) = 0$, the formula gives $\sigma(t) = E r \tau (1 - e^{-t/\tau})$, which tends to the viscous value $\eta r$ with $\eta = E\tau$.
The symmetric form $\varepsilon(t) = J(t) \sigma(0^+) + \int_0^t J(t - s) \dot\sigma(s) \, ds$ holds with the creep compliance $J$.
In physics the principle is often taken as the definition of linear viscoelasticity; it fails for nonlinear materials and for aging materials such as young concrete.

## Explanations

### L1 human

Each strain you put into a viscoelastic material leaves a stress that fades with time.
Boltzmann's principle says that these fading stresses simply add up.
So once you know how the material answers one sudden step, you know how it answers any loading history.

### L2 human

The principle turns the constitutive law into a convolution, so that the [[Laplace transform|0V49JEZW06]] changes it into the algebraic relation $\hat\sigma(s) = s \hat G(s) \hat\varepsilon(s)$.
This is the basis of the correspondence principle and of the complex modulus used in oscillatory tests.
Spring–dashpot models, whose relaxation moduli are Prony series, are special cases.
