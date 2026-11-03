---
tag: E1F970GGRC
kind: concept
name: Wolfe conditions
msc: [90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Wolfe_conditions
same_as:
  wikidata: Q3002999
  wikipedia: Wolfe conditions
---

## Summary

The Wolfe conditions are two inequalities that a step length must satisfy in an inexact [[line search|B6T5HA74QW]].
The first, the Armijo condition, asks for a sufficient decrease of the function.
The second, the curvature condition, rules out steps that are too short.
They are the standard acceptance test in quasi-Newton methods such as BFGS, and they guarantee global convergence results of Zoutendijk type.

## Explanations

### L1 human

When you walk downhill along a fixed direction, a good stopping point should be lower than the start by a definite margin.
It should also be far enough that the slope has flattened out somewhat.
The first Wolfe condition asks for the first property and the second Wolfe condition asks for the second.
For $f(x) = x^2$ from $x = 1$ in the direction $-1$, the step to the bottom, $x = 0$, passes both tests, while a tiny step of length $0.01$ fails the second.
