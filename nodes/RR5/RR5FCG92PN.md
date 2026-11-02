---
tag: RR5FCG92PN
kind: concept
name: Stiff equation
msc: [65L04, 34A99]
specializes: [0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Stiff_equation
same_as:
  wikidata: Q29744
  wikipedia: Stiff equation
---

## Summary

A stiff equation is an ordinary differential equation on which explicit numerical methods must take extremely small steps to stay stable.
This happens even where the solution is smooth, for example with the [[Euler method|0JARTXX4XP]].
Stiffness typically comes from processes that decay on very different time scales.
Stiff equations are solved with implicit methods, which remain stable with large steps.
See the [[definition|AXND5JRQAZ]].

## Explanations

### L1 human

Imagine a system with one part that settles in a millisecond and another part that changes over hours.
After the first millisecond the fast part is at rest, and the solution looks slow and smooth.
Still, a simple step-by-step method must keep tiny steps, or its errors in the fast part blow up.
For $y' = -1000\,(y - \cos t)$ the solution quickly follows $\cos t$, yet the explicit Euler method needs steps below $0.002$.
