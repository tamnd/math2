---
tag: EHGECREYB4
kind: concept
name: Laplace transform method for convolution equations
msc: [45D05, "45E10", 44A10]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Summary

The Laplace transform method solves a [[Volterra equation of convolution type|SNFYTC1TTA]] on $[0, \infty)$ by turning it into an algebraic equation.
The [[convolution theorem for the Laplace transform|0JNMJEDD93]] changes the convolution $k * x$ into the product $\hat k \, \hat x$ of the transforms.
One solves for $\hat x$ and then inverts the transform.
It is the standard way to find explicit solutions, and also to study the long-time behaviour of solutions.

## Explanations

### L1 human

A convolution equation mixes the unknown with its own past, which makes it hard to solve directly.
After a [[Laplace transform|0V49JEZW06]], the mixing becomes a plain multiplication.
For example, $x(t) = 1 + \int_0^t x(s) \, ds$ becomes $\hat x(p) = \frac1p + \frac1p \hat x(p)$.
So $\hat x(p) = \frac{1}{p - 1}$, which is the transform of $e^t$, and indeed $x(t) = e^t$.
