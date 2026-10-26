---
tag: ~faf292cd
kind: statement
role: corollary
name: Derivative of a polynomial
msc: [26A24]
uses: [~df6921ca, ~b5467eee]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial
    locator: Calculus
---

## Statement

Let $p(x) = \sum_{k=0}^{n} a_k x^k$ with real coefficients $a_k$.
Then $p$ is differentiable on $\mathbb{R}$, and
$$p'(x) = \sum_{k=1}^{n} k a_k x^{k-1}.$$

## Remarks

It follows from the [[power rule|~df6921ca]] and the [[linearity of differentiation|~b5467eee]].
So the derivative of a polynomial of degree $n \ge 1$ is a polynomial of degree $n - 1$.
Mathlib states it as `Polynomial.hasDerivAt`.

## Explanations

### L1 human

We differentiate a polynomial term by term with the power rule.
For example, the derivative of $3 x^2 + 5 x + 7$ is $6 x + 5$.
