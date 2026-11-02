---
tag: 5TBC06NNS1
kind: concept
name: Completely distributive lattice
msc: [06D10, 06B23]
specializes: [D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Completely_distributive_lattice
same_as:
  wikidata: Q5156529
  wikipedia: Completely distributive lattice
---

## Summary

A completely distributive lattice is a complete lattice in which arbitrary meets distribute over arbitrary joins, in the strongest possible form.
It is the infinite version of a [[distributive lattice|0HM0HQCK6N]].
Power sets and the closed interval $[0, 1]$ are completely distributive, and every completely distributive lattice is a [[frame|306PWGH7BF]].

## Explanations

### L1 human

In a distributive lattice, one can expand $a \wedge (b \vee c)$ into $(a \wedge b) \vee (a \wedge c)$, like multiplying out brackets.
Complete distributivity allows this expansion for infinitely many factors, each of which is an infinite join.
The result is a join over all ways of choosing one term from each factor, just as $(a_1 + a_2)(b_1 + b_2)$ is the sum of the four products $a_i b_j$.
In the lattice of subsets of a set, with unions and intersections, this expansion always works.
