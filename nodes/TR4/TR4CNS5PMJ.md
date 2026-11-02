---
tag: TR4CNS5PMJ
kind: concept
name: Root-finding algorithm
msc: [65H05, 65H04]
sources:
  - url: https://en.wikipedia.org/wiki/Root-finding_algorithm
same_as:
  wikidata: Q1085860
  wikipedia: Root-finding algorithm
---

## Summary

A root-finding algorithm computes approximations of a zero of a function, that is, a point $x$ with $f(x) = 0$.
Most such algorithms are iterative: they produce a sequence of points, or of shrinking intervals, that tends to a zero.
Bracketing methods such as the [[bisection method|7VMYC7MB3Q]] and [[regula falsi|462AEY7MWF]] keep a sign change and always converge for continuous $f$.
Open methods such as [[Newton's method|07EXVNF9VP]] and the [[secant method|9ZC177PVPC]] converge faster near a simple zero, but only from good starting points.
Methods are compared by their [[rate of convergence|YWZQC5E54B]] and by the number of function evaluations per step.

## Explanations

### L1 human

Solving an equation such as $x^3 = x + 1$ means finding where the function $f(x) = x^3 - x - 1$ is $0$.
There is no simple formula for most such equations, so one guesses and improves the guess step by step.
For this $f$, $f(1) = -1 < 0$ and $f(2) = 5 > 0$, so a zero lies between $1$ and $2$, and halving this interval repeatedly closes in on it, near $1.3247$.
Faster methods use the slope of $f$ to jump close to the zero in a few steps.
