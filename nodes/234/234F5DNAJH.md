---
tag: 234F5DNAJH
kind: concept
name: Tricomi confluent hypergeometric function
msc: [33C15]
specializes: [6AZ4ZBN1M8]
sources:
  - url: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
---

## Summary

The Tricomi confluent hypergeometric function $U(a, b, z)$ is the solution of [[Kummer's equation|NT917KFR57]] that behaves like $z^{-a}$ as $z \to +\infty$.
It is a combination of two Kummer functions $M$.
It grows or decays only like a power of $z$ at infinity, while $M(a, b, z)$ in general grows like $e^z$.
Many functions of applied mathematics are special cases of $U$.
Examples are the complementary error function, the upper incomplete gamma function and the modified Bessel function $K_\nu$.

## Explanations

### L1 human

Kummer's equation has a two-dimensional space of solutions.
Kummer's function $M$ is the solution that is nice at $z = 0$.
Tricomi's function $U$ is the solution that is nice at $z = +\infty$: it behaves like a power of $z$ instead of growing exponentially.
For $\operatorname{Re} a > 0$ and $\operatorname{Re} z > 0$ it has the integral form $U(a, b, z) = \frac{1}{\Gamma(a)} \int_0^\infty e^{-zt}\, t^{a - 1} (1 + t)^{b - a - 1}\, dt$.
For $b = a + 1$ the factor $(1 + t)^{b - a - 1}$ is $1$, and the integral gives $U(a, a + 1, z) = z^{-a}$.
