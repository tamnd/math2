---
tag: G0S748GZCX
kind: concept
name: Shannon–Fano coding
msc: [94A45, 94A29, 68P30]
specializes: [GNB3T6TD0M]
sources:
  - url: https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding
same_as:
  wikidata: Q2645
  wikipedia: Shannon–Fano coding
---

## Summary

Shannon–Fano coding is the name of two early methods that build a prefix code from the symbol probabilities of a source.
Shannon's method gives each symbol a codeword of length about $\log_2 (1/p)$, read off from the cumulative probabilities.
Fano's method splits the list of symbols into two parts of nearly equal probability and recurses.
Shannon's method gives an expected length within one bit of the entropy.
Neither method always gives the shortest expected length; Huffman coding does.

## Explanations

### L1 human

A symbol with probability $1/8$ should get a codeword of about $3$ bits, because $2^{-3} = 1/8$.
Fano's version plays a game of twenty questions: ask "is the symbol in the first half of the list?", where the halves have about equal probability, and keep asking.
Each answer is one bit of the codeword.
For probabilities $1/2, 1/4, 1/8, 1/8$ both methods give $0, 10, 110, 111$.
