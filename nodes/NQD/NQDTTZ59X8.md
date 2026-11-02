---
tag: NQDTTZ59X8
kind: concept
name: Period-doubling bifurcation
msc: ["37G15", "37E05", "34C23"]
sources:
  - url: https://en.wikipedia.org/wiki/Period-doubling_bifurcation
same_as:
  wikidata: Q2181373
  wikipedia: Period-doubling bifurcation
---

## Summary

A period-doubling bifurcation, or flip bifurcation, happens in a family of maps when the derivative at a fixed point crosses $-1$.
The fixed point changes stability, and an orbit of period $2$ is born from it.
For flows, the same happens to a periodic orbit whose Floquet multiplier crosses $-1$: a new periodic orbit of about twice the period appears.
A sequence of such bifurcations, at parameters that accumulate geometrically, is one of the main routes to chaos, governed by the [[Feigenbaum constants|F1EHT2CPHC]].

## Explanations

### L1 human

Picture a population that settles to the same size each year.
When a parameter such as the growth rate is increased, this steady state can lose stability by overshooting: too large one year, too small the next.
The population then settles into an alternating pattern, high and low, of period two.
This is a period-doubling bifurcation; in the logistic map $x \mapsto r x (1 - x)$ it happens at $r = 3$.
