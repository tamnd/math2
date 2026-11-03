---
tag: G1D2MFDZN6
kind: definition
name: Lead–lag compensator
msc: [93B51, 93C80]
defines: E15NAJRK3M
uses: [86JKV3TRFD, NSGTEGWZY0, BMY8QZSD9H]
sources:
  - url: https://en.wikipedia.org/wiki/Lead%E2%80%93lag_compensator
---

## Definition

Let $k > 0$, and let $z, p > 0$ be real numbers.
A *lead compensator* is a controller with [[transfer function|86JKV3TRFD]] $C(s) = k \dfrac{s + z}{s + p}$ with $0 < z < p$.
A *lag compensator* has the same form with $0 < p < z$.
A *lead–lag compensator* is a product
$$C(s) = k \, \frac{s + z_1}{s + p_1} \cdot \frac{s + z_2}{s + p_2}, \qquad 0 < z_1 < p_1, \quad 0 < p_2 < z_2,$$
of a lead factor and a lag factor.

## Remarks

The [[zeros and poles|NSGTEGWZY0]] of a lead factor lie at $-z$ and $-p$ on the negative real axis, with the zero closer to the origin.
At a frequency $\omega > 0$, the phase of $(i\omega + z)/(i\omega + p)$ is $\arctan(\omega / z) - \arctan(\omega / p)$, which is positive for a lead factor and negative for a lag factor.
For a lead factor, the largest phase is reached at $\omega = \sqrt{zp}$, and its value $\varphi_{\max}$ satisfies $\sin \varphi_{\max} = (p - z)/(p + z)$.

Example: $z = 1$, $p = 3$ gives a lead compensator.
At $\omega = \sqrt{3}$ its phase is $\arctan \sqrt{3} - \arctan(1/\sqrt{3}) = 60^\circ - 30^\circ = 30^\circ$, and indeed $\sin 30^\circ = 1/2 = (3 - 1)/(3 + 1)$.

Non-example: $C(s) = (s - 1)/(s + 3)$ is not a lead or lag compensator, because $z = -1$ is not positive; its zero at $s = 1$ lies in the right half-plane.

Lead–lag compensators are often written $k \dfrac{1 + \alpha T s}{1 + T s}$ with $T > 0$, which is a lead factor for $\alpha > 1$ and a lag factor for $0 < \alpha < 1$; their effect is read off the [[frequency response|BMY8QZSD9H]].
