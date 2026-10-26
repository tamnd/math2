---
tag: 07ZMX4ANJS
kind: statement
role: proposition
name: Differentiable functions are continuous
msc: [26A24]
uses: [0A61B60B5R, 0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_function
    locator: Differentiability and continuity
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \mathbb{R}$, and let $a \in I$.
If $f$ is [[differentiable|0A61B60B5R]] at $a$, then $f$ is [[continuous at|0EEE2CZB2A]] $a$.

## Remarks

For $x \ne a$, write $f(x) - f(a) = \frac{f(x) - f(a)}{x - a} \cdot (x - a)$. The first factor tends to $f'(a)$ and the second to $0$.
The converse fails. The [[absolute value|0CQ9ZM383N]] is continuous but not differentiable at $0$. The [[Weierstrass function|01A0MK1730]] is continuous and nowhere differentiable.
Mathlib states it as `HasDerivAt.continuousAt`.

## Explanations

### L1 human

If a graph has a tangent line at a point, it cannot jump there.
A jump would make the slopes of the secant lines blow up.
