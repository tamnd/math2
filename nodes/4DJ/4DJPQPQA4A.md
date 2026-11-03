---
tag: 4DJPQPQA4A
kind: concept
name: Communication complexity
msc: [68Q11, 68Q17]
sources:
  - url: https://en.wikipedia.org/wiki/Communication_complexity
same_as:
  wikidata: Q5154130
  wikipedia: Communication complexity
---

## Summary

Communication complexity measures how many bits two parties must exchange to compute a function of their joint input.
Each party sees only its own part of the input and has unlimited computing power.
The model was introduced by Andrew Yao in 1979.
Lower bounds in this model give lower bounds for circuits, data structures, streaming algorithms and other models.

## Explanations

### L1 human

Alice holds a string $x$ and Bob holds a string $y$, both of $n$ bits.
They want to know whether $x = y$, and they pay for every bit they send.
Alice can send all of $x$, which costs $n$ bits, and Bob answers with one bit.
One can show that no deterministic method uses fewer bits in the worst case.
With shared randomness, however, comparing a few random parities of the strings is enough to be right with high probability.
