---
tag: MGACY98E9H
kind: object
name: Hermite polynomials
msc: [33C45, "12E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite_polynomials
same_as:
  wikidata: Q658574
  wikipedia: Hermite polynomials
---

## Description

The (physicists') Hermite polynomials are the polynomials $H_n \in \Z[x]$, $n \ge 0$, given by
$$H_n(x) = (-1)^n e^{x^2} \frac{d^n}{dx^n} e^{-x^2}.$$
Equivalently, $H_0 = 1$, $H_1 = 2x$ and $H_{n+1} = 2x \, H_n - 2n \, H_{n-1}$ for $n \ge 1$.
The probabilists' Hermite polynomials $\operatorname{He}_n$ use the weight $e^{-x^2/2}$ instead: $\operatorname{He}_n(x) = (-1)^n e^{x^2/2} \frac{d^n}{dx^n} e^{-x^2/2}$.

## Remarks

The first values are $H_2 = 4x^2 - 2$, $H_3 = 8x^3 - 12x$, and $\operatorname{He}_2 = x^2 - 1$, $\operatorname{He}_3 = x^3 - 3x$.
Check for $H_2$ with the recursion: $2x \cdot 2x - 2 \cdot 1 \cdot 1 = 4x^2 - 2$.
The polynomial $H_n$ has degree $n$ and leading coefficient $2^n$, while $\operatorname{He}_n$ is monic.
The two families are related by $H_n(x) = 2^{n/2} \operatorname{He}_n(\sqrt{2} \, x)$.
They are orthogonal on $\R$: $\int_{-\infty}^{\infty} H_m(x) H_n(x) e^{-x^2} \, dx = \sqrt{\pi} \, 2^n n! \, \delta_{mn}$.
They satisfy $H_n' = 2n \, H_{n-1}$ and $\operatorname{He}_n' = n \operatorname{He}_{n-1}$.
In quantum mechanics, the eigenfunctions of the harmonic oscillator are $H_n(x) e^{-x^2/2}$ up to scaling.

## Explanations

### L1 human

Differentiate the bell curve $e^{-x^2}$ again and again.
Each derivative is a polynomial times $e^{-x^2}$, and up to sign these polynomials are the Hermite polynomials.
They are the natural polynomials to use when the weight is a Gaussian bell curve.
