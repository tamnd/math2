---
tag: K5RXH32SE7
kind: concept
name: Dirichlet series as Mellin transforms
msc: [11M41, 44A15, 30B50]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_series
---

## Summary

A [[Dirichlet series|8MWTEF6462]] $F(s) = \sum_{n \ge 1} a(n) n^{-s}$ can be written as a [[Mellin transform|N5PVGRJE1T]] in two standard ways.
First, $\Gamma(s) F(s)$ is the Mellin transform of the exponential sum $\sum_n a(n) e^{-nx}$.
Second, $F(s)/s$ is the Mellin transform at $-s$ of the summatory function $A(x) = \sum_{n \le x} a(n)$.
These identities let one study Dirichlet series with the tools of integral transforms: analytic continuation, inversion formulas such as Perron's formula, and asymptotics through residues.

## Explanations

### L1 human

The basic fact is $\int_0^\infty x^{s-1} e^{-nx} \, dx = \Gamma(s) n^{-s}$.
So a sum of exponentials $\sum a(n) e^{-nx}$ has a Mellin transform equal to $\Gamma(s)$ times the Dirichlet series with the same coefficients.
For $a(n) = 1$ the exponential sum is $1/(e^x - 1)$, and the identity becomes $\int_0^\infty x^{s-1}/(e^x - 1) \, dx = \Gamma(s)\zeta(s)$ for $\operatorname{Re} s > 1$.
Going back by Mellin inversion recovers information on the coefficients from the analytic behaviour of $F$.
