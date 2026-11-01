---
tag: D6D0SR1FK3
kind: concept
name: Polynomial long division
msc: [13F20, 68W30]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_long_division
same_as:
  wikidata: Q1068675
  wikipedia: Polynomial long division
---

## Summary

Polynomial long division is the algorithm that divides a polynomial $f$ by a polynomial $g$ with invertible leading coefficient.
It produces the quotient $q$ and the remainder $r$ with $f = q g + r$ and $\deg r < \deg g$.
These are the quotient and remainder of the [[division algorithm for polynomials|0MES3KS0ZC]].
It is the basic step of the [[Euclidean algorithm|023VY493K0]] for polynomials and of many computations in algebra.

## Explanations

### L1 human

It works like long division of integers, with degrees in place of digits.
At each step you divide the leading term of what is left by the leading term of $g$.
You write this term in the quotient, subtract its product with $g$, and go on.
For example, dividing $x^2 + 1$ by $x - 1$ gives the quotient $x + 1$ and the remainder $2$, since $x^2 + 1 = (x + 1)(x - 1) + 2$.
The [[definition|FTAK2F0TR3]] gives the steps.
