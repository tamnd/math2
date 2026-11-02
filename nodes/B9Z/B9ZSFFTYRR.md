---
tag: B9ZSFFTYRR
kind: definition
name: Z-transform as a generating function
msc: [44A55, 05A15]
defines: H9FSFB7T28
uses: [EPG6JPVJE7, 0PHAC833JF, 0N288P2TB5]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function
  - url: https://en.wikipedia.org/wiki/Z-transform
---

## Definition

Let $(x_n)_{n \ge 0}$ be a sequence of complex numbers.
Its ordinary [[generating function|0PHAC833JF]] is the power series $G(w) = \sum_{n \ge 0} x_n w^n$, with [[radius of convergence|0N288P2TB5]] $\rho \in [0, \infty]$.
Its [[unilateral Z-transform|EPG6JPVJE7]] is $X(z) = \sum_{n \ge 0} x_n z^{-n}$.
The *generating-function form of the Z-transform* is the identity
$$X(z) = G(1/z) \quad \text{for } \abs{z} > 1/\rho,$$
with the conventions $1/0 = \infty$ and $1/\infty = 0$.

## Remarks

Example: $x_n = a^n$ with $a \ne 0$ has $G(w) = 1/(1 - a w)$ with $\rho = 1/\abs{a}$, and $G(1/z) = z/(z - a)$ for $\abs{z} > \abs{a}$, which is its Z-transform.
Non-example: a two-sided sequence with some $x_n \ne 0$ for $n < 0$ has a bilateral Z-transform with positive powers of $z$.
These become negative powers of $w$, so the result is a Laurent series in $w$ and not an ordinary generating function.
Under $w = 1/z$, the disc of convergence $\abs{w} < \rho$ of $G$ becomes the outside $\abs{z} > 1/\rho$ of a circle.
The shift rule $\mathcal{Z}\{(x_{n+1})\} = z(X(z) - x_0)$ corresponds to $(G(w) - x_0)/w$ for generating functions.
