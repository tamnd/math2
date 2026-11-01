---
tag: GGZV75ZZMV
kind: concept
name: Algebraic Riccati equation
msc: [15A24, 49N10, 93C05]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_Riccati_equation
same_as:
  wikidata: Q4723989
  wikipedia: Algebraic Riccati equation
---

## Summary

An algebraic Riccati equation is a quadratic matrix equation for an unknown symmetric matrix $X$, such as $A^T X + XA - XBR^{-1}B^T X + Q = 0$.
It is the steady state of the matrix Riccati differential equation.
Its stabilising solution gives the optimal feedback of the linear-quadratic regulator and the gain of the steady-state Kalman filter.
Without the quadratic term it reduces to a [[Lyapunov equation|92GVPZH9FT]].

## Explanations

### L1 human

A controller wants to steer a linear system to rest while keeping both the error and the effort small.
The best policy feeds back the state through a matrix gain, and that gain comes from a matrix $X$ solving a Riccati equation.
The equation is quadratic in $X$, like $ax^2 + bx + c = 0$ for numbers, so it can have several solutions.
For one variable with $A = 0$ and $B = Q = R = 1$, it reads $1 - x^2 = 0$, and the useful solution is $x = 1$.
