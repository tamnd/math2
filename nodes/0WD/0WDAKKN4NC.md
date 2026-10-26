---
tag: 0WDAKKN4NC
kind: counterexample
name: x^2 sin(1/x) is differentiable with discontinuous derivative
msc: [26A24]
uses: [0A61B60B5R, 06SKCHDQT5, 0Q5A47J48D]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_function
    locator: Differentiability classes
---

## Counterexample

Let $f(x) = x^2 \sin(1/x)$ for $x \ne 0$, and let $f(0) = 0$.
Then $f$ is [[differentiable|0A61B60B5R]] on $\mathbb{R}$, but $f'$ is not continuous at $0$.
At $0$, the difference quotient is $h \sin(1/h)$, which tends to $0$. So $f'(0) = 0$.
For $x \ne 0$, $f'(x) = 2 x \sin(1/x) - \cos(1/x)$. This has no limit as $x \to 0$, because $\cos(1/x)$ has none.

## Remarks

So $f$ is differentiable but not [[of class $C^1$|06SKCHDQT5]].
The discontinuity of $f'$ at $0$ is essential. By [[Darboux's theorem|0Q5A47J48D]], a derivative can have no jump discontinuities.

## Explanations

### L1 human

The factor $x^2$ flattens the oscillation of $\sin(1/x)$ enough to give a slope $0$ at the origin.
But near the origin the slopes keep swinging between about $-1$ and $1$.
