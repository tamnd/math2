---
tag: XVNSQHGFFR
kind: definition
name: Proper time
msc: [83A05, 53B30]
defines: YG74WHC3S9
uses: [G49G4R1K04, Z788G6MJ9E, PNEFDF4Z03]
sources:
  - url: https://en.wikipedia.org/wiki/Proper_time
---

## Definition

Let $M$ be [[Minkowski space|G49G4R1K04]] with metric $\eta$ of signature $(-, +, +, +)$, and let $c > 0$ be the speed of light.
Let $\sigma \colon [a, b] \to M$ be a smooth parametrisation of a timelike [[world line|Z788G6MJ9E]].
The *proper time* along $\sigma$ from $\sigma(a)$ to $\sigma(b)$ is
$$\Delta\tau = \frac{1}{c} \int_a^b \sqrt{-\eta(\sigma'(s), \sigma'(s))} \, ds.$$
In an inertial frame, with the world line written as $t \mapsto (ct, \mathbf{x}(t))$ for $t \in [t_1, t_2]$ and velocity $\mathbf{v}(t) = d\mathbf{x}/dt$, this is
$$\Delta\tau = \int_{t_1}^{t_2} \sqrt{1 - \frac{\abs{\mathbf{v}(t)}^2}{c^2}} \, dt.$$

## Remarks

Example: for the straight world line $\sigma(t) = (ct, vt, 0, 0)$ with $v = 0.6 c$ and $t \in [0, 10]$, $\Delta\tau = \int_0^{10} \sqrt{1 - 0.36} \, dt = 8$.
For a straight world line from $p$ to $q$, $\Delta\tau = \sqrt{-s^2}/c$, where $s^2$ is the [[spacetime interval|PNEFDF4Z03]] between $p$ and $q$.
Non-example: for the spacelike curve $\sigma(s) = (0, s, 0, 0)$ the integrand $\sqrt{-\eta(\sigma', \sigma')} = \sqrt{-1}$ is not real, so proper time is not defined; such curves have a proper length instead.
Proper time does not depend on the parametrisation, by the change of variables formula, and it is invariant under Poincaré transformations.
Along a null world line the same integral is $0$.
