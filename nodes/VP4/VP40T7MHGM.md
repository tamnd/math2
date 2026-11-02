---
tag: VP40T7MHGM
kind: concept
name: Romberg's method
msc: [65D30, 65B05, 41A55]
sources:
  - url: https://en.wikipedia.org/wiki/Romberg%27s_method
same_as:
  wikidata: Q1078449
  wikipedia: Romberg's method
---

## Summary

Romberg's method computes a definite integral by applying [[Richardson extrapolation|WMTZG71K2Y]] again and again to the [[trapezoidal rule|FH0538XCZR]] with step sizes $h, h/2, h/4, \dots$.
It works because the error of the trapezoidal rule for a smooth function has an expansion in even powers of $h$.
This expansion comes from the [[Euler–Maclaurin formula|9P839VB8S7]].
Each extrapolation step removes one more term of this expansion.
The results are arranged in a triangular table whose diagonal converges fast for smooth integrands.

## Explanations

### L1 human

The trapezoidal rule is crude, but its error shrinks in a very regular way when the step is halved.
Since the leading error is about four times smaller after halving, a suitable combination of two results cancels it.
Repeating this trick removes the next error term, then the next one.
For example, combining the trapezoidal values for $1$ and $2$ subintervals in this way gives exactly Simpson's rule.
