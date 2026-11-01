---
tag: 92GVPZH9FT
kind: concept
name: Lyapunov equation
msc: [15A24, 93D05, 34D20]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_equation
same_as:
  wikidata: Q1028945
  wikipedia: Lyapunov equation
---

## Summary

The Lyapunov equation is the linear matrix equation $AX + XA^* + Q = 0$, or its discrete form $AXA^* - X + Q = 0$, for an unknown matrix $X$.
Its solutions give quadratic [[Lyapunov functions|01REYCJ371]] for the linear system $x' = A^* x$ or $x_{k+1} = A^* x_k$.
Every eigenvalue of $A$ has negative real part exactly when the continuous equation with a positive definite $Q$ has a positive definite solution.
So the equation turns [[Lyapunov stability|0F2SYCKDT2]] into linear algebra.
The continuous form is a special case of the [[Sylvester equation|M9SW4NVP2H]].

## Explanations

### L1 human

To show that a system comes to rest, one looks for an energy that always decreases along its motion.
For a linear system the natural energies are quadratic, $x^* X x$ for a matrix $X$.
The Lyapunov equation is the condition on $X$ that makes this energy decrease at a prescribed rate.
For one variable $x' = ax$ with $a < 0$, the energy $x^2$ decreases, and the equation $2aX + q = 0$ has the positive solution $X = -q/(2a)$ for $q > 0$.
