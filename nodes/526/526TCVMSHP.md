---
tag: 526TCVMSHP
kind: concept
name: Fredholm integral equation
msc: [45B05]
specializes: [AYZCKG34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
same_as:
  wikidata: Q2991898
  wikipedia: Fredholm integral equation
---

## Summary

A Fredholm integral equation is a [[linear integral equation|AYZCKG34QK]] whose integral runs over a fixed set, such as $[a, b]$.
The upper limit is not the variable $x$.
It comes in a [[first kind|2RMWAVR1HV]], $\int_a^b K(x, s) \varphi(s) \, ds = f(x)$, and a [[second kind|DEYYNVCV9J]], $\varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds$.
For the second kind with a continuous or square-integrable kernel, [[Fredholm theory|242TFD41KZ]] gives a complete picture of solvability.
This picture is much as for square systems of linear equations.
[[Boundary value problems|TM8VQJWGHZ]] for differential equations lead to Fredholm equations through [[Green's functions|SH6JY9RN2E]].

## Explanations

### L1 human

In a Fredholm equation, the value of the unknown at each point depends on its values on the whole interval.
This is unlike a [[Volterra integral equation|DND8CBEVXT]], where only the values up to the current point matter.
A Fredholm equation behaves like a very large square system of linear equations.
For example, $\varphi(x) = x + \int_0^1 x s \, \varphi(s) \, ds$ is a Fredholm equation of the second kind on $[0, 1]$, with solution $\varphi(x) = 3x/2$.
