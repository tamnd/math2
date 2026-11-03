---
tag: A83CYGDXFG
kind: concept
name: Mutual information
msc: [94A17, 62B10]
sources:
  - url: https://en.wikipedia.org/wiki/Mutual_information
same_as:
  wikidata: Q252973
  wikipedia: Mutual information
---

## Summary

The mutual information $I(X; Y)$ of two random variables measures how much information one of them gives about the other.
It is the [[Kullback–Leibler divergence|PQBW43X5RE]] of the joint law of $(X, Y)$ from the product of the two marginal laws.
For discrete variables of finite entropy, $I(X; Y) = H(X) - H(X \mid Y) = H(X) + H(Y) - H(X, Y)$.
It is non-negative, symmetric, and zero exactly for independent variables, and the [[channel capacity|J7MZ2XQP9M]] is its maximum over input laws.

## Explanations

### L1 human

Mutual information measures how much learning one quantity tells you about another.
If $X$ and $Y$ are independent, learning $Y$ tells nothing about $X$, and the mutual information is $0$.
If $Y$ is an exact copy of a fair coin $X$, learning $Y$ tells everything about $X$, and the mutual information is $1$ bit.
Unlike correlation, it detects every kind of dependence, not only linear dependence.
It is the amount of uncertainty about $X$ that disappears when $Y$ is observed.
