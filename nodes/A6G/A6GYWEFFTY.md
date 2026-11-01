---
tag: A6GYWEFFTY
kind: statement
role: theorem
name: Marden's theorem
msc: [30C15, 51M04]
uses: [019MA1VTR2, 0YTCMFB4HC, 0CTNFGYMM2, 0VKCCEXBJ1]
about: [019MA1VTR2, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Marden%27s_theorem
same_as:
  wikidata: Q1568612
  wikipedia: Marden's theorem
---

## Statement

Let $p$ be a polynomial of degree $3$ with complex coefficients whose three [[roots|019MA1VTR2]] $z_1, z_2, z_3$ are not collinear in the plane $\C$.
Let $T$ be the [[triangle|0CTNFGYMM2]] with vertices $z_1, z_2, z_3$.
Then there is a unique [[ellipse|0VKCCEXBJ1]] inscribed in $T$ and tangent to its three sides at their midpoints.
The foci of this ellipse are the two roots of the derivative $p'$.

## Remarks

The ellipse is the Steiner inellipse of $T$.
If $p$ is monic, then $p'(z) = (z - z_1)(z - z_2) + (z - z_2)(z - z_3) + (z - z_3)(z - z_1)$.
One proof computes the foci of the Steiner inellipse and checks, with the reflection property of the tangent lines of an ellipse, that they are the roots of this quadratic.
For an equilateral triangle the inellipse is the incircle, and for $p(z) = z^3 - 1$ its centre $0$ is the double root of $p'(z) = 3z^2$.
Example: for $p(z) = z(z - 1)(z - i)$, one gets $p'(z) = 3z^2 - 2(1 + i)z + i$, whose roots are the foci of the inellipse of the triangle $0, 1, i$.
The theorem refines the Gauss–Lucas theorem for cubics: the critical points lie not only in the triangle but at the foci of a specific ellipse inside it.

## Explanations

### L1 human

A cubic polynomial has three roots, which form a triangle in the plane.
There is exactly one ellipse that fits inside the triangle and touches each side at its midpoint.
Marden's theorem says that the two foci of this ellipse are exactly the roots of the derivative.
It is a striking link between algebra and classical geometry.

### L2 human

The roots of $p'$ are the [[critical points|0YTCMFB4HC]] of $p$, so the theorem locates the critical points of a cubic from its roots alone.
It is a classical result of the geometry of polynomials, which studies where the zeros of a polynomial and of its derivatives lie.
Together with [[Sendov's conjecture|101H2VSX2R]], it belongs to the study of how the zeros of $p'$ sit relative to the zeros of $p$.
