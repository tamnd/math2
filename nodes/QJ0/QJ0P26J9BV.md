---
tag: QJ0P26J9BV
kind: concept
name: Overdetermined system
msc: [15A06, 65F20]
specializes: [0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Overdetermined_system
same_as:
  wikidata: Q331348
  wikipedia: Overdetermined system
---

## Summary

An overdetermined system is a [[system of linear equations|0GT4WWGWH2]] with more equations than unknowns.
Such a system usually has no solution; a system with no solution is called [[inconsistent|0X6V9B1V10]].
Overdetermined systems arise whenever many measurements are fitted with a model that has few parameters.
The method of [[least squares|0BYTQ4X1HC]] then finds the vector that comes closest to solving all equations.

## Explanations

### L1 human

Each equation is a condition, and each unknown is a freedom.
With more conditions than freedoms, the conditions usually contradict each other.
Picture three lines in the plane: two lines usually meet in a point, but a third line usually misses that point.
For example, $x + y = 2$, $x - y = 0$ and $x + 2y = 4$ have no common solution, because the first two force $x = y = 1$ and then $x + 2y = 3$.
