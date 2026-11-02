---
tag: EHFQK1WXKS
kind: concept
name: Rational approximation
msc: [41A20, 41A21, 41A50]
specializes: [VNWH2KADN7]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_function
---

## Summary

Rational approximation is the approximation of functions by [[rational functions|0XDK9CGYKJ]] $p/q$ with prescribed bounds on the degrees of $p$ and $q$.
Rational functions can imitate poles, steep fronts, and singular points much better than polynomials of the same number of parameters.
A striking case is [[Newman's theorem|JEQVZXHE6A]]: $\abs{x}$ on $[-1, 1]$ has rational approximation error of order $e^{-c\sqrt{n}}$, while polynomials only achieve order $1/n$.
[[Padé approximants|1F16G4V64X]] and best uniform rational approximations are the main constructions.

## Explanations

### L1 human

A polynomial is a sum of powers and can only grow without bound far away; it struggles to follow a function with a sharp corner or a near blow-up.
A quotient of two polynomials has more freedom: its denominator can be small where the function is large.
Rational approximation asks how close such quotients of given degrees can come to a given function.
For example, $1/(1 + 25x^2)$ on $[-1, 1]$ is itself a rational function of degree $2$, but polynomials need high degree to approximate it well.
