---
tag: 0MH1WK89PP
kind: statement
role: corollary
name: Derivative of a polynomial
msc: [26A24]
uses: [0JZGW75C5Z, 0M0TKFRX2A]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial
    locator: Calculus
---

## Statement

Let $p(x) = \sum_{k=0}^{n} a_k x^k$ with real coefficients $a_k$.
Then $p$ is differentiable on $\mathbb{R}$, and
$$p'(x) = \sum_{k=1}^{n} k a_k x^{k-1}.$$

## Remarks

It follows from the [[power rule|0JZGW75C5Z]] and the [[linearity of differentiation|0M0TKFRX2A]].
So the derivative of a polynomial of degree $n \ge 1$ is a polynomial of degree $n - 1$.
Mathlib states it as `Polynomial.hasDerivAt`.

## Explanations

### L1 human

We differentiate a polynomial term by term with the power rule.
For example, the derivative of $3 x^2 + 5 x + 7$ is $6 x + 5$.
