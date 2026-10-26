---
tag: 0FNKFT8H6E
kind: concept
name: Total derivative
aliases: [derivative-of-a-map-between-euclidean-spaces, differential-of-a-map]
msc: [26B05]
uses: [0XPR1E85W0, 06EH97V2A7, 047NDTEPCV]
sources:
  - url: https://en.wikipedia.org/wiki/Derivative_(multivariable_calculus)
    locator: Derivative as a linear map
  - url: https://en.wikipedia.org/wiki/Derivative_(multivariable_calculus)
    locator: Total derivative
same_as:
  wikidata: Q636889
  wikipedia: Derivative (multivariable calculus)
---

## Summary

Let $f$ map an open subset of $\mathbb{R}^n$ to $\mathbb{R}^m$. The total derivative of $f$ at a point $a$ is the linear map $Df(a) \colon \mathbb{R}^n \to \mathbb{R}^m$ that best approximates $f$ near $a$. That is, $f(a + h) = f(a) + Df(a)(h) + o(\|h\|)$ as $h \to 0$.
It is the [[Fréchet derivative|06EH97V2A7]] in the case of [[Euclidean spaces|0XPR1E85W0]].
Its matrix in the standard bases is the [[Jacobian matrix|047NDTEPCV]] of $f$ at $a$.

## Remarks

The total derivative accounts for changes in all variables at once. A partial derivative accounts for a change in one variable only.
When $f$ depends on $t$ both directly and through other functions of $t$, the total derivative $\dfrac{d}{dt} f(t, x(t))$ is the sum $\dfrac{\partial f}{\partial t} + \dfrac{\partial f}{\partial x} \dfrac{dx}{dt}$, by the [[chain rule|0EAAS2EHDR]].

## Explanations

### L1 human

For a function of one variable, the derivative at a point is a number: the slope of the tangent line.
For a function of several variables, the derivative at a point is a linear map: it tells how the output changes for each small step in any direction.
