---
tag: BVGYDP6YKF
kind: concept
name: Central difference
msc: [39A70, 65D25]
specializes: [7JSQZ126BP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Summary

The central difference of a function $f$ with step $h$ is $\delta_h f(x) = f(x + \tfrac{h}{2}) - f(x - \tfrac{h}{2})$.
It is symmetric around the point $x$.
For a smooth function, the quotient $\delta_h f(x) / h$ approximates $f'(x)$ with an error of order $h^2$, better than the order $h$ of the one-sided quotients.

## Explanations

### L1 human

To estimate the slope of a curve at a point, you can look a little to the right and a little to the left of it, and compare.
The central difference does exactly this, with the point in the middle.
For $f(x) = x^2$ and step $h$ the result is $(x + h/2)^2 - (x - h/2)^2 = 2hx$.
Dividing by $h$ gives $2x$, which is the exact derivative, while a one-sided difference gives $2x + h$.
