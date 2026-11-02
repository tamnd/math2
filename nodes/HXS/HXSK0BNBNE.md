---
tag: HXSK0BNBNE
kind: statement
role: theorem
name: Stewart's theorem
msc: [51M04]
uses: [0CTNFGYMM2, 0NPPGHQNXQ]
about: [0CTNFGYMM2]
sources:
  - url: https://en.wikipedia.org/wiki/Stewart%27s_theorem
same_as:
  wikidata: Q739403
  wikipedia: Stewart's theorem
---

## Statement

Let $ABC$ be a [[triangle|0CTNFGYMM2]] in the Euclidean plane, and let $D$ be a point on the segment $BC$.
Write $a = BC$, $b = CA$, $c = AB$, $m = BD$, $n = DC$ and $d = AD$ for the [[distances|0NPPGHQNXQ]].
Then
$$b^2 m + c^2 n = a \left( d^2 + m n \right).$$

## Remarks

If $D$ lies strictly between $B$ and $C$, the angles $\angle ADB$ and $\angle ADC$ add up to $\pi$, so their cosines are opposite.
Apply the [[law of cosines|060ZVZBV3E]] to the triangles $ABD$ and $ADC$ at the vertex $D$.
Multiply the first equation by $n$, the second by $m$, and add: the cosine terms cancel, and $m + n = a$ gives the formula.
If $D = B$ or $D = C$, the formula is direct.

Example: if $D$ is the midpoint of $BC$, then $m = n = a/2$, and the formula becomes $d^2 = \frac{b^2 + c^2}{2} - \frac{a^2}{4}$.
This is [[Apollonius's theorem|0NAKHQ9XYY]] on the length of a [[median|0XW8HX8VEV]].

For a point $D$ on the line $BC$ outside the segment, the formula holds with signed lengths $m$ and $n$.

## Explanations

### L1 human

Draw a segment from one corner of a triangle to any point of the opposite side.
Stewart's theorem gives the length of that segment from the three sides and the two pieces into which it cuts the opposite side.
No angles are needed.

### L2 human

Stewart's theorem is the general form of several familiar length formulas.
With the midpoint it gives the length of a median.
With the foot of an angle bisector, located by the [[angle bisector theorem|0859R2V6ES]], it gives the length of the bisector.
