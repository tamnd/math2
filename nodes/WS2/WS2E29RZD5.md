---
tag: WS2E29RZD5
kind: concept
name: Solution of recurrences by generating functions
msc: [39A06, 05A15]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function
---

## Summary

This method turns a recurrence for a sequence $(u_n)$ into an equation for its [[generating function|0PHAC833JF]] $U(x) = \sum_{n \ge 0} u_n x^n$.
For a linear recurrence with constant coefficients, the equation is linear and its solution $U$ is a rational function.
Expanding $U$ again, for example by partial fractions, gives a closed formula for $u_n$.
The method is a standard tool of enumerative combinatorics and of the analysis of algorithms.

## Explanations

### L1 human

A sequence is an infinite list of numbers, which is hard to handle at once.
Packing the whole list into one power series turns the step-by-step rule into an algebraic equation.
For example, if $u_0 = 1$ and $u_{n+1} = 2 u_n$, then $U(x) - 1 = 2 x U(x)$.
So $U(x) = 1/(1 - 2x) = \sum 2^n x^n$, and $u_n = 2^n$.
