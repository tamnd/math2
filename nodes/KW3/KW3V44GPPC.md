---
tag: KW3V44GPPC
kind: concept
name: Algorithmic randomness
msc: [03D32, 68Q30]
sources:
  - url: https://en.wikipedia.org/wiki/Algorithmically_random_sequence
---

## Summary

Algorithmic randomness makes precise which individual infinite binary sequences are random.
The standard notion is Martin-Löf randomness.
It calls a sequence random if it passes every effective statistical test, that is, if it avoids every effectively given set of measure zero.
Almost every sequence, in the sense of the uniform measure, is random in this sense, while no computable sequence is.
The notion connects computability, probability and [[Kolmogorov complexity|8PY3K6NCKF]].

## Explanations

### L1 human

Probability theory says that a fair coin produces "typical" sequences, but it does not say which single sequence is random.
The sequence $000\ldots$ is as likely as any other, yet nobody would call it random.
Algorithmic randomness says a sequence is random if no computer program can find a pattern in it that a fair coin would rarely produce.
Equivalently, its first $n$ bits cannot be compressed much, for every $n$.
