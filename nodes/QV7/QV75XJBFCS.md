---
tag: QV75XJBFCS
kind: concept
name: Lebesgue–Stieltjes measure
msc: [28A12, 26A42]
specializes: [DYR1QFNGNJ]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue%E2%80%93Stieltjes_integration
---

## Summary

A Lebesgue–Stieltjes measure is a measure on the real line built from a non-decreasing, right-continuous function $F$, so that the interval $(a, b]$ gets measure $F(b) - F(a)$.
Every locally finite Borel measure on $\R$ arises this way.
For $F(x) = x$ it is Lebesgue measure, and for the distribution function of a random variable it is the law of that variable.
Integration against it is Lebesgue–Stieltjes integration, which extends the Riemann–Stieltjes integral.

## Explanations

### L1 human

Think of $F(x)$ as the total mass lying to the left of $x$ on a line.
Then the mass of the interval $(a, b]$ is $F(b) - F(a)$.
Where $F$ grows fast, there is a lot of mass, and where $F$ jumps, there is a point mass equal to the jump.
For example, if $F(x) = 0$ for $x < 0$ and $F(x) = 1$ for $x \ge 0$, the measure is a single unit mass at $0$.
