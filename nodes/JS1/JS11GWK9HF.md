---
tag: JS11GWK9HF
kind: concept
name: Huffman coding
msc: [94A45, 94A29, 68P30]
specializes: [GNB3T6TD0M]
sources:
  - url: https://en.wikipedia.org/wiki/Huffman_coding
same_as:
  wikidata: Q2647
  wikipedia: Huffman coding
---

## Summary

Huffman coding builds a prefix code for a finite source with known symbol probabilities.
It repeatedly merges the two least likely symbols into one, which builds a code tree from the leaves up.
The resulting code has the smallest expected codeword length among all uniquely decodable codes for the source.
It is a basic step in many file and image compression formats.

## Explanations

### L1 human

Frequent letters should get short codewords and rare letters long ones.
Huffman's idea is to start with the two rarest letters: they will differ only in their last bit, so treat them as one combined letter.
Repeat until only one letter is left, then read the codewords off the tree of merges.
For probabilities $1/2, 1/4, 1/8, 1/8$ this gives the codewords $0, 10, 110, 111$.
The average length is $1.75$ bits instead of the $2$ bits of a fixed-length code.
