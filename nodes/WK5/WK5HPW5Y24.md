---
tag: WK5HPW5Y24
kind: concept
name: Smoothness classes
msc: [26A24, "26E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothness
    locator: Differentiability classes
---

## Summary

The smoothness classes $C^0, C^1, C^2, \ldots, C^\infty$ sort functions by how many continuous derivatives they have.
A function of class $C^k$ has $k$ derivatives, and the $k$-th one is continuous.
The classes are nested, each strictly inside the one before, and their intersection is the class $C^\infty$ of [[smooth functions|0V33BNKZ9S]].
Theorems in analysis and geometry state their hypotheses in terms of these classes.

## Explanations

### L1 human

Some functions are continuous but have corners, like $\abs{x}$.
Some have a derivative, but the derivative has a corner, like $x \abs{x}$, whose derivative is $2\abs{x}$.
Counting how many times you can differentiate before a corner shows up gives the smoothness class.
So $\abs{x}$ is of class $C^0$, $x\abs{x}$ is of class $C^1$, and a polynomial is of class $C^\infty$.
