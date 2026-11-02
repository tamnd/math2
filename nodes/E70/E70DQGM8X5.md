---
tag: E70DQGM8X5
kind: concept
name: Kernel pair
msc: [18A30, 18A20]
specializes: [Q05K04QJ71]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_category
---

## Summary

The kernel pair of a morphism $f \colon X \to Y$ is the [[pullback|Q05K04QJ71]] of $f$ along itself.
It records which pairs of elements $f$ sends to the same place.
So it is the categorical form of the equivalence relation induced by a map.
A morphism $f \colon X \to Y$ is a [[monomorphism|Y2NP1JFR86]] exactly when $X$ with two identity maps is a kernel pair of $f$.
In a [[regular category|2SM3JRJXA4]], a regular epimorphism is the coequalizer of its kernel pair.

## Explanations

### L1 human

A function can send different inputs to the same output.
The kernel pair collects all pairs of inputs with the same output.
For the map from the integers to the remainders modulo $3$, it is the set of pairs $(a, b)$ with $a - b$ divisible by $3$.
For a group homomorphism, it carries the same information as the kernel.
