---
tag: MKFKFTPMXZ
kind: concept
name: Kolmogorov quotient
msc: [54D10, 54B15]
specializes: [0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_space
---

## Summary

The Kolmogorov quotient of a topological space identifies any two points that no open set can tell apart.
The result is a [[T0 space|07SG12TQH3]], and its open sets correspond exactly to the open sets of the original space.
It lets one pass to a $T_0$ space without losing any topological information.
For a pseudometric space it gives the associated metric space.

## Explanations

### L1 human

In some spaces, two different points have exactly the same neighbourhoods.
No open set contains one of them without the other, so the topology cannot see the difference.
The Kolmogorov quotient glues such twin points into one point.
For example, on $\R^2$ with the pseudometric $d((x_1, y_1), (x_2, y_2)) = \abs{x_1 - x_2}$, points on the same vertical line are twins.
Gluing them gives the real line.
