---
tag: Q7S0D1NAG6
kind: concept
name: Feigenbaum–Cvitanović functional equation
msc: ["37E20", 39B12]
specializes: [BCGBQ3HK26]
sources:
  - url: https://en.wikipedia.org/wiki/Feigenbaum_constants
---

## Summary

The Feigenbaum–Cvitanović functional equation is $g(x) = -\alpha \, g(g(x/\alpha))$, for an even function $g$ with $g(0) = 1$ and a constant $\alpha$.
Its solution is the fixed point of the renormalization operator that doubles the period of a unimodal map and rescales space.
The constant $\alpha$ that comes with the solution is the second of the [[Feigenbaum constants|F1EHT2CPHC]], $\alpha \approx 2.5029$.
The equation explains why the [[period-doubling cascade|6J921PEDN2]] looks the same at every scale, for a large class of maps.

## Explanations

### L1 human

Take a map with one hump, such as $x \mapsto 1 - \mu x^2$, and look at its second iterate near the top of the hump.
After shrinking the picture by a fixed factor and flipping it upside down, it looks almost like the original map.
The equation describes a map that reproduces itself exactly under this operation.
The shrinking factor of that map, about $2.5$, then shows up in the period-doubling route to chaos of many different systems.
