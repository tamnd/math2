---
tag: WAMRHWW82R
kind: concept
name: Laguerre polynomials
msc: [33C45, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre_polynomials
same_as:
  wikidata: Q1124546
  wikipedia: Laguerre polynomials
---

## Summary

The Laguerre polynomials $L_n^{(\alpha)}$ are the [[classical orthogonal polynomials|47WJ34NC9K]] on the half-line $[0, \infty)$ for the weight $x^\alpha e^{-x}$.
The case $\alpha = 0$ gives the ordinary Laguerre polynomials $L_n$.
They solve the Laguerre differential equation.
They appear in the radial wave functions of the hydrogen atom and in Gaussian quadrature on $[0, \infty)$.

## Explanations

### L1 human

On the half-line from $0$ to infinity, the weight $e^{-x}$ gives more importance to small numbers than to large ones.
The Laguerre polynomials are the polynomials that are perpendicular to each other for this weight.
The first ones are $L_0 = 1$, $L_1 = 1 - x$ and $L_2 = \frac{x^2 - 4x + 2}{2}$.
For instance, $L_1$ is perpendicular to $L_0$ because $\int_0^\infty (1 - x) e^{-x} \, dx = 1 - 1 = 0$.
