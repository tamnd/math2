---
tag: B1Z1C8AHVD
kind: statement
role: theorem
name: Fáry–Milnor theorem
msc: [53A04, 57K10]
uses: [QP9DY5K8QW, 7JQS6VKFEZ, QYEAZTYGPT, 0D032NSZKY]
about: [QP9DY5K8QW, QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/F%C3%A1ry%E2%80%93Milnor_theorem
same_as:
  wikidata: Q3527071
  wikipedia: Fáry–Milnor theorem
---

## Statement

Let $\gamma \colon [a, b] \to \R^3$ be a regular simple [[closed curve|0D032NSZKY]] of class $C^2$ whose derivatives up to order $2$ also agree at $a$ and $b$.
If the [[total curvature|QP9DY5K8QW]] of $\gamma$ is at most $4\pi$, then $\gamma$ is unknotted, that is, its image is a trivial [[knot|QYEAZTYGPT]].
Equivalently, every knotted curve of this kind has total curvature greater than $4\pi$.

## Remarks

Milnor's proof uses height functions.
For almost every unit vector $v$, the function $t \mapsto \ip{\gamma(t)}{v}$ has finitely many local maxima, and the total curvature equals $2\pi$ times the average number of these maxima over all $v$.
If the total curvature is less than $4\pi$, some direction $v$ gives exactly one local maximum and one local minimum.
Then each plane orthogonal to $v$ meets the curve in at most two points, and joining these pairs of points gives an embedded disc bounded by the curve.
So the curve is unknotted; the case of total curvature exactly $4\pi$ needs a further argument.
Example: a standard trefoil knot must have total curvature greater than $4\pi$, while a round circle, with $2\pi$, is unknotted.
István Fáry and John Milnor proved the theorem independently, around 1949 and 1950.

## Explanations

### L1 human

A knotted loop of wire must bend a lot.
In total, it must turn by more than two full turns.
So if a closed loop turns by at most two full turns, it can be pulled into a round circle without cutting.

### L2 human

The theorem refines [[Fenchel's theorem|F0BJ2BHSZG]], which gives the bound $2\pi$ for every closed curve.
The bound $4\pi$ is sharp: there are knotted curves with total curvature as close to $4\pi$ as one likes.
Milnor's averaging formula for the total curvature is a model of later integral-geometric methods, such as the Crofton formula.
