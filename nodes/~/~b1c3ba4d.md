---
tag: ~b1c3ba4d
kind: statement
role: proposition
name: Slopes of a convex function are increasing
msc: [26A51]
uses: [~aaa9779c]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
    locator: Functions of one variable
---

## Statement

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be [[convex|~aaa9779c]].
Then for all $x < y < z$ in $I$,
$$\frac{f(y) - f(x)}{y - x} \le \frac{f(z) - f(x)}{z - x} \le \frac{f(z) - f(y)}{z - y}.$$

## Remarks

Write $y = t x + (1 - t) z$ with $t = (z - y)/(z - x)$, and apply the definition of convexity.
The converse holds: a function with this property is convex.
The first and the last quotient give the adjacent form `ConvexOn.slope_mono_adjacent` of Mathlib.

## Explanations

### L1 human

For a convex function, chords further to the right are steeper.
So the slopes of the graph increase from left to right.
