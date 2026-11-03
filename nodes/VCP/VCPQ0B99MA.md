---
tag: VCPQ0B99MA
kind: concept
name: Hankel singular value
msc: [93B11, 93C05, 15A18]
sources:
  - url: https://en.wikipedia.org/wiki/Hankel_singular_value
same_as:
  wikidata: Q5648530
  wikipedia: Hankel singular value
---

## Summary

The Hankel singular values of a stable linear system measure how much each internal state direction matters.
They refer to the map from past inputs to future outputs.
They are the square roots of the eigenvalues of the product of the [[controllability Gramian|703MCKB5SZ]] and the [[observability Gramian|9YEW705KHA]].
They do not depend on the choice of state coordinates, so they are invariants of the [[transfer function|86JKV3TRFD]].
Small Hankel singular values mark states that are both hard to reach and hard to observe.
This is the basis of balanced truncation in model reduction.

## Explanations

### L1 human

Feed a stable system an input in the past, stop, and watch the output in the future.
Some internal states are easy to excite and show up strongly in the output; others barely matter.
The Hankel singular values rank the state directions by this combined importance, from the largest to the smallest.
For $x' = -x + u$, $y = x$ there is one Hankel singular value, equal to $1/2$.
