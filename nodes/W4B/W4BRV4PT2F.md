---
tag: W4BRV4PT2F
kind: concept
name: Gersten complex
msc: ["19E08", "19D45", "14C35"]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_formula
---

## Summary

The Gersten complex of a scheme $X$ in degree $n$ is a complex built from the points of $X$, grouped by codimension.
Its terms are sums of [[algebraic K-groups|5GVFZWMWC8]] of the residue fields of these points.
Its differentials come from Quillen's localization sequence.
For smooth varieties over a field it gives a flasque resolution of the K-theory sheaf, which leads to [[Bloch's formula|K72F2F3ET3]].

## Explanations

### L1 human

Every point of a scheme, closed or not, has a residue field, and fields have K-groups.
The Gersten complex first lists the K-groups of the residue fields of the generic points.
Then come those of points in codimension one, then codimension two, and so on, with the K-degree lowered by one at each step.
In degree one it starts with the nonzero rational functions and sends each one to its orders of vanishing along the divisors.
For $X = \operatorname{Spec} \Z$ this is the map $\Q^\times \to \bigoplus_p \Z$ that sends a rational number to the exponents of the primes in it.
