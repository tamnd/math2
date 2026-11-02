---
tag: SKMQ02FP9J
kind: definition
name: Unilateral Z-transform
msc: [44A55, 39A06]
defines: EPG6JPVJE7
uses: [5FY0JQGHYZ, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Z-transform
    locator: Unilateral Z-transform
---

## Definition

Let $(x_n)_{n \in \Z}$ or $(x_n)_{n \ge 0}$ be a [[sequence|0G9EKM0E15]] of complex numbers.
The *unilateral Z-transform* of $x$ is
$$X(z) = \sum_{n = 0}^{\infty} x_n z^{-n},$$
as a function of the nonzero complex numbers $z$ for which the series converges absolutely.

## Remarks

Let $r = \limsup_{n \to \infty} \abs{x_n}^{1/n}$.
The series converges absolutely for $\abs{z} > r$ and diverges for $0 < \abs{z} < r$, by the root test.
Example: $x_n = n$ gives $X(z) = \sum_{n \ge 0} n z^{-n} = z/(z - 1)^2$ for $\abs{z} > 1$, by differentiating the geometric series.
Non-example: $x_n = n!$ gives $r = \infty$, so the series converges for no $z$, and $x$ has no unilateral Z-transform as a function.
The unilateral transform of $x$ equals the [[Z-transform|5FY0JQGHYZ]] of the sequence that agrees with $x$ for $n \ge 0$ and is $0$ for $n < 0$.
Writing $w = z^{-1}$ turns it into the ordinary generating function $\sum_{n \ge 0} x_n w^n$.
