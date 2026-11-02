---
tag: 9FS1JFZSX4
kind: concept
name: Idempotence
msc: [08A02, 16U40]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotence
same_as:
  wikidata: Q368988
  wikipedia: Idempotence
---

## Summary

Idempotence is the property of something that gives the same result when it is applied twice as when it is applied once.
An element $x$ is idempotent for a [[binary operation|0M418FE7BB]] $\ast$ when $x \ast x = x$, and a function $f$ is idempotent when $f \circ f = f$.
Lattice operations, projections and closure operators are idempotent.
The [[idempotent elements of a ring|0N5NJZKKN3]] are the idempotents for its multiplication.

## Explanations

### L1 human

Pressing the "on" button of a machine that is already on changes nothing; that is idempotence.
In numbers, $\max(x, x) = x$ for every $x$, so the operation $\max$ is idempotent.
Rounding down is an idempotent function: rounding a number that is already an integer leaves it unchanged, so rounding twice is the same as rounding once.
Addition of numbers is not idempotent, because $1 + 1 \ne 1$.
