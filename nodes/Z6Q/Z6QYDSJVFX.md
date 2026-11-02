---
tag: Z6QYDSJVFX
kind: statement
role: theorem
name: Four-vertex theorem
msc: [53A04]
uses: [7JQS6VKFEZ, 0D032NSZKY, 06JMR2XWXW, 00R1JDDV5X]
about: [7JQS6VKFEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Four-vertex_theorem
same_as:
  wikidata: Q994401
  wikipedia: Four-vertex theorem
---

## Statement

Let $L > 0$ and let $\gamma \colon \R \to \R^2$ be an $L$-periodic curve of class $C^3$, parametrised by [[arc length|00R1JDDV5X]].
Assume that $\gamma$ is injective on $[0, L)$, so that it traces a simple [[closed curve|0D032NSZKY]].
Let $k$ be the signed [[curvature|7JQS6VKFEZ]] of $\gamma$.
A *vertex* of $\gamma$ is a point $s$ with $k'(s) = 0$.
Then $\gamma$ has at least four vertices in $[0, L)$.

## Remarks

The idea is clearest for a convex curve with nonconstant $k$.
Since $k$ is periodic, it has a maximum and a minimum, which are two vertices.
Assume there were no others.
Then the line through the two corresponding points of the curve meets it only there, and $k'$ has a fixed sign on each of the two arcs.
Choose a linear function $f(x) = \ip{x}{v} + c$ that vanishes on that line; then $k'(s) f(\gamma(s))$ has constant sign.
But the plane Frenet formulas give $\int_0^L k'(s) \, \gamma(s) \, ds = 0$ and $\int_0^L k'(s) \, ds = 0$, so the integral of $k' \cdot (f \circ \gamma)$ is $0$, a contradiction.
The general case of simple closed curves needs more work.
Example: the ellipse $x^2/a^2 + y^2/b^2 = 1$ with $a > b > 0$ has exactly four vertices, the ends of its two axes.
The hypothesis that the curve is simple is needed: a limaçon with an inner loop is a closed regular curve with only two vertices.
The theorem was proved for convex curves by Mukhopadhyaya in 1909 and for all simple closed curves by Kneser in 1912.

## Explanations

### L1 human

Take any smooth closed loop in the plane that does not cross itself.
Its curvature cannot just rise once and fall once around the loop.
There are always at least four places where the curvature stops increasing or stops decreasing.
An ellipse shows that four is the best possible: it is most curved at the ends of the long axis and flattest at the ends of the short axis.

### L2 human

When $k$ never vanishes, the vertices of $\gamma$ are exactly the points where its [[evolute|Y3ZNV24V2C]] has zero velocity.
Typically these are cusps of the evolute, as for the four cusps of the evolute of an ellipse.
The proof above uses only the plane Frenet equations $T' = kN$ and $N' = -kT$, integrated over a period.
The theorem is an early example of a global result in differential geometry, in which a local quantity is constrained by the shape of the whole curve.
