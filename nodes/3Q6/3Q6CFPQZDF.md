---
tag: 3Q6CFPQZDF
kind: concept
name: Thue equation
msc: [11D59, 11D41]
specializes: [08B1RTW7VZ]
sources:
  - url: https://en.wikipedia.org/wiki/Thue_equation
same_as:
  wikidata: Q2378270
  wikipedia: Thue equation
---

## Summary

A Thue equation is a [[Diophantine equation|08B1RTW7VZ]] $f(x, y) = m$ with $m$ a nonzero integer.
Here $f$ is an irreducible homogeneous polynomial in two variables, with integer coefficients and degree at least $3$.
Axel Thue proved in 1909 that such an equation has only finitely many integer solutions.
His proof came from a sharpening of Liouville's bound on rational approximation of algebraic numbers, the line that led to the [[Thue–Siegel–Roth theorem|R9JZA3G2NX]].
Later, [[Baker's theorem|WMBJSNG57F]] gave explicit bounds on the solutions.

## Explanations

### L1 human

Take an equation such as $x^3 - 2y^3 = 1$ and look for whole number solutions.
If $(x, y)$ is a large solution, then $x/y$ is an extremely good rational approximation of $\sqrt[3]{2}$.
Thue showed that algebraic numbers like $\sqrt[3]{2}$ cannot have too many such good approximations.
So there are only finitely many solutions.
For degree $2$ this fails: the Pell equation $x^2 - 2y^2 = 1$ has infinitely many solutions.
