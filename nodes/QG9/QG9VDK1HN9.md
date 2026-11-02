---
tag: QG9VDK1HN9
kind: concept
name: Appell series
msc: [33C65]
specializes: [X24AGT6TK9]
sources:
  - url: https://en.wikipedia.org/wiki/Appell_series
same_as:
  wikidata: Q4780998
  wikipedia: Appell series
---

## Summary

The Appell series $F_1, F_2, F_3, F_4$ are four double power series in two variables $x$ and $y$ that generalise the Gauss [[hypergeometric series|428M453CR2]].
Their coefficients are ratios of [[Pochhammer symbols|YZHM3HSM0F]] in the two summation indices.
Each of them reduces to a Gauss hypergeometric function when one of the variables is $0$.
They appear in integrals of products of powers, in the theory of algebraic curves and in physics.

## Explanations

### L1 human

The Gauss hypergeometric series is a power series in one variable whose coefficients are built from rising factorials.
To get a series in two variables, one lets the rising factorials depend on $m$, on $n$, or on $m + n$, where $x^m y^n$ is the monomial.
There are four natural ways to do this that give genuinely new functions, and these are Appell's four series.
For example $F_1(a; b_1, b_2; c; x, x) = {}_2F_1(a, b_1 + b_2; c; x)$, so on the diagonal $F_1$ collapses back to one variable.
