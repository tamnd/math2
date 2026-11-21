---
tag: SZZX4B3JMY
kind: example
name: A square system is neither overdetermined nor underdetermined
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: QJ0P26J9BV
    note: The system has as many equations as unknowns, so it is neither overdetermined nor underdetermined
uses: [QJ0P26J9BV, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Overdetermined_system
---

## Example

With as many equations as unknowns, a system sits on the boundary between the two kinds.
Consider the [[system|0GT4WWGWH2]] $x + y = 1$, $x - y = 0$ over $\mathbb{R}$.

1. It has $m = 2$ equations and $n = 2$ unknowns, so it is square.
2. Adding the equations gives $2x = 1$, so $x = \tfrac12$.
3. The second equation then gives $y = \tfrac12$.
4. Check: $\tfrac12 + \tfrac12 = 1$ and $\tfrac12 - \tfrac12 = 0$.

So the system has the unique solution $(\tfrac12, \tfrac12)$, and it is not [[overdetermined or underdetermined|QJ0P26J9BV]].

## Remarks

A square system can also have no solution, as for $x + y = 1$, $x + y = 2$, or infinitely many, as for $x + y = 1$, $2x + 2y = 2$.
So the shape $m = n$ predicts a unique solution only in the usual case, when the matrix is invertible.

## Explanations

### L1 human

Two equations in two unknowns usually fix both unknowns.
Here they fix $x = y = \tfrac12$.

### L2 human

1. Count the equations and the unknowns.
2. If the counts are equal, the system is square.
3. Solve it, and check whether the solution is unique.

Watch out: a square system with an equation that is a combination of the others behaves like an underdetermined one, so the count alone does not promise one solution.
