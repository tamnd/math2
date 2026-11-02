---
tag: T4VP5QTQK6
kind: statement
role: proposition
name: Recurrence relations for Bessel functions
msc: [33C10]
uses: [CZCMRDWDYW, GRSNDJG363, N3CC5DRGT1]
about: [CZCMRDWDYW, GRSNDJG363]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Statement

Let $\nu \in \C$ and let $C_\nu$ be any one of $J_\nu$, $Y_\nu$, $H^{(1)}_\nu$, $H^{(2)}_\nu$.
These are a [[Bessel function of the first kind|CZCMRDWDYW]], of the [[second kind|GRSNDJG363]], or a [[Hankel function|N3CC5DRGT1]].
Then for $z \in \C \setminus (-\infty, 0]$:

1. $C_{\nu - 1}(z) + C_{\nu + 1}(z) = \frac{2\nu}{z}\, C_\nu(z)$.
2. $C_{\nu - 1}(z) - C_{\nu + 1}(z) = 2\, C_\nu'(z)$.

## Remarks

For $J_\nu$ both relations follow by comparing coefficients in the power series $J_\nu(z) = \sum_{m \ge 0} \frac{(-1)^m}{m!\, \Gamma(m + \nu + 1)} \left( \frac{z}{2} \right)^{2m + \nu}$.
Equivalent forms are $\left( z^\nu C_\nu \right)' = z^\nu C_{\nu-1}$ and $\left( z^{-\nu} C_\nu \right)' = -z^{-\nu} C_{\nu+1}$.
For $Y_\nu$ they follow from the definition through $J_{\pm\nu}$ and a limit, and for the Hankel functions by linearity.
Example: with $\nu = 0$ the second relation and $J_{-1} = -J_1$ give $J_0' = -J_1$.
Example: from $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ and $J_{-1/2}(x) = \sqrt{\frac{2}{\pi x}} \cos x$, the first relation with $\nu = \frac{1}{2}$ gives $J_{3/2}(x) = \sqrt{\frac{2}{\pi x}} \left( \frac{\sin x}{x} - \cos x \right)$.

## Explanations

### L1 human

Bessel functions of neighbouring orders are tied together by simple rules.
If one knows two consecutive orders, one gets all the others by the first rule.
The second rule gives the derivative of a Bessel function without any calculus on the function itself.

### L2 human

The first relation is a three-term recurrence in the order, so tables and software compute $J_n(x)$ for many $n$ from a few starting values.
Forward use of it is unstable for $J_n$ when $n > x$, and one runs it backward instead (Miller's algorithm).
The relations also show that Bessel functions of half-integer order are elementary, which gives the spherical Bessel functions.
The modified Bessel functions satisfy the same relations with some signs changed.
