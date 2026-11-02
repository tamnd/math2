---
tag: DCSXXT4SER
kind: concept
name: Congruence relation
msc: [08A30]
specializes: [0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence_relation
same_as:
  wikidata: Q8349849
  wikipedia: Congruence relation
---

## Summary

A congruence relation on an [[algebra|QJGPT2W0FT]] is an [[equivalence relation|0G8VEZ3WTK]] that is compatible with all the operations.
Replacing elements by congruent ones never changes the class of the result.
Congruences are exactly the relations that allow a [[quotient algebra|N5KE7FH6CX]], and they are exactly the kernels of homomorphisms.
In groups they correspond to normal subgroups, and in rings to two-sided ideals.

## Explanations

### L1 human

A congruence is a way of declaring some elements "the same" so that the operations still make sense on the classes.
The model is [[congruence modulo n|0WAY5WX8NY]] on the integers: if $a \equiv a'$ and $b \equiv b' \pmod n$, then $a + b \equiv a' + b'$ and $ab \equiv a'b'$.
So one can add and multiply remainders, which gives the ring $\Z/n\Z$.
Not every equivalence relation works: grouping integers by sign is not compatible with addition, since $1 \sim 2$ but $1 + (-1) = 0$ and $2 + (-1) = 1$ have different signs.
