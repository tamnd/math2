---
tag: QTX0GBZMT8
kind: statement
role: theorem
name: Removable sets for bounded harmonic functions
msc: [31B05, 31A05, 31B15]
uses: [0DEB0JMN0W, C95QJ7YH5T, 0R6EWFKRCF]
about: [C95QJ7YH5T, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Polar_set_(potential_theory)
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an open set.

1. Let $E \subseteq \Omega$ be a closed subset of $\Omega$ that is a [[polar set|C95QJ7YH5T]].
   Let $h$ be a [[harmonic function|0DEB0JMN0W]] on $\Omega \setminus E$ such that each point of $E$ has a neighbourhood $V$ with $h$ bounded on $V \setminus E$.
   Then $h$ extends uniquely to a harmonic function on $\Omega$.
2. Conversely, let $\Omega$ be bounded and let $K \subseteq \Omega$ be a [[compact set|0R6EWFKRCF]] that is not polar.
   Then there is a bounded harmonic function on $\Omega \setminus K$ that does not extend to a harmonic function on $\Omega$.

## Remarks

Proof idea for part 1: the question is local, so work in a small ball $B$ with $\overline B \subseteq \Omega$.
Let $H$ be the Poisson integral on $B$ of $h$ on $\partial B$, which is bounded and defined outside $E \cap \partial B$, a set of surface measure zero.
Let $u$ be a subharmonic function, not identically $-\infty$, with $u \le 0$ on $B$ and $u = -\infty$ on $E$.
For each $\varepsilon > 0$ the function $h - H + \varepsilon u$ is subharmonic on $B \setminus E$ and tends to $-\infty$ at $E$, so the maximum principle gives $h - H + \varepsilon u \le 0$.
Letting $\varepsilon \to 0$ and repeating the argument with $-h$ gives $h = H$ off the polar set $\set{u = -\infty}$, hence on $B \setminus E$.
For part 2, the restriction to $\Omega \setminus K$ of the potential of the equilibrium measure of $K$ is bounded and harmonic, and it does not extend.

Example: in $\R^2$, a single point is polar, so a bounded harmonic function on a punctured disc extends harmonically across the puncture.
The function $\log \abs{x}$ on the punctured disc is harmonic but unbounded, and it does not extend, so boundedness is needed.

Example of part 2: in $\R^3$ let $K$ be the closed unit ball and let $\Omega$ be the open ball of radius $2$.
The function $h(x) = 1/\abs{x}$ is bounded and harmonic on $\Omega \setminus K$.
Suppose that it had a harmonic extension $H$ to $\Omega$.
The function equal to $H$ on $\Omega$ and to $1/\abs{x}$ outside $K$ would be harmonic and bounded on $\R^3$ and tend to $0$ at infinity.
By Liouville's theorem it would be $0$, which is false.

## Explanations

### L1 human

A harmonic function that stays bounded cannot notice a polar set: any hole of this kind can be filled in.
Among compact sets, the polar ones are exactly those with this property.
So capacity zero is the precise notion of "too small to matter" for bounded harmonic functions.

### L2 human

This theorem extends the classical removable singularity theorem for a single point.
In the plane it gives the removability of polar sets for bounded holomorphic functions as well, since their real and imaginary parts are harmonic.
For bounded holomorphic functions the exact class of removable compact sets is larger: it is described by analytic capacity, and a segment is not removable while some non-polar sets are.
The same proof scheme, with a subharmonic function equal to $-\infty$ on the exceptional set, is used throughout potential theory to show that polar sets can be ignored.
