---
tag: AZJMC8A93H
kind: concept
name: Gomory's fractional cut
msc: [90C10]
specializes: [PR7VMJN5BH]
sources:
  - url: https://en.wikipedia.org/wiki/Cutting-plane_method
---

## Summary

Gomory's fractional cut is a valid inequality for a pure [[integer program|9GX3WH5EQF]].
It is read off from a row of an optimal [[simplex|MH272QHWPM]] tableau whose basic variable has a fractional value.
It keeps only the fractional parts of the coefficients of that row.
Ralph Gomory introduced it in 1958, and with it gave the first [[cutting-plane method|PR7VMJN5BH]] that provably solves pure integer programs in finitely many steps.
Gomory cuts are among the most useful cuts in modern solvers, mostly in their mixed-integer form.

## Explanations

### L1 human

A row of the final simplex table says that one variable equals a fraction minus some combination of the other variables.
If all variables must be nonnegative whole numbers, the fractional parts on both sides must match up in a certain way.
Writing this down gives a new inequality that every whole-number solution satisfies.
The current fractional answer breaks it, so adding it moves the search closer to a whole-number answer.
