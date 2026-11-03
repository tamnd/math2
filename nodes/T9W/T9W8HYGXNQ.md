---
tag: T9W8HYGXNQ
kind: definition
name: Surface plasmon polariton
msc: [78A40, 78A25]
defines: 47WEKV7FJ6
uses: [9BWWD4QK8Y, F768YN0P2V, VT8YK4WC0H, EZG8N3H7QN]
sources:
  - url: https://en.wikipedia.org/wiki/Surface_plasmon_polariton
---

## Definition

Let the plane $z = 0$ separate a non-magnetic dielectric in $z > 0$ from a non-magnetic metal in $z < 0$.
At the angular frequency $\omega$, let their relative [[permittivities|F768YN0P2V]] be the real numbers $\varepsilon_d > 0$ and $\varepsilon_m$.
Let $k_0 = \omega / c$, where $c$ is the speed of light in vacuum.
A *surface plasmon polariton* is a nonzero solution of the source-free [[Maxwell's equations|9BWWD4QK8Y]] with time factor $e^{-i\omega t}$ such that:

1. it is transverse magnetic: $\mathbf{H} = H_y(z) \, e^{i\beta x} \, \hat{\mathbf{y}}$ for a real $\beta > 0$;
2. it decays exponentially away from the interface on both sides, as $e^{-\kappa_d z}$ for $z > 0$ and $e^{\kappa_m z}$ for $z < 0$, with $\kappa_d, \kappa_m > 0$;
3. it satisfies the [[interface conditions|EZG8N3H7QN]] at $z = 0$.

Such a solution exists exactly when $\varepsilon_m < -\varepsilon_d$, and then
$$\beta = k_0 \sqrt{\frac{\varepsilon_m \varepsilon_d}{\varepsilon_m + \varepsilon_d}}.$$

## Remarks

Check: each half has $\kappa_j^2 = \beta^2 - \varepsilon_j k_0^2$, and continuity of $H_y$ and of $E_x$ gives $\kappa_d / \varepsilon_d + \kappa_m / \varepsilon_m = 0$.
With $\kappa_d, \kappa_m > 0$ this forces $\varepsilon_m < 0$, and squaring and solving gives the formula for $\beta$, which is real and larger than $\sqrt{\varepsilon_d}\, k_0$ exactly when $\varepsilon_m + \varepsilon_d < 0$.
So on each side the wave is an [[evanescent field|VT8YK4WC0H]].
Example: a metal in the [[Drude model|5Y1CZ2CFPN]] with $\varepsilon_m = 1 - \omega_p^2/\omega^2$ against vacuum ($\varepsilon_d = 1$) supports the wave for $\omega < \omega_p / \sqrt{2}$.
Non-example: a transverse electric field ($\mathbf{E}$ along $\hat{\mathbf{y}}$) cannot be bound to such an interface, because continuity of $E_y$ and of its normal derivative would need $\kappa_d + \kappa_m = 0$.
For real metals $\varepsilon_m$ has an imaginary part, $\beta$ becomes complex, and the wave decays along the surface too.
