---
tag: JA3DP8NM0A
kind: concept
name: Dual code
msc: [94B05]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_code
same_as:
  wikidata: Q5310189
  wikipedia: Dual code
---

## Summary

The dual code $C^\perp$ of a [[linear code|E85KREWV60]] $C \subseteq \F_q^n$ is the set of words whose [[dot product|0S52TNNTH9]] with every codeword is zero.
It is again a linear code, of dimension $n - k$ when $C$ has dimension $k$.
A [[generator matrix|8TXKFC5PRD]] of one code is a [[parity-check matrix|Y4JB44WWFG]] of the other.
The [[MacWilliams identity|2QK3T3KATX]] gives the weight distribution of $C^\perp$ from that of $C$.
Codes equal to their dual are called self-dual; the extended Golay codes are examples.

## Explanations

### L1 human

Each word $x$ defines a test on codewords: is the sum of $x_i c_i$ equal to zero?
The dual code collects all the tests that every codeword passes.
For the binary code $\set{000, 111}$, the passing tests are the words with an even number of ones, $000, 011, 101, 110$.
So a small code has a large dual, and a large code has a small dual.
