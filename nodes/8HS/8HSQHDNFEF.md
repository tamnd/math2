---
tag: 8HSQHDNFEF
kind: definition
name: Central difference
msc: [39A70, 65D25]
defines: BVGYDP6YKF
uses: [CYW8E2HTWN, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Definition

Let $f \colon \R \to \R$ be a function and let $h > 0$.
The *central difference* of $f$ with step $h$ is the function $\delta_h f \colon \R \to \R$ given by
$$\delta_h f(x) = f\left(x + \tfrac{h}{2}\right) - f\left(x - \tfrac{h}{2}\right).$$

## Remarks

It is the [[finite difference|7JSQZ126BP]] with offsets $-\tfrac{h}{2}$ and $\tfrac{h}{2}$.
Example: for $f(x) = x^3$, $\delta_h f(x) = 3hx^2 + \tfrac{h^3}{4}$, by expanding both cubes.
Non-example: $f(x + h) - f(x)$ is not centred at $x$, so it is the forward difference and not the central difference.
For sequences one often uses the version $f(x + h) - f(x - h)$ with step $2h$, which avoids half-integer points.
If $f$ is three times continuously differentiable, Taylor's theorem gives $\frac{f(x + h) - f(x - h)}{2h} = f'(x) + O(h^2)$ as $h \to 0$.
