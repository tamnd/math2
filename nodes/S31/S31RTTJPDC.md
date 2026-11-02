---
tag: S31RTTJPDC
kind: definition
name: Axiom A
msc: [37D20]
defines: Z26Z4XZFVA
uses: [NY9MCZXY6N, EY2W34JZA4, T75CZ5H47N, 0D198GPMTJ, 0Z1Y7JHGBR]
sources:
  - url: https://en.wikipedia.org/wiki/Axiom_A
---

## Definition

Let $M$ be a compact smooth manifold and let $f \colon M \to M$ be a $C^1$ [[diffeomorphism|0Z1Y7JHGBR]].
Let $\Omega(f)$ be the [[non-wandering set|EY2W34JZA4]] of $f$.
Then $f$ satisfies *Axiom A* if both of the following hold.

1. $\Omega(f)$ is a [[hyperbolic set|NY9MCZXY6N]] of $f$.
2. The set of [[periodic points|T75CZ5H47N]] of $f$ is [[dense|0D198GPMTJ]] in $\Omega(f)$.

## Remarks

Every periodic point is non-wandering, so clause 2 says that $\Omega(f)$ is the closure of the set of periodic points.
Example: the north-south map of the circle, the time-one map of $\theta' = \sin\theta$, has $\Omega(f) = \set{0, \pi}$.
Both fixed points are hyperbolic, with derivatives $e$ and $e^{-1}$, so both clauses hold.
Non-example: an irrational rotation of the circle has $\Omega(f)$ equal to the whole circle, but it has no periodic points, and the derivative $1$ is not hyperbolic; both clauses fail.
Another non-example is the time-one map of $\theta' = 1 - \cos\theta$: its only non-wandering point $0$ is fixed, but the derivative there is $1$, so clause 1 fails.
For flows, Axiom A asks that the non-wandering set be hyperbolic in the flow sense and that closed orbits be dense in it.
