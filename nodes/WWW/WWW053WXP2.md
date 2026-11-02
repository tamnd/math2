---
tag: WWW053WXP2
kind: concept
name: Riemann P-symbol
msc: ["33C05", "34M03"]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%27s_differential_equation
---

## Summary

The Riemann P-symbol is a notation for the solutions of [[Riemann's differential equation|RS8Z48E784]].
It is a table listing the three singular points, the two exponents at each, and the variable.
Since the equation is determined by these data, the symbol names its whole two-dimensional space of solutions.
Simple rules tell how the symbol changes under a [[Möbius transformation|0SG74WBFA2]] of the variable and under multiplication by powers.
These rules turn many transformation formulas of the [[hypergeometric function|463X5V31D9]] into bookkeeping.

## Explanations

### L1 human

Instead of writing a long differential equation, one writes a small table with three columns.
Each column gives a singular point and the two powers that the solutions show near it.
The table stands for all solutions of the equation with that data.
For example, the hypergeometric function belongs to the table with columns $(0; 0, 1-c)$, $(\infty; a, b)$ and $(1; 0, c-a-b)$.
Moving the points by a Möbius map or multiplying by powers just changes entries of the table in a predictable way.
