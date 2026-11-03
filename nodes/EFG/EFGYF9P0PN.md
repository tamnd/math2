---
tag: EFGYF9P0PN
kind: concept
name: Block code
msc: [94B25, 94B05]
specializes: [TAE6K8NQ46]
sources:
  - url: https://en.wikipedia.org/wiki/Block_code
same_as:
  wikidata: Q884707
  wikipedia: Block code
---

## Summary

A block code is an [[error-correcting code|TAE6K8NQ46]] in which every message is encoded as a word of the same length $n$ over a finite alphabet.
The code is the set of these codewords, a subset of the [[Hamming space|6E7ZZ4DYX3]] of words of length $n$.
Its main parameters are the length, the number of codewords and the [[minimum distance|M2X88AXM17]], which measure cost, information and robustness.
Most classical codes, such as Hamming codes and Reed–Solomon codes, are block codes; convolutional codes are not.

## Explanations

### L1 human

A block code cuts the data into blocks and replaces each block by a longer codeword of fixed length.
The extra symbols add redundancy, which lets the receiver detect or correct errors.
For example, the even-weight code of length $3$ adds a parity bit to each block of $2$ bits: $00 \mapsto 000$, $01 \mapsto 011$, $10 \mapsto 101$, $11 \mapsto 110$.
Any single flipped bit makes the number of ones odd, so it is detected.
