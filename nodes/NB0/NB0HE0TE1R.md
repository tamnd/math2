---
tag: NB0HE0TE1R
kind: definition
name: Distribution function of a measurable function
msc: [28A20, "46E30"]
defines: HQVXKEMN5N
uses: [P15VQS5DJ9, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Layer_cake_representation
---

## Definition

Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]].
Let $f \colon X \to \C$ or $f \colon X \to [-\infty, \infty]$ be a [[measurable function|YYNCJSR0PJ]].
The *distribution function* of $f$ is the function $d_f \colon [0, \infty) \to [0, \infty]$ given by
$$d_f(t) = \mu(\set{x \in X : \abs{f(x)} > t}).$$

## Remarks

Example: let $X = [0, 1]$ with Lebesgue measure and $f(x) = x^2$.
For $0 \le t < 1$ the set $\set{x : x^2 > t}$ is $(\sqrt{t}, 1]$, so $d_f(t) = 1 - \sqrt{t}$.
For $t \ge 1$ the set is empty, so $d_f(t) = 0$.

Non-example: the cumulative distribution function $F(t) = \mu(\set{f \le t})$ of probability theory is a different object.
It measures where $f$ is small, uses $f$ and not $\abs{f}$, and is increasing rather than decreasing.

The function $d_f$ is non-increasing and right-continuous.
Two functions with the same distribution function are called *equimeasurable*, and they have the same $L^p$ norms.
Some authors write $\lambda_f$ or $\mu_f$ for $d_f$.
