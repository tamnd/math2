---
tag: 1NYTFT5NPE
kind: concept
name: Path integral formulation
msc: [81S40, 81Q30, 81T08]
sources:
  - url: https://en.wikipedia.org/wiki/Path_integral_formulation
same_as:
  wikidata: Q898323
  wikipedia: Path integral formulation
---

## Summary

The path integral formulation describes quantum evolution as a sum over all paths a system could take.
Each path $q(\cdot)$ contributes the phase $e^{iS[q]/\hbar}$, where $S$ is the classical action.
The transition amplitude is the "integral" of these phases over all paths with fixed end points.
No Lebesgue-type measure on paths makes this literal.
So the integral is defined as a limit of finite-dimensional integrals over broken-line paths.
After [[Wick rotation|G686S8SEK0]] it becomes a genuine integral, given by the [[Feynman–Kac formula|W26MGR4DA3]].
It is the standard tool for perturbative quantum field theory, and it shows how classical mechanics appears when $\hbar \to 0$, by stationary phase.

## Explanations

### L1 human

A classical particle follows one path, the one that makes the action stationary.
In quantum mechanics, the particle "tries" every path between the start and the end.
Each path gets a little rotating arrow whose angle is the action divided by $\hbar$, and the arrows are added up.
Paths far from the classical one have rapidly changing angles and cancel each other, so for large actions only paths near the classical path matter.
This explains why everyday objects follow classical laws.
