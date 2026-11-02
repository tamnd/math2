---
tag: M1KYAQMF9W
kind: problem
name: Pompeiu problem
msc: [35N25, 44A12, 35R30]
uses: [2Z2QVWZ262]
about: [J05VKG4XQB]
sources:
  - url: https://en.wikipedia.org/wiki/Pompeiu_problem
same_as:
  wikidata: Q3406234
  wikipedia: Pompeiu problem
history:
  posed_by: "Dimitrie Pompeiu"
  first_stated: "1929"
---

## Problem

Let $n \ge 2$ and let $K \subseteq \R^n$ be a bounded set with nonempty interior.
The set $K$ has the *Pompeiu property* if the only continuous function $f \colon \R^n \to \C$ with
$$\int_{\sigma(K)} f \, dx = 0 \quad \text{for every rigid motion } \sigma \text{ of } \R^n$$
is $f = 0$.
Here a rigid motion is a composition of a rotation and a translation, and the integral is against [[Lebesgue measure|2Z2QVWZ262]].
Determine which sets have the Pompeiu property; in particular, decide whether every bounded simply connected Lipschitz domain without the Pompeiu property is a ball.

## Remarks

A ball does not have the Pompeiu property.
For the unit ball in $\R^n$ and a suitable nonzero vector $a$, the function $f(x) = \sin(a \cdot x)$ has integral $0$ over every translate of the ball, and rotations map balls to balls.
Squares and other polygons are known to have the Pompeiu property.
By a theorem of Williams (1976), for smooth contractible domains the conjectured answer is equivalent to [[Schiffer's conjecture|J05VKG4XQB]] on an overdetermined Neumann eigenvalue problem.

## Explanations

### L1 human

Slide and rotate a fixed shape all over the plane, and suppose a function averages to zero on every copy of the shape.
Must the function be zero everywhere?
For a square the answer is yes.
For a disc the answer is no: a suitable wave $\sin(a x)$ averages to zero on every disc of the given radius.
Pompeiu's problem asks whether the disc is the only shape for which this happens.
