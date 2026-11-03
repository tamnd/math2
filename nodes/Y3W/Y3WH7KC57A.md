---
tag: Y3WH7KC57A
kind: definition
name: Emissivity
msc: [80A21, 78A40]
defines: VETMCF1NQ5
uses: [A2RMYX8A65, S6XR2K4N8G, AJ8M9MGZGF]
sources:
  - url: https://en.wikipedia.org/wiki/Emissivity
---

## Definition

Let a surface be at absolute [[temperature|AJ8M9MGZGF]] $T$.
Fix a wavelength $\lambda$ and a direction $(\theta, \phi)$, with $\theta$ the angle from the surface normal.
Let $I_{\lambda}(\lambda, \theta, \phi, T)$ be the spectral radiance of the [[thermal radiation|S6XR2K4N8G]] that the surface emits.
Let $I_{\lambda, b}(\lambda, T)$ be the spectral radiance of a [[black body|A2RMYX8A65]] at the same temperature $T$.

1. The *spectral directional emissivity* is $\varepsilon_{\lambda, \theta}(\lambda, \theta, \phi, T) = I_{\lambda}(\lambda, \theta, \phi, T) / I_{\lambda, b}(\lambda, T)$.
2. The *total hemispherical emissivity* is $\varepsilon(T) = E(T) / E_b(T)$.
   Here $E(T)$ is the power emitted by the surface per unit area over all wavelengths and directions.
   And $E_b(T)$ is the same quantity for a black body at $T$.

## Remarks

Example: a black body has $I_\lambda = I_{\lambda, b}$ for all $\lambda$ and directions, so $\varepsilon_{\lambda, \theta} = 1$ and $\varepsilon = 1$.

Non-example: divide the radiance of a surface at $T$ by that of a black body at another temperature $T' \ne T$.
The result is not an emissivity, since the definition compares at the same temperature, and it could even exceed $1$.

Since no body emits more than a black body at the same temperature, $0 \le \varepsilon \le 1$.
A surface whose $\varepsilon_{\lambda, \theta}$ does not depend on $\lambda$ is called grey, and one whose emissivity does not depend on direction is called diffuse.
With $E_b = \sigma T^4$, the emitted power of a surface is $E = \varepsilon \sigma T^4$, where $\sigma$ is the Stefan–Boltzmann constant.
