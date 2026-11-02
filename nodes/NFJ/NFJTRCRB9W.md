---
tag: NFJTRCRB9W
kind: concept
name: Three-term recurrence relation
msc: [39A06, 33C45]
specializes: [8Y28JQB0Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrence_relation
---

## Summary

A three-term recurrence relation is a linear recurrence of order two that links three consecutive terms $u_{n+1}$, $u_n$ and $u_{n-1}$.
It is the simplest recurrence beyond first order and appears throughout analysis.
[[Orthogonal polynomials|8TXASARQN1]] satisfy one, and so do the numerators and denominators of [[continued fractions|04P2RJ4WPS]] and many special functions.
Its solutions form a two-dimensional space, which leads to the study of minimal and dominant solutions.

## Explanations

### L1 human

Each new term is built from the two terms just before it, with coefficients that may change with $n$.
The Fibonacci rule $u_{n+1} = u_n + u_{n-1}$ is the simplest example.
The Chebyshev polynomials obey $T_{n+1}(x) = 2x\, T_n(x) - T_{n-1}(x)$, which lets you compute them one after another from $T_0 = 1$ and $T_1 = x$.
