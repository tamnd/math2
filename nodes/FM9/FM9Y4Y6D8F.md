---
tag: FM9Y4Y6D8F
kind: concept
name: Stein equation
msc: [15A24, 39B42, 93D05]
specializes: [92GVPZH9FT]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_equation
---

## Summary

The Stein equation is the linear matrix equation $X - AXA^* = Q$ for an unknown square matrix $X$.
It is the discrete-time form of the [[Lyapunov equation|92GVPZH9FT]].
When every eigenvalue of $A$ has absolute value less than $1$, it has the unique solution $X = \sum_{k \ge 0} A^k Q (A^*)^k$.
This links the stability of the recursion $x_{k+1} = A^* x_k$ with positive definite solutions of a linear equation.

## Explanations

### L1 human

Consider a system that updates its state by a matrix at each time step.
The Stein equation asks for a quadratic energy that drops by a prescribed amount $Q$ at each step.
For one variable with $A = 1/2$ and $Q = 3$, the equation $X - X/4 = 3$ gives $X = 4$.
The solution adds up the contributions of $Q$ over all future steps, which is finite exactly when the system decays.
