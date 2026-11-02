---
tag: 7MZGZFQ347
kind: concept
name: Quadratic functional equation
msc: [39B52, 39B22]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
---

## Summary

The quadratic functional equation is the [[functional equation|SRAN4EKWS0]] $f(x + y) + f(x - y) = 2 f(x) + 2 f(y)$.
The unknown $f$ maps an abelian group, usually a real vector space, to the real numbers.
Every [[quadratic form|0RBQS1JJCR]] solves it, and on $\R$ the continuous solutions are the functions $f(x) = cx^2$.
It is the functional form of the [[parallelogram law|026HPGYGS4]], and it lies behind the [[Jordan–von Neumann theorem|46WGVM5VS6]].

## Explanations

### L1 human

For $f(x) = x^2$ the equation is the identity $(x + y)^2 + (x - y)^2 = 2x^2 + 2y^2$.
For the squared length of vectors it is the parallelogram law: the squares of the two diagonals add up to the squares of the four sides.
The equation asks which functions behave like a square in this sense.
Its solutions are exactly the functions of the form $f(x) = B(x, x)$ for a symmetric biadditive map $B$.
