---
tag: 8TXKFC5PRD
kind: concept
name: Generator matrix
msc: [94B05]
specializes: [0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Generator_matrix
same_as:
  wikidata: Q1502046
  wikipedia: Generator matrix
---

## Summary

A generator matrix of a [[linear code|E85KREWV60]] is a matrix whose rows form a [[basis|0KCQ9Y3QKA]] of the code.
For an $[n, k]$ code over $\F_q$ it is a $k \times n$ matrix $G$, and the codewords are exactly the products $mG$ with $m \in \F_q^k$.
So it gives the encoding map, from messages of $k$ symbols to codewords of $n$ symbols.
A generator matrix in the form $(I_k \mid P)$ gives a systematic encoding, in which the message appears in the first $k$ positions of the codeword.

## Explanations

### L1 human

A linear code may have a huge number of codewords, but a generator matrix lists only a few of them, one per row.
Every codeword is a sum of some of these rows, with coefficients from the field.
To encode a message, write it as a row vector and multiply it by the matrix.
For example, the matrix with the single row $(1, 1, 1)$ over $\F_2$ generates the code $\set{000, 111}$: the message $0$ gives $000$ and the message $1$ gives $111$.
