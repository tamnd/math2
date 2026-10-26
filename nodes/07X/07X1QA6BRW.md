---
tag: 07X1QA6BRW
kind: statement
role: theorem
name: Derivative of the logarithm
msc: [33B10, 26A24]
uses: [0M0RZ3HSB0, 0EX9GFJ0B3, 0044CPHJBV]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_logarithm
    locator: In calculus
---

## Statement

The [[natural logarithm|0044CPHJBV]] is differentiable on $(0, \infty)$, and
$$\frac{d}{dx} \ln x = \frac{1}{x} \quad \text{for } x > 0.$$

## Remarks

By the [[inverse function rule|0M0RZ3HSB0]] and [[$\exp' = \exp$|0EX9GFJ0B3]], the derivative at $x = e^y$ is $\frac{1}{e^y} = \frac{1}{x}$.
For $x \ne 0$, the derivative of $\ln |x|$ is $1/x$.
By the chain rule, $(\ln f(x))' = f'(x)/f(x)$ when $f > 0$. Mathlib states the main claim as `Real.hasDerivAt_log`.

## Explanations

### L1 human

The slope of the graph of $\ln$ at $x$ is $1/x$.
So the logarithm grows more and more slowly as $x$ gets large.
