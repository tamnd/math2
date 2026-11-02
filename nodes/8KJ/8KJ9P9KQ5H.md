---
tag: 8KJ9P9KQ5H
kind: concept
name: Matching pursuit
msc: [41A46, 94A12, 41A65]
sources:
  - url: https://en.wikipedia.org/wiki/Matching_pursuit
same_as:
  wikidata: Q6786281
  wikipedia: Matching pursuit
---

## Summary

Matching pursuit is a greedy algorithm that builds an approximation of a vector from a dictionary of unit vectors, one element at a time.
At each step it picks the dictionary element most correlated with the current residual and removes the projection of the residual on that element.
It gives a cheap way to compute [[n-term approximations|GEK0NP5WQM]] and [[sparse approximations|WC8P971XGW]] when the exact problem is too hard.
A variant, orthogonal matching pursuit, re-projects onto all chosen elements at each step.

## Explanations

### L1 human

Imagine explaining a sound with a few notes from a large catalogue.
Matching pursuit first picks the note that matches the sound best, subtracts it, and then repeats with what is left.
Each step makes the leftover part shorter, because a component of it is removed.
In $\R^2$ with the dictionary $e_1$, $e_2$ and $u = (e_1 + e_2)/\sqrt{2}$, the vector $f = (2, 1)$ first picks $u$, since $\ip{f}{u} = 3/\sqrt{2}$ is the largest correlation.
The leftover $(1/2, -1/2)$ then needs both $e_1$ and $e_2$, so the greedy method uses three elements, while $f = 2e_1 + e_2$ needs only two.
