---
tag: S60JN2XN7A
kind: concept
name: Error exponent
msc: [94A24, 94A40]
sources:
  - url: https://en.wikipedia.org/wiki/Error_exponent
same_as:
  wikidata: Q5395710
  wikipedia: Error exponent
---

## Summary

The error exponent measures how fast the error probability of a good code goes to zero as the block length $n$ grows.
If the error probability behaves like $2^{-nE}$, the number $E$ is the exponent.
For a channel and a rate $R$ below the [[capacity|J7MZ2XQP9M]], the best exponent $E(R)$ is positive, which sharpens the [[noisy-channel coding theorem|PR3NJB0SKG]].
See the [[definition|44NBMJ2689]].

## Explanations

### L1 human

The coding theorem says that long codes can make errors as rare as we like, at any rate below capacity.
The error exponent says how quickly: each extra symbol of block length multiplies the error probability by about $2^{-E}$.
For example, send one bit several times over a noisy binary channel and take a majority vote.
The error probability of this code falls exponentially as the number of repeats grows.
Its exponent is positive but its rate tends to zero.
Good codes keep a positive exponent while also keeping a positive rate, and the exponent shrinks to zero as the rate approaches capacity.
