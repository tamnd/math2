---
tag: MWBRNBXW1Y
kind: concept
name: Uniquely decodable code
msc: [94A45, 68P30]
specializes: [BACPE6MVPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Variable-length_encoding
---

## Summary

A uniquely decodable code is a code in which every concatenation of codewords can be split back into codewords in only one way.
This is the least one asks of a code for messages, since otherwise the receiver cannot recover the message.
Prefix codes are uniquely decodable, and the [[Kraft–McMillan inequality|G1ZAWMBNE1]] shows that both classes allow exactly the same lists of codeword lengths.

## Explanations

### L1 human

A code replaces each letter of a message by a codeword and writes the codewords one after the other, with no separators.
The code is uniquely decodable when the receiver can always undo this.
The binary code $\set{0, 01, 11}$ is uniquely decodable, although one may have to read far ahead to split a string.
The code $\set{0, 1, 01}$ is not: the string $01$ is either the single codeword $01$ or the codeword $0$ followed by $1$.
