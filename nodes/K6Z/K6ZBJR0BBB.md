---
tag: K6ZBJR0BBB
kind: definition
name: Q factor
msc: [70J30, 70J35]
defines: NSJ6GVVP16
uses: [99PP8V3619, 0RNXVVTJTJ]
sources:
  - url: https://en.wikipedia.org/wiki/Q_factor
---

## Definition

Let $m > 0$, $k > 0$ and $c > 0$, and consider the [[damped harmonic oscillator|0RNXVVTJTJ]] $m \ddot x + c \dot x + k x = 0$, with natural frequency $\omega_0 = \sqrt{k/m}$ and [[damping ratio|99PP8V3619]] $\zeta = c / (2 \sqrt{m k})$.
Its *Q factor* is
$$Q = \frac{\sqrt{m k}}{c} = \frac{m \omega_0}{c} = \frac{1}{2 \zeta}.$$

## Remarks

The oscillator is underdamped exactly when $Q > 1/2$.
The averaged energy decays like $e^{-\omega_0 t / Q}$, since the amplitude decays like $e^{-\zeta \omega_0 t}$.
For large $Q$, the energy lost in one cycle is close to $2\pi/Q$ times the stored energy, and the resonance peak of the forced oscillator has width about $\omega_0 / Q$.
These approximate forms are often used as the definition in physics and engineering.

Example: $m = 1$, $k = 4$, $c = 0.4$ gives $\omega_0 = 2$ and $Q = 2 / 0.4 = 5$.

Non-example: for $c = 0$ the formula divides by zero; the undamped oscillator has no finite Q factor, and one says informally that $Q = \infty$.
