---
tag: 1SFZNN31JW
kind: concept
name: Gibbs entropy
msc: [82B03, 94A17, 82B30]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(statistical_thermodynamics)
---

## Summary

The Gibbs entropy of a [[statistical ensemble|M0JYTP1C8B]] with probabilities $p_i$ is $S = -k_B \sum_i p_i \ln p_i$, where $k_B$ is the Boltzmann constant.
It measures how spread out the distribution over microstates is.
For the uniform distribution on $W$ microstates it equals $k_B \ln W$, which is [[Boltzmann's entropy formula|QMSMPVY8ED]].
Up to the factor $k_B$ and the base of the logarithm, it is the Shannon entropy of information theory.

## Explanations

### L1 human

Entropy measures how much we do not know about the exact microstate.
If the system is surely in one state, the entropy is $0$.
If it is equally likely to be in any of $W$ states, the entropy is $k_B \ln W$, and this is the largest possible value with $W$ states.
For a fair coin, $S = k_B \ln 2$; for a coin that lands heads with probability $0.9$, the entropy is smaller, about $0.33 \, k_B$.
