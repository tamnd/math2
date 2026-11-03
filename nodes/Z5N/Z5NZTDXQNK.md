---
tag: Z5NZTDXQNK
kind: definition
name: Bullen parameter
msc: [86A15, 86A04]
defines: ME689AGRPK
uses: [E4CX8RCSHF, PPXM3HCN6Y]
sources:
  - url: https://en.wikipedia.org/wiki/Adams%E2%80%93Williamson_equation
---

## Definition

Let a spherically symmetric planet in hydrostatic equilibrium have density $\rho(r) > 0$ and gravity $g(r) > 0$ at radius $r$.
Let $\alpha$ and $\beta$ be its P- and S-speeds, with seismic parameter $\Phi = \alpha^2 - \frac43\beta^2 > 0$.
The *Bullen parameter* at radius $r$ is
$$\eta(r) = -\frac{\Phi(r)}{\rho(r)\, g(r)} \frac{d\rho}{dr}(r).$$

## Remarks

By the [[Adams–Williamson equation|E4CX8RCSHF]], $\eta = 1$ in any shell of uniform composition and adiabatic temperature.
With $K = \rho\Phi$, the [[bulk modulus|PPXM3HCN6Y]] along the profile, and $dP/dr = -\rho g$, one finds the equivalent form $\eta = dK/dP + g^{-1} d\Phi/dr$.
The check: $dK/dP = (\Phi\, d\rho/dr + \rho\, d\Phi/dr)/(-\rho g) = \eta - g^{-1} d\Phi/dr$.
Example: if $\rho$ satisfies the Adams–Williamson equation, then $d\rho/dr = -\rho g/\Phi$, and the formula gives $\eta = 1$.
Non-example: a shell in which density does not change with depth while $\rho$, $g$, $\Phi$ are positive has $\eta = 0 \ne 1$; it cannot be adiabatic and uniform.
A superadiabatic temperature gradient gives $\eta < 1$, and a gradual change of composition or phase toward denser material with depth gives $\eta > 1$.
