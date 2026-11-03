---
tag: 8K5AM6EMWH
kind: definition
name: Virial mass
msc: [85A15, 85A40]
defines: EC34EJYV16
uses: [PPHFS2P4G4, 5V6T169QRK, A8YJ7EKMV7, 6T0BTVNMRF]
sources:
  - url: https://en.wikipedia.org/wiki/Virial_mass
---

## Definition

Let $H(z)$ be the Hubble parameter at redshift $z$, as in [[Hubble's law|5V6T169QRK]], and let $\rho_c(z) = 3 H(z)^2 / (8 \pi G)$ be the critical density of the [[Friedmann equations|PPHFS2P4G4]].
Fix an overdensity $\Delta > 0$.
Let a roughly spherical object have mass density $\rho(r)$ at distance $r$ from its centre.
Its *virial radius* $r_\Delta$ is the radius at which the mean density inside equals $\Delta \rho_c(z)$:
$$\frac{3}{4 \pi r_\Delta^3} \int_0^{r_\Delta} 4 \pi r^2 \rho(r) \, dr = \Delta \, \rho_c(z).$$
The *virial mass* is
$$M_\Delta = \frac{4 \pi}{3} \Delta \, \rho_c(z) \, r_\Delta^3.$$

## Remarks

Common choices are $\Delta = 200$, giving $M_{200}$, and $\Delta = 18 \pi^2 \approx 178$, the value the [[spherical collapse model|A8YJ7EKMV7]] predicts for a collapsed object in a universe of matter only.
Some authors use the mean matter density instead of $\rho_c$.
The name comes from the [[virial theorem|6T0BTVNMRF]], which the matter inside $r_\Delta$ approximately satisfies.

Example: a singular isothermal sphere $\rho(r) = \sigma^2 / (2 \pi G r^2)$ has mean density $3\sigma^2 / (2 \pi G r^2)$ inside $r$.
Setting this equal to $\Delta \rho_c$ gives $r_\Delta = \sigma \sqrt{3 / (2 \pi G \Delta \rho_c)}$ and $M_\Delta = 2 \sigma^2 r_\Delta / G$.

Non-example: a density that is constant out to infinity has mean density equal to that constant at every radius.
If the constant is below $\Delta \rho_c$, no radius satisfies the condition, and no virial mass is defined.
