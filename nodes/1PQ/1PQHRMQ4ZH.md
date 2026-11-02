---
tag: 1PQHRMQ4ZH
kind: definition
name: Non-measurable set
msc: [28A05]
defines: PKQ7ABPVSG
uses: [N4KDT83V3S]
sources:
  - url: https://en.wikipedia.org/wiki/Non-measurable_set
---

## Definition

Let $(X, \Sigma)$ be a [[measurable space|N4KDT83V3S]].
A subset $A \subseteq X$ is *non-measurable* (with respect to $\Sigma$) if $A \notin \Sigma$.
Without further qualification, a non-measurable subset of $\R^n$ is a set that is not Lebesgue measurable.

## Remarks

Example: on $X = \set{1, 2}$ with $\Sigma = \set{\varnothing, X}$, the set $\set{1}$ is non-measurable.
Example: a Vitali set in $[0, 1]$ is not Lebesgue measurable.
Non-example: every interval, every open set and every closed subset of $\R^n$ is Lebesgue measurable, so none of them is non-measurable.
For Lebesgue measure, $A \subseteq \R^n$ is non-measurable if and only if there is a set $B$ with $\lambda^*(B) < \lambda^*(B \cap A) + \lambda^*(B \setminus A)$, where $\lambda^*$ is Lebesgue outer measure.
Every subset of $\R^n$ with positive outer measure contains a non-measurable subset.
Being non-measurable depends on $\Sigma$: a set that is not a Borel set may still be Lebesgue measurable.
