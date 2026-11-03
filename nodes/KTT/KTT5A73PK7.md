---
tag: KTT5A73PK7
kind: concept
name: Lovász extension
msc: [90C27, 90C25, 05B35]
sources:
  - url: https://en.wikipedia.org/wiki/Submodular_set_function
---

## Summary

The Lovász extension turns a function on the subsets of an $n$-element set into a function on $\R^n$.
It agrees with the set function on the $0$-$1$ vectors.
It is piecewise linear, and on each region where the coordinates have a fixed order it is linear.
Lovász proved that the extension is a [[convex function|07Q7CNM5WF]] exactly when the set function is [[submodular|4WQA9XFA52]].
This bridge lets methods of convex optimization minimize submodular functions.

## Explanations

### L1 human

A set function only knows values at the corners of the cube $[0, 1]^n$, one corner for each subset.
The Lovász extension fills in the cube by sorting the coordinates of a point and walking from the empty set to the full set in that order.
Each step adds one element and is weighted by the corresponding coordinate.
For the cut function of a single edge between elements $1$ and $2$, the extension is $\abs{x_1 - x_2}$.
It is $1$ at the corners $(1, 0)$ and $(0, 1)$ and $0$ at the other two.
That function is convex, as the theorem predicts for a submodular function.
