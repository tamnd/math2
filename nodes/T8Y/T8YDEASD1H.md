---
tag: T8YDEASD1H
kind: concept
name: Rational difference equation
msc: [39A20, 39A05]
specializes: [7C7FBZGERM]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_difference_equation
same_as:
  wikidata: Q7295762
  wikipedia: Rational difference equation
---

## Summary

A rational difference equation is a [[nonlinear difference equation|7C7FBZGERM]] whose next term is a quotient of two affine expressions in the earlier terms.
It is one of the simplest classes of nonlinear recurrences, yet its solutions show convergence, periodicity and unbounded growth depending on the parameters.
The first-order case is the iteration of a [[Möbius transformation|0SG74WBFA2]] and can be solved in closed form by reduction to a linear recurrence.
Higher-order cases are studied mainly through the stability and periodicity of their solutions.

## Explanations

### L1 human

Each new term is a fraction whose top and bottom are linear in the previous terms.
For example $x_{n+1} = 1/(1 + x_n)$ with $x_0 = 1$ gives $1, 1/2, 2/3, 3/5, 5/8, \dots$.
These are ratios of consecutive Fibonacci numbers, and they approach $(\sqrt{5} - 1)/2 \approx 0.618$.
The division makes the rule nonlinear, but in the first-order case a clever change of variables makes it linear again.
