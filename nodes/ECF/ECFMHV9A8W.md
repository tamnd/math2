---
tag: ECFMHV9A8W
kind: concept
name: Concatenated code
msc: [94B05, 94B60]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Concatenated_error_correction_code
same_as:
  wikidata: Q5158264
  wikipedia: Concatenated error correction code
---

## Summary

A concatenated code combines two codes: an outer code over a large alphabet and an inner code over a small alphabet.
Each symbol of an outer codeword is encoded by the inner code, and the results are written one after another.
The distance of the result is at least the product of the two distances, and the decoding can be done in two stages.
Forney introduced concatenated codes in 1966 to get long codes with good error correction and efficient decoding.
The construction underlies [[Justesen codes|FM4SW5DB8T]] and many practical systems.

## Explanations

### L1 human

The outer code protects a message written in large symbols, for example bytes.
Each byte is then turned into a short bit string by a small inner code, which is cheap to decode by brute force.
Most inner blocks decode correctly, and the outer code repairs the few blocks that do not.
For example, a [[Reed–Solomon code|5VBWJ7EFTX]] over $\F_{256}$ as outer code and an $8$-bit-to-$16$-bit inner binary code give a binary code.
