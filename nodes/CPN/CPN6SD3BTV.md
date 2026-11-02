---
tag: CPN6SD3BTV
kind: concept
name: Round-off error
msc: [65G50]
sources:
  - url: https://en.wikipedia.org/wiki/Round-off_error
same_as:
  wikidata: Q2145211
  wikipedia: Round-off error
---

## Summary

Round-off error, or rounding error, is the difference between the exact result of a computation and the result computed with [[rounded|5NPVX29Y0C]] numbers.
In [[floating-point arithmetic|RTKRSC3KPH]] each single rounding has relative error at most the unit roundoff, about $10^{-16}$ in double precision.
Many roundings can add up, and a subtraction of nearly equal numbers can magnify them, as in [[catastrophic cancellation|TJPNYW7J8E]].
It is distinct from [[truncation error|4AKCQERM89]], which comes from the method even in exact arithmetic.

## Explanations

### L1 human

A computer keeps only a fixed number of digits, so it must round almost every result.
Each rounding error is tiny, but a long computation does millions of operations.
Sometimes the errors cancel each other, and sometimes they pile up.
A classic example: adding $0.1$ ten times in double precision does not give exactly $1$, because $0.1$ is rounded when stored and again after each addition.
