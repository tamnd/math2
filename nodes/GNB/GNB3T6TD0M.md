---
tag: GNB3T6TD0M
kind: concept
name: Prefix code
msc: [94A45, 68P30]
specializes: [MWBRNBXW1Y]
sources:
  - url: https://en.wikipedia.org/wiki/Prefix_code
same_as:
  wikidata: Q1278039
  wikipedia: Prefix code
---

## Summary

A prefix code is a code in which no codeword is the beginning of another codeword.
Such a code can be decoded on the fly: one reads symbols until the current block is a codeword, outputs it and starts again.
Every prefix code is uniquely decodable, and by the [[Kraft–McMillan inequality|G1ZAWMBNE1]] nothing is lost in codeword lengths by restricting to prefix codes.

## Explanations

### L1 human

Think of telephone numbers: no valid number is the start of a longer valid number, so the exchange knows when you have finished dialling.
A prefix code works the same way for messages.
The binary code $\set{0, 10, 110, 111}$ is a prefix code.
The string $0110100$ splits in only one way, as $0 \mid 110 \mid 10 \mid 0$, and the reader never needs to look ahead.
