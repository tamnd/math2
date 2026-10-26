---
tag: 0TNZC55X3J
kind: counterexample
name: Partial derivatives do not imply differentiability
msc: [26B05]
uses: [09EGC6F8PT, 0HHHDCXZV4, 0C0KPAKK9Y]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_derivative
    locator: Definition
---

## Counterexample

One could guess that a function of several variables is differentiable at a point when all its partial derivatives exist there.
This is false.
Let $f \colon \mathbb{R}^2 \to \mathbb{R}$ be given by $f(x, y) = \dfrac{xy}{x^2 + y^2}$ for $(x, y) \ne (0, 0)$ and $f(0, 0) = 0$.
Both [[partial derivatives|09EGC6F8PT]] of $f$ exist at $(0, 0)$, and both are $0$.
But $f$ is not continuous at $(0, 0)$, so $f$ is not [[differentiable|0HHHDCXZV4]] at $(0, 0)$.

## Remarks

The function is $0$ on both axes, so $f(h, 0) = f(0, h) = 0$ for each $h$, and both difference quotients at the origin are $0$.
On the line $y = x$ the value is $1/2$, so $f$ is not continuous at the origin, as in the [[separately continuous function|0C0KPAKK9Y]]. A function that is differentiable at a point is continuous there.
Even all directional derivatives are not enough. For $g(x, y) = x^2 y / (x^4 + y^2)$ off the origin and $g(0, 0) = 0$, each directional derivative at the origin exists, but $g = 1/2$ on the parabola $y = x^2$ minus the origin.
If the partial derivatives exist near the point and are continuous at it, then the function is differentiable, by the [[criterion with continuous partial derivatives|0KXSK8TEEB]].

## Explanations

### L1 human

The partial derivatives look only along the two axes.
A function can be flat on both axes and still do something wild between them, here on the diagonal.
Differentiability asks for a good linear approximation in all directions at once, which is much more.
