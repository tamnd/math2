---
tag: G3MKXX8MX9
kind: definition
name: Supersonic flow
msc: [76J20, 76N15]
defines: G4EN6Y0ZZ2
uses: [FJC2GMVARF, GFHJ858AN1, SN4J6KP03C, 92C3S03AQZ, WR0F7AJZVD]
sources:
  - url: https://en.wikipedia.org/wiki/Supersonic_speed
---

## Definition

Let a [[compressible flow|FJC2GMVARF]] have velocity $\mathbf{u}(x)$ and local [[speed of sound|SN4J6KP03C]] $c(x)$ on a region $\Omega$.
The flow is *supersonic* on $\Omega$ if its local [[Mach number|GFHJ858AN1]] satisfies $M(x) = \abs{\mathbf{u}(x)} / c(x) > 1$ for all $x \in \Omega$.
A flow past a body is called supersonic when its free stream Mach number $M_\infty$ is greater than $1$.

## Remarks

Take steady plane flow with a uniform stream along the $x$-axis and small disturbances.
The perturbation potential $\varphi$ solves
$$(M_\infty^2 - 1)\varphi_{xx} - \varphi_{yy} = 0.$$
This equation is [[hyperbolic|92C3S03AQZ]] for $M_\infty > 1$, in contrast with the elliptic subsonic case of the [[Prandtl–Glauert transformation|WR0F7AJZVD]].
Its characteristics are the lines $y = \pm x / \sqrt{M_\infty^2 - 1}$, which make the Mach angle $\mu = \arcsin(1/M_\infty)$ with the stream.
Example: air at $M_\infty = 2$; then $\mu = 30^\circ$, and a small disturbance at a point affects only the wedge of half-angle $30^\circ$ behind it.
Non-example: a flow at $M_\infty = 0.8$ is subsonic, and its disturbances spread in all directions.
In usage, supersonic often means $1.2 < M_\infty < 5$, the range between transonic and hypersonic flow.
