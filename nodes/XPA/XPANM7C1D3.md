---
tag: XPANM7C1D3
kind: concept
name: Nuclear operator
msc: [47B10, 46B28]
sources:
  - url: https://en.wikipedia.org/wiki/Nuclear_operator
same_as:
  wikidata: Q96396744
  wikipedia: Nuclear operator
---

## Summary

A nuclear operator is a bounded linear map between Banach spaces that can be written as an absolutely summable series of rank-one maps.
The notion, due to Grothendieck, extends the trace class operators of Hilbert spaces to Banach spaces.
Nuclear operators are compact, and they are the basis of Grothendieck's theory of nuclear spaces and of trace and determinant theory on Banach spaces.

## Explanations

### L1 human

The simplest operators are those of rank one: measure a vector by a linear functional, then multiply a fixed vector by the result.
A nuclear operator is an infinite sum of such pieces whose sizes add up to a finite number.
So it is a limit of matrices in a strong, summable sense.
For example, on square-summable sequences, multiplying the $n$-th coordinate by $2^{-n}$ is nuclear, since it is the sum of the rank-one pieces $x \mapsto 2^{-n} x_n e_n$ of sizes $2^{-n}$.
