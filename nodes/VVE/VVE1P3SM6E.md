---
tag: VVE1P3SM6E
kind: concept
name: Lp spaces on groups
msc: [43A15, "46E30"]
specializes: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
---

## Summary

The spaces $L^p(G)$ of a locally compact group $G$ are the [[Lp spaces|SASP14MA1Z]] of $G$ with respect to a left [[Haar measure|VY0HXD3GC4]].
The group acts on them by translations, which preserve the norm.
For $1 \le p < \infty$ this action is continuous, a fact used constantly in harmonic analysis.
The case $p = 1$ gives the [[group algebra|6GD25S53ND]] and the case $p = 2$ gives the Hilbert space of the regular representation.

## Explanations

### L1 human

On a group with its Haar measure one can integrate, so one can form the usual spaces of functions whose $p$-th power is integrable.
What is special is that the group can shift these functions around without changing their size.
On the real line, $L^2(\R)$ is the space of finite-energy signals, and shifting a signal in time does not change its energy.
On the integers with counting measure, $L^p(\Z)$ is the space of sequences $(a_n)$ with $\sum_n \abs{a_n}^p < \infty$.
