---
tag: DDCNQDTGQW
kind: definition
name: Transonic flow
msc: [76H05, 35M10]
defines: 20G6N8JGEH
uses: [FJC2GMVARF, GFHJ858AN1, SN4J6KP03C, 21DD2334NR, JSDMGGTG7G]
sources:
  - url: https://en.wikipedia.org/wiki/Transonic
---

## Definition

Consider a steady [[compressible flow|FJC2GMVARF]] past a body, with local [[Mach number|GFHJ858AN1]] $M(x) = \abs{\mathbf{u}(x)} / c(x)$, where $c(x)$ is the local [[speed of sound|SN4J6KP03C]].
The flow is *transonic* if the set where $M < 1$ and the set where $M > 1$ are both nonempty.
The surface $\set{x : M(x) = 1}$ that separates them is the *sonic surface*, or sonic line in a plane flow.
The *critical Mach number* of the body is the free stream Mach number at which $M = 1$ is first reached somewhere on the body.

## Remarks

Example: a typical airfoil at free stream Mach number $0.8$ has a supersonic pocket above its upper surface, closed downstream by a [[shock wave|JSDMGGTG7G]].
The flow elsewhere is subsonic, so the flow is transonic.
Non-example: the same airfoil at free stream Mach number $0.3$ has $M < 1$ everywhere, so the flow is subsonic.
In engineering usage the transonic range is roughly $0.8 < M_\infty < 1.2$.
For steady irrotational flow, the potential equation is elliptic where $M < 1$ and hyperbolic where $M > 1$.
So a transonic flow solves a PDE of mixed type, a nonlinear relative of the [[Tricomi equation|21DD2334NR]].
