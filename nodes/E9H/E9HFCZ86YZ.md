---
tag: E9HFCZ86YZ
kind: concept
name: Expander code
msc: [94B05, 05C48]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Expander_code
same_as:
  wikidata: Q5420758
  wikipedia: Expander code
---

## Summary

An expander code is a [[linear code|E85KREWV60]] defined by parity checks along a bipartite [[expander graph|DXJXVFV79H]]: bits sit on one side, checks on the other.
Expansion forces every small set of bits to touch many checks, so no small nonzero set of bits can satisfy all checks.
Hence the [[minimum distance|M2X88AXM17]] is a constant fraction of the length.
Sipser and Spielman showed in 1996 that, with enough expansion, a simple bit-flipping algorithm corrects a constant fraction of errors in linear time.
Expander codes thus give asymptotically good codes with linear-time decoding.

## Explanations

### L1 human

Imagine bits on the left and checks on the right, each bit wired to a few checks.
If any small group of bits is wired to many different checks, then flipping a few bits always breaks some check, so a corrupted word cannot pass as a codeword.
Moreover, a bit that sits in many broken checks is likely to be wrong, so flipping such bits one by one repairs the word.
For example, the six edges of the complete graph $K_4$ as bits and its four vertices as checks give an expander code of length $6$ and distance $3$.
