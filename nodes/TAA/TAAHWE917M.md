---
tag: TAAHWE917M
kind: concept
name: Reaction–diffusion system
msc: [35K57, 35Q92, 35K58]
specializes: [1CCTH8X2FT]
sources:
  - url: https://en.wikipedia.org/wiki/Reaction%E2%80%93diffusion_system
same_as:
  wikidata: Q901210
  wikipedia: Reaction–diffusion system
---

## Summary

A reaction–diffusion system is a system of [[parabolic|1CCTH8X2FT]] equations $\partial_t u = D \Delta u + R(u)$ for several quantities.
Each quantity diffuses in space and reacts with the others at each point.
It models chemical reactions, population dynamics, the spread of epidemics and the formation of patterns in biology.
Depending on the reaction term, solutions can show travelling fronts, spatial patterns or oscillations.
Turing showed that diffusion can make a stable uniform state unstable and so create patterns.

## Explanations

### L1 human

Picture several chemicals in a dish: each one spreads out by diffusion, and at each point they react and turn into each other.
The equation for each concentration has two parts, a diffusion part that evens it out and a reaction part that depends on the local amounts.
With one quantity and the reaction $u(1 - u)$, it describes a population that grows to a limit and spreads, leading to a wave that invades empty space.
With two quantities that diffuse at different speeds, it can produce spots and stripes like those on animal coats.
