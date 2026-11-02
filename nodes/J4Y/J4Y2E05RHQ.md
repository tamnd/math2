---
tag: J4Y2E05RHQ
kind: statement
role: theorem
name: Descartes' theorem
msc: [51M04, 52C26]
uses: [060W5CBZP6]
about: [060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Descartes%27s_theorem
same_as:
  wikidata: Q1196538
  wikipedia: Descartes's theorem
---

## Statement

Let $\Gamma_1, \Gamma_2, \Gamma_3, \Gamma_4$ be four [[circles|060W5CBZP6]] in the Euclidean plane such that each two of them are tangent and the six points of tangency are distinct.
Let $r_i$ be the radius of $\Gamma_i$.
Put $k_i = 1/r_i$ if no other circle lies inside $\Gamma_i$, and $k_i = -1/r_i$ if the other three circles lie inside $\Gamma_i$.
Then
$$(k_1 + k_2 + k_3 + k_4)^2 = 2\left(k_1^2 + k_2^2 + k_3^2 + k_4^2\right).$$

## Remarks

The numbers $k_i$ are the signed curvatures of the circles.
The statement extends to the case where one circle is a straight line, with curvature $0$.
Solving the quadratic equation for $k_4$ gives
$$k_4 = k_1 + k_2 + k_3 \pm 2\sqrt{k_1 k_2 + k_2 k_3 + k_3 k_1},$$
and the two signs correspond to the two circles that touch $\Gamma_1, \Gamma_2, \Gamma_3$.
Example: an outer circle of radius $1$ ($k_1 = -1$) holds two circles of radius $1/2$ ($k_2 = k_3 = 2$).
The formula gives $k_4 = 3$, and indeed $(-1 + 2 + 2 + 3)^2 = 36 = 2(1 + 4 + 4 + 9)$.
One proof applies an inversion that sends two of the circles to parallel lines and computes directly.

## Explanations

### L1 human

Four circles that all touch each other are tightly linked.
If you know the sizes of three of them, the theorem tells you the size of the fourth.
It is cleanest when written with curvatures, the reciprocals of the radii.

### L2 human

The theorem is the basic step in the construction of Apollonian circle packings.
Starting from four mutually tangent circles, the second root of the quadratic replaces one circle by a new one, and the process repeats.
If the first four curvatures are integers, all curvatures in the packing are integers, which makes these packings an object of number theory.
It is a special case of the [[problem of Apollonius|F9410EB0N1]] where the given circles touch each other.
