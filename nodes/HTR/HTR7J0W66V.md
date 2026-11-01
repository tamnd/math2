---
tag: HTR7J0W66V
kind: concept
name: Coupling
msc: ["60E05", "60E15"]
sources:
  - url: https://en.wikipedia.org/wiki/Coupling_(probability)
same_as:
  wikidata: Q1784133
  wikipedia: Coupling (probability)
---

## Summary

A coupling of two [[probability measures|059TJN0NZ1]] $\mu$ and $\nu$ is a joint law of a pair $(X, Y)$.
In it, $X$ has law $\mu$ and $Y$ has law $\nu$.
The two marginals are fixed, but the dependence between $X$ and $Y$ is free to choose.
A clever choice turns a comparison of two laws into a comparison of two random variables on one space.
Couplings are a main tool for bounds in total variation distance, for convergence of [[Markov chains|0G48PYM96Q]], for [[stochastic ordering|HJPPRZ29YE]] and in optimal transport.

## Explanations

### L1 human

Two dice are a coupling of two uniform laws on $\set{1, \dots, 6}$; they can be thrown independently, or glued so that both always show the same face.
Both choices give the right law for each die, but very different pairs.
Take a coin with heads probability $p$ and one with $q \ge p$, and one uniform number $U$ in $[0, 1]$.
Say that coin one shows heads when $U < p$ and coin two when $U < q$.
Then each coin has the right law, and coin two shows heads whenever coin one does, which proves at once that coin two is more likely to show heads.
