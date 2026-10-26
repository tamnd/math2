---
tag: 0C4VWBFY73
kind: definition
name: Bernstein polynomial
msc: [41A10]
defines: 0JT92VK307
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
    locator: Definition
---

## Definition

Let $f \colon [0, 1] \to \mathbb{R}$ be a function and let $n \ge 1$ be an integer.
The $n$-th Bernstein polynomial of $f$ is
$$B_n(f)(x) = \sum_{k=0}^{n} f\Big( \frac{k}{n} \Big) \binom{n}{k} x^k (1 - x)^{n-k}.$$
The polynomials $b_{k,n}(x) = \binom{n}{k} x^k (1 - x)^{n-k}$ are the Bernstein basis polynomials.

## Remarks

If $f$ is continuous, then $B_n(f) \to f$ uniformly on $[0, 1]$. This proves the [[Weierstrass approximation theorem|0JQE130DHW]].
The basis polynomials are nonnegative on $[0, 1]$, and they sum to $1$ by the binomial theorem.
Sergei Bernstein gave this proof in 1912, with an argument from probability. Mathlib defines the basis polynomials as `bernsteinPolynomial`.

## Explanations

### L1 human

The Bernstein polynomial samples $f$ at the points $k/n$ and blends the values with smooth weights.
Near $x$, the weights concentrate on the samples with $k/n$ close to $x$.
