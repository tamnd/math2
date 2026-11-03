---
tag: QYP4KYN248
kind: concept
name: Dirac bracket
msc: [70H45, 53D17]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_bracket
same_as:
  wikidata: Q3895805
  wikipedia: Dirac bracket
---

## Summary

The Dirac bracket is a modification of the [[Poisson bracket|2S0MXDT4YH]] adapted to a set of second class constraints.
With it, the constraints have zero bracket with every function, so they can be imposed as strong equations before computing brackets.
It gives the correct bracket on the constraint surface and is the starting point for quantizing constrained systems.
It is used together with the classification into [[first class and second class constraints|SV6K39RSA6]].
See the [[definition|5VACZTEGNB]].

## Explanations

### L1 human

Suppose the variables $q_2$ and $p_2$ are both forced to be zero.
Then they are not real variables, and the bracket should forget about them.
The ordinary Poisson bracket still contains the term $\{q_2, p_2\} = 1$, which contradicts setting both to zero.
The Dirac bracket subtracts a correction so that the pair $(q_2, p_2)$ drops out and only the remaining variables are seen.
In this simple case, the Dirac bracket is just the Poisson bracket in the variables $(q_1, p_1)$.
