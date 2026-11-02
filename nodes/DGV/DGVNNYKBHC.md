---
tag: DGVNNYKBHC
kind: concept
name: Porous medium equation
msc: [35K65, 35K55, 76S05]
sources:
  - url: https://en.wikipedia.org/wiki/Porous_medium_equation
same_as:
  wikidata: Q116986877
  wikipedia: Porous medium equation
---

## Summary

The porous medium equation is the nonlinear diffusion equation $u_t = \Delta(u^m)$ with $m > 1$.
It models the flow of a gas through a porous rock, among other things.
The diffusion coefficient $m u^{m-1}$ vanishes where $u = 0$, so the equation is degenerate there.
As a consequence, disturbances travel with finite speed and solutions can have compact support with a moving free boundary.

## Explanations

### L1 human

In the ordinary [[heat equation|VP2HN86VAG]], heat spreads at once to the whole space, however little of it there is.
In the porous medium equation the spreading rate grows with the density, so where there is almost nothing, almost nothing moves.
A blob of gas therefore keeps a sharp edge that advances at finite speed.
The explicit Barenblatt solution shows this: it is a bump of compact support whose radius grows like a power of $t$.
