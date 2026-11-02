---
tag: EPS9JT55MV
kind: concept
name: Restriction of a measure
msc: [28A12]
sources:
  - url: https://en.wikipedia.org/wiki/Restriction_(mathematics)
---

## Summary

The restriction of a [[measure|PR11BZQQPG]] to a measurable set $A$ keeps the mass that lies inside $A$ and forgets the rest.
It is again a measure on the same space.
Restriction lets one integrate over a subset, since the integral of $f$ over $A$ is the integral of $f$ for the restricted measure.

## Explanations

### L1 human

Picture a measure as paint spread over a space.
Restricting it to a region $A$ wipes away all the paint outside $A$.
A set $B$ then gets the amount of paint that lies in both $B$ and $A$.
For example, restrict length on the real line to $A = [0, 1]$.
Then the interval $[0, 5]$ gets the value $1$, and the interval $[2, 3]$ gets the value $0$.
