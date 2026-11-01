---
tag: PQBW43X5RE
kind: concept
name: Kullback–Leibler divergence
msc: [94A17, 62B10, 60F10]
sources:
  - url: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
same_as:
  wikidata: Q255166
  wikipedia: Kullback–Leibler divergence
---

## Summary

The Kullback–Leibler divergence $D(P \,\|\, Q)$, also called relative entropy, measures how much a probability distribution $P$ differs from a reference distribution $Q$.
It is non-negative and equals $0$ exactly when $P = Q$, but it is not symmetric and is not a metric.
It is the rate function in [[Sanov's theorem|QWEF2WAXJM]] and the expected log-likelihood ratio in statistics.
In information theory, it is the extra code length when one codes for $Q$ but the data follow $P$.

## Explanations

### L1 human

Suppose you believe that data come from a distribution $Q$, but they really come from $P$.
The Kullback–Leibler divergence measures, on average, how surprised you are by this mistake.
For a coin that really lands heads with probability $1/2$, the divergence from a model that says $1/4$ is $\frac{1}{2} \log \frac{4}{3}$, about $0.14$ in natural units.
It is zero only when the model is right.
