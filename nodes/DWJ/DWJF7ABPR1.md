---
tag: DWJF7ABPR1
kind: concept
name: Lebesgue integral
msc: [28A25, 26A42]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_integral
same_as:
  wikidata: Q853831
  wikipedia: Lebesgue integral
---

## Summary

The Lebesgue integral assigns a number to each integrable function on a measure space.
It is built from simple functions, then non-negative functions, then general functions split into positive and negative parts.
It extends the Riemann integral to many more functions and to any measure space.
Its great strength is the convergence theorems, which let one exchange limits and integrals under mild conditions.

## Explanations

### L1 human

The Riemann integral cuts the horizontal axis into small pieces.
The Lebesgue integral cuts the vertical axis instead: for each range of values it asks how large the set of points with those values is.
This handles functions that jump around wildly.
For example, the indicator function of the rationals on $[0, 1]$ has no Riemann integral.
Its Lebesgue integral is $0$, because the rationals form a set of measure zero.
