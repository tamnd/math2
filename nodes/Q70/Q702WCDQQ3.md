---
tag: Q702WCDQQ3
kind: concept
name: Large deviations theory
msc: [60F10]
sources:
  - url: https://en.wikipedia.org/wiki/Large_deviations_theory
same_as:
  wikidata: Q3403615
  wikipedia: Large deviations theory
---

## Summary

Large deviations theory studies the exponential decay of the probabilities of rare events.
Its central notion is the large deviation principle, with a [[rate function|140N2PQSTE]] $I$.
A family of probability measures $\mu_n$ satisfies it when $\mu_n(A)$ behaves like $\exp(-n \inf_{x \in A} I(x))$.
Basic results are [[Cramér's theorem|RZZK51CXMN]] for sample means, [[Sanov's theorem|QWEF2WAXJM]] for empirical measures and [[Varadhan's lemma|BD1CNVV5P0]] for exponential integrals.
The theory is used in statistical mechanics, information theory, queueing and risk analysis.

## Explanations

### L1 human

The [[law of large numbers|0ZVEAYVRC3]] says that the average of many coin tosses is close to $1/2$.
Large deviations theory asks how unlikely it is that the average is far from $1/2$, say above $0.6$.
The answer is that such a probability shrinks exponentially in the number of tosses, with a precise exponent.
For fair coins, the probability that the average of $n$ tosses is at least $0.6$ is about $e^{-0.020 n}$, up to factors that grow more slowly than any exponential.
