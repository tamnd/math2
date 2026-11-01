---
tag: R2PHM118NG
kind: statement
role: theorem
name: Picard's little theorem
msc: ["30D20", "30D35"]
uses: [0419794R0T]
about: [0419794R0T]
sources:
  - url: https://en.wikipedia.org/wiki/Picard_theorem
---

## Statement

Let $f$ be an [[entire function|0419794R0T]] that is not constant.
Then the set $\C \setminus f(\C)$ has at most one point.
That is, $f$ takes every complex value with at most one exception.

## Remarks

One classical proof uses the [[modular lambda function|4Z1YXT957Z]], which gives a holomorphic covering map from the unit disc onto $\C \setminus \set{0, 1}$.
If $f$ omits two values, one may assume that they are $0$ and $1$.
Then $f$ lifts through this covering to an entire function with values in the unit disc, which is constant by [[Liouville's theorem|0EHKVRF4J6]], so $f$ is constant.
Another proof uses [[Bloch's theorem|KW31KDX7TB]].
The bound is sharp: $e^z$ is not constant and omits exactly the value $0$.
For polynomials no value is omitted, by the fundamental theorem of algebra.

## Explanations

### L1 human

Liouville's theorem says that a bounded entire function is constant, so a nonconstant entire function cannot avoid a whole disc of values.
Picard's little theorem is much stronger: it cannot avoid even two points.
The exponential function shows that avoiding one point is possible.

### L2 human

The theorem has a version for meromorphic functions: a nonconstant meromorphic function on $\C$ omits at most two values of the Riemann sphere, as $\tan z$ omits $i$ and $-i$.
[[Picard's great theorem|08QA8QTM71]] is a local version near an essential singularity and implies the little theorem: if $f$ is not a polynomial, then $f(1/z)$ has an essential singularity at $0$.
The [[second main theorem of Nevanlinna theory|GWYE6745JK]] gives a quantitative form: for three distinct values, the solutions of $f(z) = a$ must be numerous.
Through Bloch's principle, the theorem is linked to [[Montel's theorem|ZVFVBVJMCB]] on normal families.
