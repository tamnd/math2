---
tag: Q1QK49TTEJ
kind: concept
name: Information-based complexity
msc: [65Y20, 68Q25, 65J05]
sources:
  - url: https://en.wikipedia.org/wiki/Information-based_complexity
same_as:
  wikidata: Q6030626
  wikipedia: Information-based complexity
---

## Summary

Information-based complexity studies the minimal cost of solving continuous problems, such as integration or approximation of functions, to a given accuracy.
An algorithm may learn the input only through finitely many measurements, for example function values, so the information it has is partial.
The central quantities are the smallest error reachable with $n$ measurements and the smallest $n$ that reaches a given error $\varepsilon$.
It explains, for example, when [[Monte Carlo|HWP11G3HTN]] or [[quasi-Monte Carlo|ABSRB2KXA6]] methods can beat the curse of dimensionality.

## Explanations

### L1 human

A computer cannot see a whole function; it can only ask for its values at finitely many points.
Different functions can give the same answers, so any method must guess, and its error is limited by this uncertainty.
Information-based complexity asks how many questions are needed, at least, to reach a given accuracy.
Take the functions on $[0,1]$ whose slope is at most $1$ in size.
To integrate them to within $\varepsilon$, one needs about $1/(4\varepsilon)$ function values, and the midpoint rule achieves this.
