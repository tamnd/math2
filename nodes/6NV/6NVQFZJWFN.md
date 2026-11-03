---
tag: 6NVQFZJWFN
kind: definition
name: Mach number
msc: [76N15, 76M55]
defines: GFHJ858AN1
uses: [T3R5FWV91P, SN4J6KP03C]
sources:
  - url: https://en.wikipedia.org/wiki/Mach_number
---

## Definition

Consider a flow of a compressible fluid.
Let $u$ be the flow speed at a point, or the speed of a body relative to the fluid.
Let $c$ be the local [[speed of sound|SN4J6KP03C]] in the fluid.
The *Mach number* is
$$\mathrm{M} = \frac{u}{c}.$$
The flow is *subsonic* where $\mathrm{M} < 1$, *sonic* where $\mathrm{M} = 1$ and *supersonic* where $\mathrm{M} > 1$.

## Remarks

It is a [[dimensionless number|T3R5FWV91P]], as a ratio of two speeds.
Example: a body moving at $680\ \mathrm{m/s}$ in air with $c = 340\ \mathrm{m/s}$ has $\mathrm{M} = 2$, so the flow is supersonic.
Non-example: the difference $u - c$ is not a Mach number; it has dimension of speed and depends on the units.
For steady flow, density changes are of order $\mathrm{M}^2$, so flows with small Mach number are well modelled as incompressible.
For a steady supersonic flow, the linearised potential equation is hyperbolic, while for subsonic flow it is elliptic.
