---
tag: 95BSKT0S6M
kind: concept
name: Semi-continuity
msc: [26A15, 54C08]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-continuity
same_as:
  wikidata: Q955072
  wikipedia: Semi-continuity
---

## Summary

A real function is upper semicontinuous at a point if its values near the point cannot jump far above its value at the point.
It is lower semicontinuous if they cannot jump far below.
A function is [[continuous|0P27W9RW0G]] exactly when it is both.
Semicontinuity is the right condition for minimum and maximum problems: a lower semicontinuous function on a nonempty compact space attains its minimum.

## Explanations

### L1 human

Think of the graph of a function with a jump.
Upper semicontinuity allows a jump only if the value at the jump point sits on the upper side.
The floor function $\floor{x}$ jumps up at each integer $n$, and its value there is $n$, the upper value.
So the floor function is upper semicontinuous, but it is not lower semicontinuous.
