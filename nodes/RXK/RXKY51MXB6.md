---
tag: RXKY51MXB6
kind: concept
name: Lieb–Yngvason axiomatization of entropy
msc: [80A05, 80A10]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy
---

## Summary

The Lieb–Yngvason axiomatization derives the existence of [[entropy|SPY89W0RJ7]] from a few axioms about one relation: adiabatic accessibility between equilibrium states.
Elliott Lieb and Jakob Yngvason showed that these axioms, with a comparison hypothesis, give an entropy function.
This function is additive and extensive, and it exactly encodes which states can be reached from which.
The construction uses no heat engines, no temperature and no notion of heat.
It makes the second law a theorem about an order relation.

## Explanations

### L1 human

Say that a state $Y$ is accessible from a state $X$ if some process leads from $X$ to $Y$.
The only trace the process may leave in the surroundings is a weight that moved up or down.
Lieb and Yngvason list simple rules that this relation obeys, such as "if $X$ leads to $Y$ and $Y$ leads to $Z$, then $X$ leads to $Z$".
From these rules alone they build a number $S(X)$ for each state, so that $Y$ is accessible from $X$ exactly when $S(X) \le S(Y)$.
For example, stirring water raises its temperature and its entropy, and the reverse change cannot be made this way.
