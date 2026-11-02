---
tag: 3K1AKGXF8A
kind: concept
name: Robinson arithmetic
msc: [03F30]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
same_as:
  wikidata: Q928884
  wikipedia: Robinson arithmetic
---

## Summary

Robinson arithmetic, often written $\mathsf{Q}$, is a first-order theory of the natural numbers with zero, successor, addition and multiplication.
It has seven axioms and no induction.
It is much weaker than the [[Peano axioms|0QFT7Z76N5]], yet strong enough to represent every computable function.
For this reason the incompleteness theorems and many undecidability results already hold for $\mathsf{Q}$ and every consistent theory that extends it.

## Explanations

### L1 human

Robinson arithmetic keeps only the recursive rules for addition and multiplication and a few facts about successor.
It can check any particular computation, such as $2 + 2 = 4$.
But without induction it cannot prove general laws such as $x + y = y + x$.
Its value is that it is a small, finite list of axioms that still captures all of computation.
