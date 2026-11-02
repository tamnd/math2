---
tag: AM4RNWVV4Q
kind: concept
name: Symbol class
msc: [35S05, 47G30]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_operator
  - url: https://en.wikipedia.org/wiki/Pseudo-differential_operator
---

## Summary

A symbol class is a space of smooth functions $a(x, \xi)$ of a position $x$ and a frequency $\xi$.
Its elements grow or decay like a fixed power of $\abs{\xi}$, and their derivatives in $\xi$ decay faster.
The standard classes are the Hörmander classes $S^m_{\rho, \delta}$, where $m$ is the order.
Symbols generalise the polynomials $\sum_\alpha a_\alpha(x) \xi^\alpha$ attached to differential operators.
They are the building blocks of pseudo-differential operators and of Fourier integral operators.

## Explanations

### L1 human

A differential operator such as $\partial_x^2 + 1$ acts on a wave $e^{ix\xi}$ by multiplying it by the polynomial $1 - \xi^2$, its symbol.
Allowing more general functions of $\xi$ in place of polynomials leads to more general operators, for example a square root of $1 - \Delta$.
To keep a good calculus one asks that the symbol behaves like a power $\abs{\xi}^m$ for large $\xi$, and that each derivative in $\xi$ lowers this power by one.
For instance $(1 + \abs{\xi}^2)^{s/2}$ is a symbol of order $s$.
