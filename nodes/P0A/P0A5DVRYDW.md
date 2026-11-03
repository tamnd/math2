---
tag: P0A5DVRYDW
kind: concept
name: P/poly
msc: [68Q15, 68Q06]
specializes: [ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/P/poly
same_as:
  wikidata: Q7117817
  wikipedia: P/poly
---

## Summary

P/poly is the [[complexity class|ESPYW94XGR]] of languages decided by families of [[Boolean circuits|SQXNFGVADX]] of polynomial size, one circuit for each input length.
Equivalently, it is the class of languages decided in polynomial time with a polynomial-length advice string that depends only on the input length.
It contains [[P|GVT2NKN37K]] and [[BPP|PTD7E1PKV4]], but also some undecidable languages.
Proving that NP is not contained in P/poly would prove $\mathrm{P} \ne \mathrm{NP}$.

## Explanations

### L1 human

A normal algorithm is one program that works for all input sizes.
In P/poly, one may use a different small circuit for each input size, and nobody needs to know how to build these circuits.
This is a non-uniform model: it allows "hints" that can depend on the input length in any way.
Because of this freedom, even a language like "the set of $1^n$ for which the $n$th Turing machine halts" is in P/poly.
