---
tag: WF08BMN6Q6
kind: concept
name: Aitken's delta-squared process
msc: [65B05, 40A25]
specializes: [B1S2XJPGYD]
sources:
  - url: https://en.wikipedia.org/wiki/Aitken's_delta-squared_process
same_as:
  wikidata: Q492177
  wikipedia: Aitken's delta-squared process
---

## Summary

Aitken's delta-squared process is a [[series acceleration|B1S2XJPGYD]] method that replaces three consecutive terms of a sequence by one improved estimate of its limit.
It is exact for sequences whose error is exactly geometric.
It speeds up sequences whose error is close to geometric, such as those from [[fixed-point iteration|K6ZF91051B]].
It is the first case of the [[Shanks transformation|C0TXDZZMH7]].

## Explanations

### L1 human

If the distance to the limit shrinks by the same factor at each step, three consecutive terms are enough to find the factor and hence the limit.
Aitken's process does this calculation and returns the limit it predicts.
For $s_n = 1 + 2^{-n}$ it returns exactly $1$ from any three consecutive terms.
For sequences whose errors are only nearly geometric, the predictions are not exact but approach the limit much faster than the original terms.
