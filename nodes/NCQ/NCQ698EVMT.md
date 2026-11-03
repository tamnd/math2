---
tag: NCQ698EVMT
kind: concept
name: Sardinas–Patterson algorithm
msc: [94A45, 68P30, 68Q45]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Sardinas%E2%80%93Patterson_algorithm
same_as:
  wikidata: Q7423792
  wikipedia: Sardinas–Patterson algorithm
---

## Summary

The Sardinas–Patterson algorithm decides whether a finite code is uniquely decodable.
It tracks the "dangling suffixes" that remain when two different sequences of codewords start the same string.
The code fails to be uniquely decodable exactly when some dangling suffix is itself a codeword.
Since only finitely many suffixes of codewords exist, the algorithm always stops.

## Explanations

### L1 human

Suppose two different chains of codewords spell the same text.
Line them up: at each step one chain is ahead of the other by some leftover piece of a codeword.
The algorithm lists all such leftover pieces that can occur.
If a leftover piece can be closed off by a whole codeword, two different decodings exist.
For $\set{0, 01, 10}$ the leftover $1$ from $0$ versus $01$ leads to the leftover $0$, a codeword, and indeed $010$ reads as $0 \mid 10$ or as $01 \mid 0$.
