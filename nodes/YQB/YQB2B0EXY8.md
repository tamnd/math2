---
tag: YQB2B0EXY8
kind: concept
name: Functional inequality
msc: [39B62, 39B72]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Summary

A functional inequality is an inequality between expressions in an unknown function.
It is required to hold for all values of the variables.
It is the inequality analogue of a [[functional equation|SRAN4EKWS0]].
Standard examples are subadditivity $f(x + y) \le f(x) + f(y)$ and midpoint convexity $f\big(\tfrac{x + y}{2}\big) \le \tfrac{f(x) + f(y)}{2}$.
Typical questions are which functions satisfy a given inequality, and when mild regularity forces its solutions to be nice.

## Explanations

### L1 human

A functional equation asks for functions that make two expressions equal everywhere; a functional inequality only asks that one expression is never larger than the other.
For example, the inequality $f(x + y) \le f(x) + f(y)$ says that the value at a sum is at most the sum of the values.
The square root on $[0, \infty)$ satisfies it, while the squaring map does not.
Convex functions, norms and many quantities in probability and analysis are described by such inequalities.
