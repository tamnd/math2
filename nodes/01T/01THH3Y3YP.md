---
tag: 01THH3Y3YP
kind: definition
name: Integrating factor
msc: [34A05]
defines: 07DJAZW32T
uses: [0Z3YKRQZ48]
sources:
  - url: https://en.wikipedia.org/wiki/Integrating_factor
    locator: Solving first order linear ordinary differential equations
---

## Definition

Let $I$ be an open interval, and let $p, q : I \to \mathbb{R}$ be continuous.
An integrating factor of the [[linear first-order equation|0Z3YKRQZ48]] $y' + p(x) y = q(x)$ is a differentiable function $\mu : I \to \mathbb{R}$ with $\mu(x) \ne 0$ for each $x \in I$ and
$$\mu'(x) = p(x)\, \mu(x) \quad \text{for each } x \in I.$$
For such $\mu$ and each differentiable $y$ on $I$, $\mu \left(y' + p y\right) = (\mu y)'$.

## Remarks

If $P$ is an antiderivative of $p$ on $I$, then $\mu(x) = e^{P(x)}$ is an integrating factor. Each integrating factor is a nonzero constant times this one.
After multiplication by $\mu$, the equation becomes $(\mu y)' = \mu q$. One integration gives the [[solution formula|06B9W45XV0]].
More generally, an integrating factor is a function that makes an equation exact after multiplication. See [[integrating factor for a non-exact equation|0CX86CR8JV]].

## Explanations

### L1 human

The left side $y' + p y$ is not the derivative of a simple expression.
After multiplication by the right function $\mu$, it becomes the derivative of $\mu y$, by the product rule.
Then you can integrate both sides directly.
For $y' + y = x$, the factor is $e^x$, and the equation becomes $(e^x y)' = x e^x$.
