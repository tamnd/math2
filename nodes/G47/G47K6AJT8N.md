---
tag: G47K6AJT8N
kind: concept
name: Min-entropy
msc: [94A17, 94A60]
specializes: [AQHZ1HXXYB]
sources:
  - url: https://en.wikipedia.org/wiki/Min-entropy
same_as:
  wikidata: Q17103874
  wikipedia: Min-entropy
---

## Summary

The min-entropy of a discrete random variable $X$ is $H_\infty(X) = -\log \max_x P(X = x)$.
It is the [[Rényi entropy|AQHZ1HXXYB]] of order $\infty$ and the smallest of all Rényi entropies, so it is at most the [[Shannon entropy|Y86E072V0V]].
It measures how hard $X$ is to guess in one try: the best single guess is right with probability $2^{-H_\infty(X)}$ in bits.
For this reason it is the measure of randomness used in cryptography and in the theory of randomness extractors.

## Explanations

### L1 human

Min-entropy looks only at the most likely outcome.
If an attacker may make one guess at a secret, the best guess is the most likely value, and the min-entropy says how unlikely even this guess is to succeed.
A secret with min-entropy $k$ bits can be guessed in one try with probability at most $2^{-k}$.
For example, a password that is "123456" with probability $\frac14$ and otherwise spread over a million values has min-entropy only $2$ bits, even though its Shannon entropy is large.
