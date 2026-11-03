---
tag: C27A98GYCX
kind: definition
name: Equilibrium theory of tides
msc: [86A05]
defines: BTZB3SYKJJ
uses: [2E2KCFNMHE, 5Y2BWNY6MF]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_of_tides
---

## Definition

Model the Earth as a rigid sphere of radius $R$ with surface gravity $g$, covered by an ocean.
Let $V(x, t)$ be the total [[tide-generating potential|2E2KCFNMHE]] of the Moon and the Sun.
The *equilibrium theory of tides* assumes that at every time the ocean surface is a level surface of the [[geopotential|5Y2BWNY6MF]] plus $V$.
The *equilibrium tide* is the height of the surface above its undisturbed level given by this assumption.
To first order it is
$$\zeta_{\mathrm{eq}}(x, t) = \frac{V(x, t)}{g}, \qquad \norm{x} = R.$$
The constant term is fixed so that the volume of water is conserved.

## Remarks

Example: for the Moon, the degree two term gives $\zeta_{\mathrm{eq}} = \frac{M}{M_E} \frac{R^4}{d^3} \cdot \frac12 (3\cos^2\psi - 1)$, where $M/M_E \approx 0.0123$ is the mass ratio and $d \approx 60.3 R$.
This is about $0.36$ m at the points facing towards and away from the Moon and about $-0.18$ m on the circle between them.
Since $P_2$ has mean zero over the sphere, the degree two tide already conserves the volume.
Non-example: an observed tide of several metres in a bay is not an equilibrium tide; it is a dynamic response, amplified by resonance.
For an elastic Earth the solid Earth also deforms, and the equilibrium tide relative to the sea floor becomes $(1 + k_2 - h_2)\,V_2/g$, where $k_2$ and $h_2$ are [[Love numbers|C8HCN8NEQP]].
