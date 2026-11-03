---
tag: Q50BRXPJDT
kind: definition
name: Saffman–Taylor instability
msc: ["76E17", 76D27, 76S05]
defines: 3Y7MA0VS2J
uses: [CM1R6CSHAA, NM5Q4845Z4, DX8RV2XG6H]
sources:
  - url: https://en.wikipedia.org/wiki/Saffman%E2%80%93Taylor_instability
---

## Definition

Consider a [[Hele-Shaw cell|CM1R6CSHAA]] with gap $b > 0$, in which the gap-averaged velocity of each fluid obeys $\bar u = -\frac{b^2}{12\mu}\nabla p$, without gravity.
Fluid 1, of [[viscosity|NM5Q4845Z4]] $\mu_1$, occupies $x < Ut$ and displaces fluid 2, of viscosity $\mu_2$, which occupies $x > Ut$.
The flat interface moves with speed $U > 0$ and has surface tension $\gamma \ge 0$.
For a perturbation of the interface of the form $x = Ut + \varepsilon e^{iky + st}$, with wavenumber $k > 0$, linear stability analysis gives the growth rate
$$s(k) = \frac{k}{\mu_1 + \mu_2}\left((\mu_2 - \mu_1)U - \frac{b^2\gamma}{12}k^2\right).$$
The *Saffman–Taylor instability* is the growth of such perturbations, which occurs for the wavenumbers with $s(k) > 0$.
It occurs for some $k$ if and only if $\mu_1 < \mu_2$, that is when the less viscous fluid displaces the more viscous one.

## Remarks

Example: air ($\mu_1 \approx 0$) displacing glycerine ($\mu_2 > 0$) at speed $U$ gives $s(k) > 0$ for $0 < k < k_c = \sqrt{12\mu_2U/(b^2\gamma)}$, so long waves grow and short waves are damped by surface tension.
The fastest growing wavenumber is $k_c/\sqrt{3}$, which sets the initial spacing of the fingers.
Non-example: when the more viscous fluid displaces the less viscous one, $\mu_1 > \mu_2$, then $s(k) < 0$ for every $k > 0$, and the flat interface is stable.
Without surface tension, $\gamma = 0$ and $\mu_1 < \mu_2$, the growth rate is proportional to $k$, so arbitrarily short waves grow arbitrarily fast and the linear problem is ill-posed.
The same analysis applies to flow in a porous medium governed by [[Darcy's law|DX8RV2XG6H]], with $b^2/12$ replaced by the permeability.
