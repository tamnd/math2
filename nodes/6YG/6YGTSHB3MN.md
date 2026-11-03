---
tag: 6YGTSHB3MN
kind: concept
name: Coordinate descent
msc: [90C06, 65K05, 90C25]
sources:
  - url: https://en.wikipedia.org/wiki/Coordinate_descent
same_as:
  wikidata: Q5168004
  wikipedia: Coordinate descent
---

## Summary

Coordinate descent minimises a function of several variables by improving one coordinate at a time while the others stay fixed.
Each step is a one-dimensional problem, which is often solvable in closed form and is cheap even in very high dimension.
Under mild conditions it converges for smooth convex functions, and for a smooth convex function plus separable convex terms, as in the lasso.
It can get stuck on general nonsmooth functions.
Random and cyclic choices of the coordinate are both common.

## Explanations

### L1 human

Imagine adjusting a sound mixer with many sliders.
Instead of moving all sliders at once, you move one slider to its best position, then the next, and so on in rounds.
Each move is easy, and for well-behaved objectives the rounds approach the best setting.
For $f(x, y) = x^2 + x y + y^2$, minimising over $x$ with $y$ fixed gives $x = -y/2$, and then over $y$ gives $y = -x/2$; starting from $y = 1$ the values shrink by a factor $4$ each round toward $(0, 0)$.
