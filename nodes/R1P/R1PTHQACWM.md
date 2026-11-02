---
tag: R1PTHQACWM
kind: concept
name: Filtered algebra
msc: [16W70]
specializes: [3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Filtered_algebra
same_as:
  wikidata: Q5449241
  wikipedia: Filtered algebra
---

## Summary

A filtered algebra is an [[associative algebra|3CTW1P4HBP]] with an increasing chain of subspaces $F_0 \subseteq F_1 \subseteq \cdots$ that exhausts it and is compatible with multiplication, $F_i F_j \subseteq F_{i+j}$.
It generalizes a [[graded ring|8KB4SQGC0C]], where elements have an exact degree, to a setting where elements only have a degree "at most $i$".
Each filtered algebra has an [[associated graded|8HFAEGFQT1]] algebra, which is often simpler, and many properties pass from the graded algebra back to the filtered one.
The [[universal enveloping algebra|SCZ8PRVY00]] of a Lie algebra and the [[Weyl algebra|98QE7KY55W]] are the classic examples.

## Explanations

### L1 human

In a polynomial ring every element has a degree, and the degree of a product is at most the sum of the degrees.
A filtered algebra keeps only this rule, measuring "size at most $i$" by the subspace $F_i$.
In a noncommutative algebra, such as the algebra of differential operators, there may be no exact degree, but there is still a sensible notion of order.
Passing to the associated graded algebra forgets the lower-order terms; for differential operators it leaves only the leading symbols, which commute.
