---
tag: E7ZC459PSA
kind: concept
name: Local time
msc: [60J55, 60J65]
sources:
  - url: https://en.wikipedia.org/wiki/Local_time_(mathematics)
same_as:
  wikidata: Q3883775
  wikipedia: Local time (mathematics)
---

## Summary

The local time $L(t, x)$ of a [[Brownian motion|22735FGJV6]] measures how much time the path spends near the level $x$ up to time $t$.
It is the density of the occupation measure of the path with respect to Lebesgue measure.
Local time is the correction term in [[Tanaka's formula|GEM0ERJ5ZB]], which extends [[Itô's lemma|2J1RVQB0CM]] to the function $\abs{x}$.

## Explanations

### L1 human

A Brownian path hits each level it visits infinitely often, but the set of times it sits exactly at a level has length zero.
So the plain time spent at $x$ is always zero, and it says nothing.
Local time instead counts the time spent in a thin band $(x - \varepsilon, x + \varepsilon)$ and divides by the width $2\varepsilon$.
As $\varepsilon$ shrinks, this ratio has a finite positive limit at levels the path has crossed.
For a standard Brownian motion started at $0$, the expected local time at $0$ up to time $t$ is $\sqrt{2t/\pi}$.
