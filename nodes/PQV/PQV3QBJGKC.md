---
tag: PQV3QBJGKC
kind: definition
name: Fractional viscoelastic models
msc: [74D05, 74S40, 26A33]
defines: 193HK5AMVK
uses: [GCX1B3DAJN, JSSYGY0V87, T73XK15SA2, JTKCZ44NN3, 12G9M694YG, 0V49JEZW06]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_calculus
---

## Definition

Let $0 < \alpha < 1$, and for a function $f$ on $[0, \infty)$ let
$$D^\alpha f(t) = \frac{1}{\Gamma(1 - \alpha)} \frac{d}{dt} \int_0^t (t - s)^{-\alpha} f(s) \, ds$$
be its Riemann–Liouville derivative of order $\alpha$.
It is the derivative of the [[Riemann–Liouville integral|JTKCZ44NN3]] of $f$ of order $1 - \alpha$.
Consider strain and stress histories $\varepsilon$, $\sigma$ that vanish for $t < 0$.
A *springpot* (or Scott Blair element) with modulus $E > 0$ and time constant $\tau > 0$ is the law
$$\sigma(t) = E \tau^\alpha D^\alpha \varepsilon(t).$$
A *fractional viscoelastic model* is a linear [[viscoelastic|GCX1B3DAJN]] constitutive law built from springs, dashpots and springpots.
Equivalently, it is a linear relation with constant coefficients between $\sigma$, $\varepsilon$ and their fractional derivatives of orders in $[0, 1]$.

## Remarks

Example: for the springpot, the strain step $\varepsilon = \varepsilon_0 H(t)$ has $D^\alpha H(t) = t^{-\alpha}/\Gamma(1 - \alpha)$, so the [[relaxation modulus|JSSYGY0V87]] is the power law
$$G(t) = \frac{E}{\Gamma(1 - \alpha)} \left(\frac{t}{\tau}\right)^{-\alpha}.$$
The limits $\alpha \to 0$ and $\alpha \to 1$ recover a spring and a dashpot of viscosity $E\tau$.
Example: the fractional Maxwell model is a spring of modulus $E$ in series with a springpot of modulus $E$ and time $\tau$.
It satisfies $D^\alpha \varepsilon = D^\alpha \sigma / E + \sigma / (E \tau^\alpha)$.
By the [[Laplace transform|0V49JEZW06]] its relaxation modulus is $G(t) = E \, E_\alpha(-(t/\tau)^\alpha)$, where $E_\alpha$ is the [[Mittag-Leffler function|12G9M694YG]].
Non-example: the law $\sigma = E \varepsilon + c \varepsilon^2$ with $c \neq 0$ contains no derivatives of non-integer order and is not linear, so it is not a fractional viscoelastic model.
For histories with $\varepsilon(0) = 0$ the Riemann–Liouville and Caputo derivatives of order $\alpha \in (0, 1)$ agree, so either can be used.
