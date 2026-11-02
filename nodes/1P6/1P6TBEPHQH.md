---
tag: 1P6TBEPHQH
kind: concept
name: Inversion of rational transforms by partial fractions
msc: [44A10, 26C15]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_fraction_decomposition
---

## Summary

A rational function $F(s) = P(s)/Q(s)$ with $\deg P < \deg Q$ is the [[Laplace transform|0V49JEZW06]] of a sum of terms $t^{k-1} e^{a t}$.
To find the [[inverse Laplace transform|07WBTX1MHA]], one splits $F$ by [[partial fraction decomposition|030VFEREKG]] into terms $c/(s - a)^k$ and inverts each term from the rule $\mathcal{L}\{t^{k-1} e^{a t}/(k-1)!\} = 1/(s - a)^k$.
This is the everyday method for the transforms that arise from linear differential equations with constant coefficients.

## Explanations

### L1 human

A complicated fraction in $s$ is hard to invert at once, but simple fractions such as $1/(s - a)$ are easy: they come from $e^{a t}$.
So one first breaks the fraction into simple pieces and then inverts piece by piece.
For example, $\frac{1}{s (s + 1)} = \frac{1}{s} - \frac{1}{s + 1}$, so it is the transform of $1 - e^{-t}$.
Each root $a$ of the denominator gives a term $e^{a t}$ in the answer, and repeated roots give extra powers of $t$.
