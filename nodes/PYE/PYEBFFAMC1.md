---
kind: concept
msc:
- 31B05
- 31B25
name: Subharmonic function via harmonic comparison
sources:
- url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L6795
  locator: scv.tex:6795
tag: PYEBFFAMC1
uses:
- 0DEB0JMN0W
---

## Summary

Let $U \subset \mathbb{R}^n$ be open. A function $f \colon U \to \mathbb{R} \cup \{-\infty\}$ is subharmonic when it is upper semicontinuous and it never exceeds a [[harmonic function|0DEB0JMN0W]] that bounds it on the boundary of a ball.

Precisely, take any closed ball $\overline{B_r(a)} \subset U$. Take any function $g$ that is continuous on the closed ball and harmonic in the open ball. Suppose $f \le g$ on the sphere $\partial B_r(a)$. Then $f \le g$ at every point of the open ball $B_r(a)$.

Upper semicontinuity means $\limsup_{t \to x} f(t) \le f(x)$ at each $x \in U$.

For this definition, a harmonic function is a $C^2$ function on $U$ whose Laplacian, the sum of the second partial derivatives in the coordinates, is zero on $U$.

This is the comparison form of the definition. It is equivalent to the form that uses averages over spheres, which is the usual definition of a [[subharmonic function|Z1MHMGFNFW]].
