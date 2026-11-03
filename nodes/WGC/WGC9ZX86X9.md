---
tag: WGC9ZX86X9
kind: definition
name: Soret effect
msc: [80A19, 82C35, 82C70]
defines: ZGHEWY5NG9
uses: [KK46Q2YV1D, STR73R5MX4]
sources:
  - url: https://en.wikipedia.org/wiki/Thermophoresis
---

## Definition

Let a binary fluid mixture have mass density $\rho$, mass fraction $w$ of component $1$ and absolute [[temperature|KK46Q2YV1D]] $T$, all fields in space.
Let $j$ be the diffusive mass flux of component $1$, relative to the centre-of-mass velocity.
In the linear regime
$$j = -\rho D \nabla w - \rho\, w (1 - w)\, D_T \nabla T,$$
where $D > 0$ is the diffusion coefficient and $D_T$ is the *thermal diffusion coefficient*.
The *Soret effect* is the second term, the mass flux driven by the temperature gradient.
The ratio $S_T = D_T / D$ is the *Soret coefficient*.

## Remarks

In a steady state with no mass flux, $j = 0$ gives
$$\nabla w = -w (1 - w)\, S_T \nabla T.$$
So for $S_T > 0$ component $1$ gathers at the cold side, and for $S_T < 0$ at the warm side.
Example: in a mixture with $w = 1/2$ and $S_T = 10^{-2}\,\mathrm{K}^{-1}$, a temperature difference of $1$ K across the cell gives a mass fraction difference of about $2.5 \times 10^{-3}$.
Non-example: in an ideal mixture at uniform temperature, $\nabla T = 0$, and the flux is pure Fickian diffusion with no Soret term.
The flux and force pair of the Soret term enters the [[entropy production|STR73R5MX4]], and the reciprocal cross effect is the Dufour effect.
