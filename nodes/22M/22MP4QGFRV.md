---
tag: 22MP4QGFRV
kind: definition
name: Isentropic flow
msc: [76N15]
defines: SH8FHGTMSE
uses: [FJC2GMVARF, GFHJ858AN1, SN4J6KP03C, JSDMGGTG7G]
sources:
  - url: https://en.wikipedia.org/wiki/Isentropic_process
---

## Definition

Let a [[compressible flow|FJC2GMVARF]] have velocity $\mathbf{u}(x, t)$ and specific entropy $s(x, t)$.
The flow is *isentropic* if the entropy of each fluid particle is constant in time:
$$\frac{Ds}{Dt} = \partial_t s + \mathbf{u} \cdot \nabla s = 0.$$
It is *homentropic* if moreover $s$ is the same constant everywhere.

## Remarks

For an ideal gas with constant ratio of specific heats $\gamma$, isentropic flow means that $p / \rho^\gamma$ is constant along particle paths.
In steady isentropic flow with no heat exchange, along a streamline,
$$\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2} M^2, \qquad \frac{p_0}{p} = \left(\frac{T_0}{T}\right)^{\gamma/(\gamma - 1)}, \qquad \frac{\rho_0}{\rho} = \left(\frac{T_0}{T}\right)^{1/(\gamma - 1)},$$
where $M$ is the [[Mach number|GFHJ858AN1]] and the index $0$ marks the values at rest.
Example: smooth inviscid flow of air through a nozzle; with $T_0 = 300\ \mathrm{K}$ and $\gamma = 1.4$, the temperature at $M = 1$ is $300 / 1.2 = 250\ \mathrm{K}$.
Non-example: flow through a [[shock wave|JSDMGGTG7G]], where the entropy of each particle jumps up, so $Ds/Dt = 0$ fails.
Viscous friction and heat conduction also raise the entropy, so flow inside a boundary layer is not isentropic.
