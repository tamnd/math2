---
tag: 42NZSQ65DQ
kind: concept
name: Response surface methodology
msc: [62K20]
sources:
  - url: https://en.wikipedia.org/wiki/Response_surface_methodology
same_as:
  wikidata: Q3136137
  wikipedia: Response surface methodology
---

## Summary

Response surface methodology is a set of statistical techniques for learning how a response depends on several input factors.
Its goal is to find the factor settings that make the response best.
It fits low-order polynomial models to data from designed experiments and moves through the factor space in a sequence of experiments.
George Box and K. B. Wilson introduced it in 1951, and it is widely used to improve industrial processes.

## Explanations

### L1 human

Think of the response, such as the yield of a chemical process, as an unknown hilly landscape over the settings of temperature and pressure.
A few runs near the current settings show which way is uphill, and a flat plane fitted to them gives the direction to walk.
Near the top the landscape bends, so a quadratic surface is fitted instead and its peak is computed.
For example, if the fitted surface near the top is $y = 80 - (x_1 - 1)^2 - 2 (x_2 + 0.5)^2$, the best settings are $x_1 = 1$ and $x_2 = -0.5$.
