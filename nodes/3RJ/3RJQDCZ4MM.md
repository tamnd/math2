---
tag: 3RJQDCZ4MM
kind: definition
name: Taylor dispersion
msc: [76R50]
defines: M18H5SF3GG
uses: [DG49VBBT91, P27AH8WRRC, 961839PHN6]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor_dispersion
---

## Definition

Consider steady [[Poiseuille flow|P27AH8WRRC]] in a straight circular pipe of radius $a$ with mean velocity $U$.
The flow carries a passive solute with molecular diffusivity $D > 0$ according to the [[advection–diffusion equation|DG49VBBT91]], with no flux of solute through the wall.
Let $\bar c(x, t)$ be the average of the concentration over the cross-section at axial position $x$.
*Taylor dispersion* is the regime in which, for times long compared with the radial diffusion time $a^2 / D$, the average $\bar c$ satisfies the one-dimensional equation
$$\frac{\partial \bar c}{\partial t} + U \frac{\partial \bar c}{\partial x} = D_{\mathrm{eff}} \frac{\partial^2 \bar c}{\partial x^2}, \qquad D_{\mathrm{eff}} = D + \frac{a^2 U^2}{48 D}.$$
The quantity $D_{\mathrm{eff}}$ is the *Taylor dispersion coefficient* (the formula including the term $D$ is often called the Taylor–Aris coefficient).

## Remarks

With the [[Péclet number|961839PHN6]] $\mathrm{Pe} = a U / D$, the coefficient is $D_{\mathrm{eff}} = D (1 + \mathrm{Pe}^2 / 48)$.
So for large $\mathrm{Pe}$ the spreading along the pipe is much faster than molecular diffusion, and it grows as $D$ decreases.

Example: for a solute with $D = 10^{-5}$ cm$^2$/s in a tube of radius $a = 0.01$ cm with $U = 0.1$ cm/s, $\mathrm{Pe} = 100$ and $D_{\mathrm{eff}} \approx 209 D$.

Non-example: at times short compared with $a^2 / D$, the solute has not yet sampled the cross-section.
The band is then mainly stretched by the shear, and $\bar c$ does not obey the effective equation.

Other geometries give the same form with a different constant; for flow between parallel plates at distance $h$ the term is $h^2 U^2 / (210 D)$.
