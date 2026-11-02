---
tag: CTMRG74JN0
kind: concept
name: Pexider equation
msc: [39B22, 39B52]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Summary

The Pexider equation is the [[functional equation|SRAN4EKWS0]] $f(x + y) = g(x) + h(y)$ with three unknown functions $f, g, h \colon \R \to \R$.
It generalizes Cauchy's additive equation, which is the case $f = g = h$.
Its solutions are $f = A + a + b$, $g = A + a$ and $h = A + b$, where $A$ is an [[additive function|KF719SZD5T]] and $a, b$ are constants.
Equations of this kind, with several unknown functions in the place of one, are called Pexiderized forms of the classical equations.

## Explanations

### L1 human

The equation asks for three functions that fit together: the first one at a sum is the second at one term plus the third at the other.
Allowing three different functions gives only a little more freedom than Cauchy's equation.
For example, $f(x) = x + 3$, $g(x) = x + 1$ and $h(x) = x + 2$ solve it.
Every solution differs from an additive function only by constant shifts.
