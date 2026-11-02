---
tag: EPG6JPVJE7
kind: concept
name: Unilateral Z-transform
msc: [44A55, 39A06]
specializes: [5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Unilateral Z-transform
---

## Summary

The unilateral Z-transform of a sequence $(x_n)$ uses only its terms with $n \ge 0$: $X(z) = \sum_{n \ge 0} x_n z^{-n}$.
It is the form of the [[Z-transform|5FY0JQGHYZ]] used for initial value problems.
A forward shift of the sequence brings in its first terms, so initial values enter the transformed equation by themselves.
It plays for difference equations the part that the one-sided Laplace transform plays for differential equations.

## Explanations

### L1 human

Many processes start at a time zero, and only the values from then on matter.
The unilateral Z-transform ignores everything before time zero.
For $x_n = 2^n$ it gives $\sum_{n \ge 0} 2^n z^{-n} = z/(z - 2)$, valid when $\abs{z} > 2$.
Its set of convergence is always the outside of a circle centred at $0$, possibly together with some points of that circle.
It can also be empty or the whole plane without $0$.
