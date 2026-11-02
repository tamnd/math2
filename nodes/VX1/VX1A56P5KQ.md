---
tag: VX1A56P5KQ
kind: concept
name: Hardy–Littlewood maximal function
msc: [42B25, 28A15]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy–Littlewood_maximal_function
same_as:
  wikidata: Q3075250
  wikipedia: Hardy–Littlewood maximal function
---

## Summary

Let $f$ be a locally integrable function on $\R^n$.
Its Hardy–Littlewood maximal function $Mf$ gives at each point the largest average of $\abs{f}$ over balls centred there.
It dominates $\abs{f}$ almost everywhere and controls all local averages of $f$ at once.
The maximal operator $f \mapsto Mf$ is bounded on $L^p$ for $1 < p \le \infty$ and of weak type $(1,1)$.
These bounds give the Lebesgue differentiation theorem and are a basic tool in harmonic analysis.

## Explanations

### L1 human

At each point, look at all balls centred there and average $\abs{f}$ over each ball.
The maximal function records the biggest of these averages.
It is a worst-case summary of how large $f$ is near the point at every scale.
For the indicator of $[0, 1]$ on the line, the maximal function at a point $x > 1$ is $1/(2x)$, so it decays slowly far away.
