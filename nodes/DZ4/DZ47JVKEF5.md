---
tag: DZ47JVKEF5
kind: concept
name: Integral equation of the third kind
msc: [45A05, 45H05]
specializes: [AYZCKG34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Summary

An integral equation of the third kind is a [[linear integral equation|AYZCKG34QK]] $a_0(x) \varphi(x) = f(x) + \lambda \int K(x, s) \varphi(s) \, ds$ whose coefficient $a_0$ vanishes at some points but not everywhere.
It sits between the [[first kind|ZDS77Q0F06]], where $a_0 = 0$, and the [[second kind|8KJCN49V64]], where $a_0 = 1$.
Near the zeros of $a_0$ the equation behaves like one of the first kind, so its solutions may be singular there.
Such equations occur in transport theory and in some problems of mathematical physics.

## Explanations

### L1 human

The unknown appears outside the integral with a weight $a_0(x)$.
Where the weight is not zero one can divide by it and get an ordinary equation of the second kind.
At the points where the weight is zero this division fails, and the solution can blow up or need not exist.
For example, $x \varphi(x) = f(x) + \int_{-1}^{1} \varphi(s) \, ds$ on $[-1, 1]$ is of the third kind, since $x$ vanishes at $0$.
