---
tag: GQBX1XFNG2
kind: concept
name: Lempel–Ziv coding
msc: [68P30, 94A29]
sources:
  - url: https://en.wikipedia.org/wiki/LZ77_and_LZ78
same_as:
  wikidata: Q22670963
  wikipedia: LZ77 and LZ78
---

## Summary

Lempel–Ziv coding is a family of compression methods that replace repeated pieces of a text by references to earlier occurrences.
The two original versions, LZ77 and LZ78, were published by Abraham Lempel and Jacob Ziv in 1977 and 1978.
They need no knowledge of the source statistics, yet for stationary ergodic sources the compression rate of LZ78 tends to the entropy rate.
Many widely used compression formats are built on them.

## Explanations

### L1 human

A long text repeats itself: words, phrases and patterns come back again and again.
Instead of writing a repeated piece out, the coder writes "copy the piece seen earlier, and add this letter".
LZ78 cuts the text into phrases, each one being an earlier phrase plus one new letter.
The text $1011010100010$ cuts into $1, 0, 11, 01, 010, 00, 10$, and each phrase is sent as a pair (number of an earlier phrase, new bit).
