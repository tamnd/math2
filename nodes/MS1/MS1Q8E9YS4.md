---
tag: MS1Q8E9YS4
kind: definition
name: Mixing length theory
msc: [85A15, 85A30]
defines: HWPBFFHQ2Y
uses: [85GWQPTJ3W, 4FC5XQA2RK]
sources:
  - url: https://en.wikipedia.org/wiki/Mixing_length_model
---

## Definition

Consider a convective layer of a star in [[hydrostatic equilibrium|4FC5XQA2RK]].
Let $P$, $\rho$ and $T$ be its pressure, density and temperature, $g$ the local gravity and $c_P$ the specific heat at constant pressure.
Let $H_P = P / (\rho g)$ be the pressure scale height and $\delta = -(\partial \ln \rho / \partial \ln T)_P$.
Let $\nabla = d \ln T / d \ln P$ be the gradient of the surroundings and $\nabla_e$ the gradient followed by a moving blob, with $\nabla > \nabla_e$.
*Mixing length theory* with parameter $\alpha > 0$ models convection by blobs that travel a mean distance $\ell = \alpha H_P$ before they dissolve.
The distance $\ell$ is the *mixing length*, and the theory sets, as averages over the blobs:

1. the temperature excess of a blob, $\Delta T / T = (\nabla - \nabla_e) \, \ell / (2 H_P)$;
2. the blob speed, $v^2 = g \delta (\nabla - \nabla_e) \, \ell^2 / (8 H_P)$;
3. the convective flux, $F_{\mathrm{conv}} = \rho c_P v \, \Delta T$.

## Remarks

Combining the three clauses gives
$$F_{\mathrm{conv}} = \rho c_P T \sqrt{g \delta} \, \frac{\ell^2}{4 \sqrt{2}} \, H_P^{-3/2} (\nabla - \nabla_e)^{3/2}.$$
The numerical factors $1/2$ and $1/8$ come from averaging over blobs that have travelled between $0$ and $\ell$.
Other versions of the theory use other factors, which change the fitted value of $\alpha$.
Example: in the deep convective envelope of the Sun the density is high.
So a tiny excess $\nabla - \nabla_e$ already carries the whole luminosity, and $\nabla$ is very close to the adiabatic gradient.
Non-example: in a layer with $\nabla < \nabla_{\mathrm{ad}}$, stable by the [[Schwarzschild criterion|85GWQPTJ3W]], a displaced blob returns, and the model gives no convective flux.
Solar models usually need $\alpha$ between about $1.5$ and $2$.
