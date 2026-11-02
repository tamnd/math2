---
tag: G0ZT1SDQGS
kind: concept
name: Butterfly effect
msc: [37D45, 37B02, 37N10]
sources:
  - url: https://en.wikipedia.org/wiki/Butterfly_effect
same_as:
  wikidata: Q187536
  wikipedia: Butterfly effect
---

## Summary

The butterfly effect is the popular name for sensitive dependence on initial conditions in a dynamical system.
Arbitrarily small changes in the initial state can lead to large differences in the later states.
The name comes from Edward Lorenz, whose computer model of convection, now the [[Lorenz system|WYRC41CQN9]], showed this behaviour.
It is a central ingredient of [[chaos theory|DBKXCGDKTD]] and sets practical limits on long-range prediction, even for fully deterministic systems.

## Explanations

### L1 human

The image is that the flap of a butterfly's wings could, weeks later, change whether a storm forms far away.
The point is not that butterflies cause storms, but that tiny causes can have effects that grow out of all proportion.
A simple model is the doubling map $x \mapsto 2x \bmod 1$ on $[0, 1)$.
Two starting values that differ by $10^{-6}$ differ by about $2^n \cdot 10^{-6}$ after $n$ steps, as long as this is small.
After about $20$ steps the difference is of the same size as the whole interval.
