---
tag: N09YAJWA7E
kind: definition
name: Torsion of a curve
msc: [53A04]
defines: S4BZ697DSH
uses: [7JQS6VKFEZ, 00R1JDDV5X, 0SEDGXG9S3]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_of_a_curve
---

## Definition

Let $I \subseteq \R$ be an interval and let $\gamma \colon I \to \R^3$ be a curve of class $C^3$ parametrised by [[arc length|00R1JDDV5X]] $s$, with [[curvature|7JQS6VKFEZ]] $\kappa(s) > 0$ for all $s \in I$.
Its unit tangent is $T = \gamma'$, its unit normal is $N = T' / \kappa$, and its binormal is $B = T \times N$, where $\times$ is the [[cross product|0SEDGXG9S3]].
The vector $B'(s)$ is a multiple of $N(s)$.
The *torsion* of $\gamma$ at $s$ is the number $\tau(s)$ with
$$B'(s) = -\tau(s) \, N(s).$$

## Remarks

For a regular $C^3$ curve with any parameter $t$ and $\gamma' \times \gamma'' \ne 0$, the torsion is
$$\tau = \frac{\det(\gamma', \gamma'', \gamma''')}{\norm{\gamma' \times \gamma''}^2}.$$
Example: take the helix $\gamma(t) = (a \cos t, a \sin t, bt)$ with $a > 0$ and $b \in \R$.
Then $\gamma' \times \gamma'' = (ab \sin t, -ab \cos t, a^2)$ and $\det(\gamma', \gamma'', \gamma''') = a^2 b$, so $\tau = b / (a^2 + b^2)$.
Non-example: on the curve $t \mapsto (t, t^3, 0)$ the curvature vanishes at $t = 0$, so $N$ and $B$ are not defined there and the torsion is not defined at that point.
Some books use the opposite sign convention $B' = \tau N$.
A curve with $\kappa > 0$ lies in a plane if and only if $\tau = 0$ everywhere.
