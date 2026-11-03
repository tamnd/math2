---
tag: BMW8P4EMTZ
kind: definition
name: Shallow ice approximation
msc: [86A40, 76A20]
defines: 3HZG36PHDP
uses: [ZSWNS5BRS1, 8RA7AMWSAF]
sources:
  - url: https://en.wikipedia.org/wiki/Ice-sheet_model
---

## Definition

Consider grounded ice of constant density $\rho$ under gravity $g$, with bed elevation $b(x, y)$, surface elevation $s(x, y, t)$ and thickness $H = s - b$.
The ice deforms by [[Glen's flow law|ZSWNS5BRS1]] with rate factor $A$ and exponent $n$.
Assume that the aspect ratio of thickness to horizontal extent is small.
The *shallow ice approximation* is the model given by the leading order of the flow equations in this ratio:

1. The pressure is hydrostatic, $p = \rho g (s - z)$.
2. The only deviatoric stresses kept are the vertical shear stresses $(\tau_{xz}, \tau_{yz}) = -\rho g (s - z) \nabla s$, where $\nabla s$ is the horizontal gradient of $s$.
3. The horizontal velocity $\mathbf u$ satisfies $\partial \mathbf u / \partial z = 2A\,\tau_e^{\,n-1} (\tau_{xz}, \tau_{yz})$ with $\tau_e = \abs{(\tau_{xz}, \tau_{yz})}$, and equals a given sliding velocity $\mathbf u_b$ at the bed.
4. The thickness obeys the [[conservation law|8RA7AMWSAF]] $\partial H / \partial t + \nabla \cdot \mathbf q = a$, where $\mathbf q = \int_b^s \mathbf u \, dz$ is the ice flux and $a$ is the net accumulation rate.

## Remarks

Integrating clause 3 twice with $\mathbf u_b = 0$ gives
$$\mathbf q = -\frac{2A(\rho g)^n}{n + 2} H^{n+2} \abs{\nabla s}^{n-1} \nabla s,$$
so clause 4 becomes a nonlinear diffusion equation for $H$.
Example: take a flat bed in one dimension, constant accumulation $a > 0$, a divide at $x = 0$ and a margin at $x = L$.
The steady flux is then $q = ax$.
Solving $q = -\Gamma H^{n+2} \abs{H'}^{n-1} H'$ with $\Gamma = 2A(\rho g)^n/(n+2)$ gives the profile $H(x)^{2 + 2/n} = H(0)^{2 + 2/n}\big(1 - (x/L)^{1 + 1/n}\big)$.
A non-example is a floating ice shelf: there is no shear stress at its base, so clause 2 fails and the flow is controlled by longitudinal stresses instead.
The approximation also breaks down near ice divides and margins and in fast ice streams, where longitudinal stresses matter.
