---
tag: G5WT6QN8WR
kind: concept
name: Convergence in measure
msc: [28A20]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_in_measure
same_as:
  wikidata: Q768656
  wikipedia: Convergence in measure
---

## Summary

A sequence $(f_n)$ of [[measurable functions|YYNCJSR0PJ]] converges in measure to $f$ if bad sets shrink.
For each $\varepsilon > 0$, the set where $f_n$ differs from $f$ by at least $\varepsilon$ must have measure tending to $0$.
It is weaker than uniform convergence and than convergence in $L^p$.
In probability theory it is called convergence in probability.

## Explanations

### L1 human

Convergence in measure does not ask the functions to approach $f$ at every point.
It asks that the region where $f_n$ is far from $f$ shrinks to size $0$.
For example, a narrow bump of height $1$ that sweeps again and again across $[0, 1]$, getting narrower each pass, converges to $0$ in measure.
Yet at each point the bump returns infinitely often, so the sequence converges at no point.
