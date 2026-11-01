---
tag: A8251BHCMP
kind: concept
name: Bounded variation
msc: [26A45]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_variation
same_as:
  wikidata: Q829653
  wikipedia: Bounded variation
---

## Summary

A real function on a closed interval has bounded variation when the total up-and-down movement of its values is finite.
This total movement is the [[total variation|8QA5DEWNYD]] of the function.
Functions of bounded variation are exactly the differences of two [[monotone functions|0WFF6AZPBP]], by the [[Jordan decomposition|KDT3E0VE0K]].
They are the natural integrators for the [[Riemann–Stieltjes integral|JT9AFHG0NA]] and they are differentiable almost everywhere.

## Explanations

### L1 human

Walk along the graph of a function from left to right and count how far the value goes up and down in total.
If this distance is finite, the function has bounded variation.
Every monotone function on $[a, b]$ has bounded variation, since its values move in one direction only.
The function $x \sin(1/x)$ on $[0, 1]$, with value $0$ at $0$, does not.
It swings up and down infinitely often near $0$, and the sizes of the swings add up to infinity.
