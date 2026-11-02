---
tag: 3TWMBFQJJ8
kind: concept
name: Closable operator
msc: [47A05, 47B25]
specializes: [KRJX5RA0PW]
sources:
  - url: https://en.wikipedia.org/wiki/Unbounded_operator
---

## Summary

A closable operator is an unbounded operator that has a closed extension.
Many operators are first defined on a convenient small domain, such as smooth functions, and are not closed there.
If they are closable, they have a smallest closed extension, the closure, which is the operator one actually studies.

## Explanations

### L1 human

Sometimes a formula is written down only for nice inputs, and the resulting operator is not closed.
One then tries to enlarge the domain by taking limits, keeping the rule that limits of inputs go with limits of outputs.
This works when the same input limit can never come with two different output limits.
For example, differentiation on polynomials, in the space $C[0, 1]$ with the supremum norm, is closable, and its closure is differentiation on continuously differentiable functions.
