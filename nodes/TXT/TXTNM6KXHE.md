---
tag: TXTNM6KXHE
kind: concept
name: Prony series
msc: [74D05]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_Maxwell_model
---

## Summary

A Prony series is a finite sum of decaying exponentials plus a constant, used to represent the [[relaxation modulus|JSSYGY0V87]] of a linear viscoelastic material.
It is exactly the relaxation modulus of a [[generalized Maxwell model|H2XT5TQJ7K]], so each term has a mechanical meaning as a spring–dashpot arm.
Measured relaxation curves are fitted by Prony series, and finite element codes use them because the hereditary integral can then be updated step by step.

## Explanations

### L1 human

A real material forgets its stress over many time scales, from seconds to years.
A Prony series models this as a few separate exponential decays, each with its own time constant, added together.
For example, $G(t) = 1 + 2 e^{-t} + 3 e^{-t/100}$ has a fast decay, a slow decay, and a long-term level $1$.
