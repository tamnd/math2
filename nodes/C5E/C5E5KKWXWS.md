---
tag: C5E5KKWXWS
kind: concept
name: Mackey–Glass equation
msc: [92C30, 34K60, 34K23]
specializes: [39PCDRDB01]
sources:
  - url: https://en.wikipedia.org/wiki/Mackey%E2%80%93Glass_equations
same_as:
  wikidata: Q104847195
  wikipedia: Mackey–Glass equations
---

## Summary

The Mackey–Glass equation is a scalar nonlinear [[delay differential equation|39PCDRDB01]].
Michael Mackey and Leon Glass proposed it as a model of the production of blood cells.
The rate of production depends on the state a fixed time $\tau$ earlier, which models the time needed for cells to mature.
For large delays its solutions can oscillate and even behave chaotically, so it is a standard example of [[chaos|DBKXCGDKTD]] in a one-dimensional equation with delay.

## Explanations

### L1 human

The body makes new blood cells in response to a signal, but the new cells take days to mature.
So the production today answers the number of cells some days ago.
Such a delayed feedback tends to overshoot: the body makes too many cells, then too few, and so on.
The Mackey–Glass equation turns this story into a formula, and for long delays it produces irregular, chaotic oscillations.
This was offered as an explanation of some blood diseases with oscillating cell counts.
