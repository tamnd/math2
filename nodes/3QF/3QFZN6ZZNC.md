---
tag: 3QFZN6ZZNC
kind: concept
name: NC
msc: [68Q15, 68Q06, 68Q10]
specializes: [ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/NC_(complexity)
same_as:
  wikidata: Q1141840
  wikipedia: NC (complexity)
---

## Summary

NC, Nick's class, is the [[complexity class|ESPYW94XGR]] of problems decided by uniform families of [[Boolean circuits|SQXNFGVADX]] of polynomial size and polylogarithmic depth.
Its circuits use gates with at most two inputs.
It is the standard formal notion of a problem that can be solved very fast in parallel with a reasonable number of processors.
It is split into levels $\mathrm{NC}^i$, of depth $O(\log^i n)$.
It is contained in [[P|GVT2NKN37K]], and it is a major open question whether $\mathrm{NC} = \mathrm{P}$.

## Explanations

### L1 human

Some tasks split into many small pieces that can be done at the same time.
Adding up $n$ numbers is an example: add them in pairs, then add the pairs in pairs, and so on, which takes about $\log n$ rounds.
NC collects the problems that can be solved this way in a number of rounds that is a power of $\log n$, using polynomially many processors.
Problems that are complete for P, such as evaluating a given circuit, are believed not to be in NC: they seem inherently sequential.
