---
tag: D67W7FNRDW
kind: definition
name: Bonnor–Ebert mass
msc: [85A30, 85A15, "76E20"]
defines: MEFJ35FV3F
uses: [4FC5XQA2RK, 5MXPY6QTZ6, SN4J6KP03C]
sources:
  - url: https://en.wikipedia.org/wiki/Bonnor%E2%80%93Ebert_mass
---

## Definition

Let an isothermal gas with [[sound speed|SN4J6KP03C]] $c_s > 0$ form a ball in [[hydrostatic equilibrium|4FC5XQA2RK]] under its own gravity.
Let $G$ be the gravitational constant, and let the boundary be held at a fixed external pressure $P_{\text{ext}} > 0$.
Such equilibria are the solutions of the isothermal [[Emden–Chandrasekhar equation|5MXPY6QTZ6]] truncated at a dimensionless radius $\xi_0$.
For fixed $c_s$ and $P_{\text{ext}}$ their mass $M$ is a function of $\xi_0$.
The *Bonnor–Ebert mass* $M_{\text{BE}}$ is the maximum of this function over $\xi_0 > 0$.
It is attained at $\xi_0 \approx 6.45$, and
$$M_{\text{BE}} \approx 1.18 \, \frac{c_s^4}{G^{3/2} P_{\text{ext}}^{1/2}}.$$

## Remarks

Example: doubling the temperature at fixed $P_{\text{ext}}$ doubles $c_s^2$, so $M_{\text{BE}}$ grows by the factor $4$.
At the critical sphere the ratio of central to boundary density is about $14$; equilibria with a larger density contrast, $\xi_0 > 6.45$, are unstable to collapse.
Non-example: a sphere of mass $2 M_{\text{BE}}$ at the same $c_s$ and $P_{\text{ext}}$ has no hydrostatic equilibrium at all, so it has no Bonnor–Ebert structure and must collapse.
The isothermal equation is $\frac{1}{\xi^2} \frac{d}{d\xi}\left(\xi^2 \frac{d\psi}{d\xi}\right) = e^{-\psi}$, with density $\rho = \rho_c e^{-\psi}$, central density $\rho_c$ and radius $r = \xi \, c_s / \sqrt{4\pi G \rho_c}$.
Letting $\xi_0 \to \infty$ approaches the [[singular isothermal sphere|GCPWX48XRD]] at large radii.
