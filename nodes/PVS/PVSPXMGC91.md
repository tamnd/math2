---
tag: PVSPXMGC91
kind: definition
name: Relaxation modulus
msc: [74D05]
defines: JSSYGY0V87
uses: [GCX1B3DAJN, 09C4JP7Y0M, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Stress_relaxation
---

## Definition

Consider a linear [[viscoelastic|GCX1B3DAJN]] material in a one-dimensional test, such as uniaxial tension or simple shear.
Apply the strain history $\varepsilon(t) = \varepsilon_0 H(t)$, where $H$ is the [[Heaviside step function|09C4JP7Y0M]] and $\varepsilon_0 \neq 0$ is a constant.
The resulting stress has the form $\sigma(t) = \varepsilon_0 G(t)$ for $t > 0$, with a function $G$ that does not depend on $\varepsilon_0$.
This function $G \colon (0, \infty) \to \R$ is the *relaxation modulus* of the material.

## Remarks

Example: for the law $\dot\varepsilon = \dot\sigma / E + \sigma / \eta$ of a spring and a dashpot in series, the step gives $\sigma(0^+) = E \varepsilon_0$ and then $\dot\sigma = -\sigma E / \eta$, so $G(t) = E e^{-t/\tau}$ with $\tau = \eta / E$.
Non-example: for a nonlinear law such as $\sigma = E \varepsilon + c \varepsilon^3$ with $c \neq 0$, the ratio $\sigma(t)/\varepsilon_0$ depends on $\varepsilon_0$, so no relaxation modulus exists.
The *creep compliance* $J(t)$ is defined in the same way from a stress step $\sigma(t) = \sigma_0 H(t)$, by $\varepsilon(t) = \sigma_0 J(t)$.
The two functions are linked through the [[Laplace transform|0V49JEZW06]] by $\hat G(s) \hat J(s) = 1/s^2$, or equivalently $\int_0^t G(t - u) J(u) \, du = t$ for $t > 0$.
