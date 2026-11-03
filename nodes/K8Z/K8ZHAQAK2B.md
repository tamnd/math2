---
tag: K8ZHAQAK2B
kind: concept
name: Hamming weight
msc: [94B05, 94B25]
sources:
  - url: https://en.wikipedia.org/wiki/Hamming_weight
same_as:
  wikidata: Q5645805
  wikipedia: Hamming weight
---

## Summary

The Hamming weight of a word is the number of its symbols that are different from zero.
For a binary word it is the number of ones.
It is the [[Hamming distance|EP5HNGSXFA]] from the word to the zero word.
For vectors over a field, the distance between two words is the weight of their difference, which makes weights the basic tool for linear codes.
In computing, the Hamming weight of the binary expansion of an integer is called its population count.

## Explanations

### L1 human

Count the ones: the word $10110$ has weight $3$.
If a codeword is sent and the word received differs from it, the difference marks the positions with errors.
The weight of the difference is the number of errors.
In Mathlib the notion is `hammingNorm`.
