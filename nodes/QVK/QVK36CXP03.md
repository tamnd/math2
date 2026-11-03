---
tag: QVK36CXP03
kind: concept
name: Shapley value
msc: [91A12]
sources:
  - url: https://en.wikipedia.org/wiki/Shapley_value
same_as:
  wikidata: Q240046
  wikipedia: Shapley value
---

## Summary

The Shapley value is a rule that shares the worth of a [[cooperative game|39HGM44CFZ]] among its players.
Each player receives her average marginal contribution, taken over all orders in which the players could join the grand coalition.
Lloyd Shapley showed that it is the only sharing rule that satisfies four natural axioms: efficiency, symmetry, the null player property and additivity.
It is used in cost sharing, in the measurement of voting power, and to explain the predictions of statistical models.

## Explanations

### L1 human

Imagine the players arriving one at a time and each one receiving what her arrival adds to the group already present.
The result depends on the order of arrival, so the Shapley value averages over all orders.
Suppose two partners earn $10$ together, the first earns $4$ alone and the second earns nothing alone.
The first gets $4$ or $10$ depending on the order, and the second gets $6$ or $0$.
Averaging gives $7$ to the first and $3$ to the second.
