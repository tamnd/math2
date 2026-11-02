---
tag: YJ1JWF6ZDG
kind: concept
name: Lommel function
msc: [33C10]
sources:
  - url: https://en.wikipedia.org/wiki/Lommel_function
same_as:
  wikidata: Q2279929
  wikipedia: Lommel function
---

## Summary

The Lommel functions $s_{\mu,\nu}$ and $S_{\mu,\nu}$ are particular solutions of Bessel's equation with right-hand side $z^{\mu + 1}$.
They contain the [[Struve function|K290RBT8GB]] and the [[Anger function|9P87VQZ0P7]] as special cases, up to adding Bessel functions.
They give a common frame for the inhomogeneous Bessel equations met in physics.

## Explanations

### L1 human

Bessel's equation with zero right-hand side has the Bessel functions as solutions.
If the right-hand side is a power $z^{\mu+1}$, one needs one extra solution to describe all the others.
The Lommel function $s_{\mu,\nu}$ is such a solution, written as a power series that starts with $z^{\mu+1}$.
For example, with $\mu = 1$ and $\nu = 0$ the constant $1$ already solves the equation, since $z^2 \cdot 0 + z \cdot 0 + z^2 \cdot 1 = z^2$.
The Lommel function is the solution that starts with $\frac{z^2}{4}$, namely $s_{1,0}(z) = 1 - J_0(z)$.
