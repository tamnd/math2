---
tag: AGG1WQVR0V
kind: definition
name: Radiosity
msc: [80A21, 78A40]
defines: 5SAVDDA5P1
uses: [S6XR2K4N8G, VETMCF1NQ5, A2RMYX8A65, 1Y36434YTE]
sources:
  - url: https://en.wikipedia.org/wiki/Radiosity_(radiometry)
---

## Definition

Let $dA$ be an element of a surface.
The *radiosity* $J$ of the surface at $dA$ is the radiant power leaving $dA$ per unit area.
It is summed over all wavelengths and over all directions of the hemisphere above the surface.
It includes the [[thermal radiation|S6XR2K4N8G]] emitted by the surface and the radiation reflected or transmitted by it.
The *irradiation* $G$ is the radiant power incident on $dA$ per unit area.

## Remarks

For an opaque, grey and diffuse surface at absolute temperature $T$ with [[emissivity|VETMCF1NQ5]] $\varepsilon$, the reflectivity is $1 - \varepsilon$, and
$$J = \varepsilon \sigma T^4 + (1 - \varepsilon) G,$$
where $\sigma$ is the Stefan–Boltzmann constant.
The net radiative [[heat flux|1Y36434YTE]] leaving the surface is $q'' = J - G = \dfrac{\varepsilon}{1 - \varepsilon} (\sigma T^4 - J)$ for $\varepsilon < 1$.

Example: a [[black body|A2RMYX8A65]] at temperature $T$ has $\varepsilon = 1$ and reflects nothing, so $J = \sigma T^4$ whatever the irradiation.

Non-example: the irradiation $G$ is not the radiosity: it is the power arriving at the surface, not leaving it.
The two are equal only when the net radiative flux is zero.

Radiosity has the unit W/m$^2$, like a heat flux.
