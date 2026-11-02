---
tag: XV4K9GREJ9
kind: concept
name: Rational variety
msc: [14M20, "14E08"]
specializes: [YF1SE8WJK3]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_variety
same_as:
  wikidata: Q3554829
  wikipedia: Rational variety
---

## Summary

A rational variety is a variety that is birationally equivalent to projective space.
Its points can be parametrised, on a dense open set, by rational functions of independent parameters.
Deciding which varieties are rational is one of the oldest problems of [[birational geometry|51YVV85GWB]].
Every rational variety is [[unirational|YF1SE8WJK3]], and the converse fails in dimension $3$ over $\C$.

## Explanations

### L1 human

A variety is rational when you can describe almost all of its points by free coordinates, with no hidden constraints.
The circle $x^2 + y^2 = 1$ is rational: each point other than $(-1, 0)$ is
$$\left( \frac{1 - t^2}{1 + t^2}, \frac{2t}{1 + t^2} \right)$$
for exactly one $t$, which is the slope of the line through $(-1, 0)$ and the point.
A smooth plane cubic, such as $y^2 = x^3 - x$, is not rational.
Its genus is $1$, while a rational curve has genus $0$.
