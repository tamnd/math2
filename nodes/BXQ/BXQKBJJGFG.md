---
tag: BXQKBJJGFG
kind: object
name: Bernoulli polynomials
msc: [11B68]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli_polynomials
same_as:
  wikidata: Q2346201
  wikipedia: Bernoulli polynomials
---

## Description

The Bernoulli polynomials are the polynomials $B_n(x) \in \Q[x]$, $n \ge 0$, given by the generating function
$$\frac{t \, e^{x t}}{e^t - 1} = \sum_{n=0}^{\infty} B_n(x) \frac{t^n}{n!}.$$
Equivalently, $B_n(x) = \sum_{k=0}^{n} \binom{n}{k} B_k \, x^{n-k}$, where $B_k$ are the [[Bernoulli numbers|0KC00K7KY4]] with $B_1 = -\frac{1}{2}$.

## Remarks

The first values are $B_0(x) = 1$, $B_1(x) = x - \frac{1}{2}$, $B_2(x) = x^2 - x + \frac{1}{6}$ and $B_3(x) = x^3 - \frac{3}{2} x^2 + \frac{1}{2} x$.
Each $B_n$ is monic of degree $n$, and $B_n(0) = B_n$.
They satisfy $B_n'(x) = n B_{n-1}(x)$ and $B_n(x + 1) - B_n(x) = n x^{n-1}$ for $n \ge 1$.
Summing the second identity gives the sums of powers: for $p \ge 0$ and $m \ge 1$,
$$\sum_{k=0}^{m-1} k^p = \frac{B_{p+1}(m) - B_{p+1}(0)}{p + 1}.$$
Check with $p = 1$, $m = 4$: $\frac{B_2(4) - B_2(0)}{2} = \frac{12}{2} = 6 = 0 + 1 + 2 + 3$.
They also satisfy $B_n(1 - x) = (-1)^n B_n(x)$.

## Explanations

### L1 human

The Bernoulli polynomials are a family of polynomials that turn sums of powers into polynomial formulas.
Their values at $0$ are the Bernoulli numbers.
The difference $B_n(x + 1) - B_n(x)$ is the simple monomial $n x^{n-1}$, which is what makes the sums telescope.
