---
tag: AX0NJ6NK81
kind: concept
name: Augmented Lagrangian method
msc: [90C30, 49M29, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Augmented_Lagrangian_method
same_as:
  wikidata: Q4820432
  wikipedia: Augmented Lagrangian method
---

## Summary

The augmented Lagrangian method, also called the method of multipliers, solves constrained problems by adding a quadratic penalty to the Lagrangian.
It alternates between minimizing this augmented Lagrangian in the primal variables and updating estimates of the [[Lagrange multipliers|0VKKP8X6Q6]].
Unlike the pure [[penalty method|AY9Q1VNDJB]], under standard hypotheses it converges without sending the penalty parameter to infinity, which avoids ill-conditioning.
It was introduced by Hestenes and by Powell in 1969, and it underlies the alternating direction method of multipliers.

## Explanations

### L1 human

A penalty method charges a fine for breaking a constraint, but it needs a huge fine to get the answer exactly right.
The augmented Lagrangian method also keeps a price for each constraint, the multiplier, and adjusts it after each round.
If the last answer broke the constraint in one direction, the price is shifted to push it back.
With the right prices, a moderate fine already gives the exact answer.
