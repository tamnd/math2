---
tag: ZH2S50NSZ6
kind: concept
name: Oscillation theory
msc: [34C10]
sources:
  - url: https://en.wikipedia.org/wiki/Oscillation_theory
same_as:
  wikidata: Q289610
  wikipedia: Oscillation theory
---

## Summary

Oscillation theory studies the zeros of solutions of differential equations, above all of second-order linear equations $(p y')' + q y = 0$.
Its main questions are whether solutions have infinitely many zeros, how the zeros are spaced, and how the zeros of different solutions are related.
The theory started with the comparison and separation theorems of Charles Sturm.
It gives criteria in terms of the coefficients, and it is linked to [[Sturm–Liouville theory|7WV6B2502K]], where the $n$-th eigenfunction has $n - 1$ zeros.

## Explanations

### L1 human

A solution oscillates if it crosses the axis again and again, without end, like a sine wave.
Oscillation theory asks which equations force their solutions to behave like this.
The equation $y'' + y = 0$ is oscillatory, since its solutions $A \sin(x + c)$ have infinitely many zeros.
The equation $y'' - y = 0$ is not: its solutions $A e^x + B e^{-x}$ have at most one zero.
For $y'' + q(x) y = 0$, a large positive $q$ means many oscillations, a phenomenon the Sturm comparison theorem makes precise.
