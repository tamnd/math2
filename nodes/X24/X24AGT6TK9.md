---
tag: X24AGT6TK9
kind: concept
name: Horn hypergeometric series
msc: [33C65, 33C70]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_function
---

## Summary

A Horn hypergeometric series is a double power series $\sum_{m, n} A_{m, n} x^m y^n$ with a special kind of coefficients.
Moving one step in either index multiplies the coefficient by a rational function of $(m, n)$.
This is the two-variable form of the defining property of the Gauss [[hypergeometric series|428M453CR2]], whose consecutive coefficients have a rational ratio.
Horn classified the convergent series of this type of order two.
His list has 34 essentially distinct series, including the four Appell series and their confluent forms.

## Explanations

### L1 human

In one variable, a hypergeometric series is a power series where each coefficient is the previous one times a fixed rational function of the index.
In two variables the coefficients form a grid, and one can step right (in $m$) or up (in $n$).
Horn's condition asks that each of the two steps multiplies the coefficient by a rational function of the position.
For instance $A_{m, n} = \frac{(m + n)!}{m!\, n!}$, the coefficients of $\sum (x + y)^N$, give the ratios $\frac{m + n + 1}{m + 1}$ and $\frac{m + n + 1}{n + 1}$.
