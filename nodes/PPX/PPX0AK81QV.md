---
tag: PPX0AK81QV
kind: concept
name: Fredholm determinant
msc: [45B05, 47B10]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_determinant
same_as:
  wikidata: Q3045336
  wikipedia: Fredholm determinant
---

## Summary

The Fredholm determinant of a continuous kernel $K$ on $[a, b]$ is the entire function $D(\lambda) = \sum_{n \ge 0} \frac{(-\lambda)^n}{n!} \int \cdots \int \det[K(x_i, x_j)] \, dx_1 \cdots dx_n$.
It plays for the integral operator $\varphi \mapsto \int K(\cdot, y) \varphi(y) \, dy$ the role that $\det(I - \lambda A)$ plays for a square matrix $A$.
Its zeros are the [[characteristic values|DC7HMHVREP]] of the kernel.
Together with the [[Fredholm minors|HP5VJ9EBST]] it gives an explicit formula for the solution of the [[Fredholm equation of the second kind|DEYYNVCV9J]].
When the integral operator $T$ of $K$ is a [[trace class operator|Z2CP530WDE]], $D(\lambda)$ equals the operator determinant $\det(I - \lambda T)$.

## Explanations

### L1 human

Replace the integral by a sum over $n$ equally spaced points, and the integral operator becomes an $n \times n$ matrix.
For that matrix one can compute $\det(I - \lambda A)$ by expanding it into sums of principal minors.
Letting the number of points grow turns these sums into multiple integrals, and the result is the Fredholm determinant.
For the kernel $K(x, y) = xy$ on $[0, 1]$ only the first two terms survive, and $D(\lambda) = 1 - \lambda/3$.
It vanishes at $\lambda = 3$, which is exactly where the equation $\varphi = \lambda \int_0^1 x y \varphi(y) \, dy$ has the nonzero solution $\varphi(x) = x$.
