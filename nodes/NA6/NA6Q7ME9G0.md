---
tag: NA6Q7ME9G0
kind: statement
role: theorem
name: Orthogonal decomposition of a vector along a nonzero vector
msc: ["15A63", "51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [0JW13B48YP]
uses: [0S52TNNTH9, 0XKBKGTCPC, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_projection
    locator: Definitions in terms of a and b
  - url: https://understandinglinearalgebra.org/
    locator: Section 6.1
---

## Statement

Let $n$ be a positive integer, let $u, v \in \mathbb{R}^n$, and assume $v \neq 0$.
Let $u \cdot v$ be the [[dot product|0S52TNNTH9]] and $\|\cdot\|$ the [[length|0XKBKGTCPC]].

1. There is exactly one pair $(c, q)$ of a real number $c$ and a vector $q \in \mathbb{R}^n$ with $u = cv + q$ and $q \cdot v = 0$.
2. This pair is $c = \dfrac{u \cdot v}{v \cdot v}$ and $q = u - cv$. So $p = cv$ is the [[vector projection|0JW13B48YP]] $\operatorname{proj}_v u$.
3. For each real number $t$, $\|u - tv\| \geq \|q\|$, with equality if and only if $t = c$.

## Remarks

### Why each hypothesis is needed

- The hypothesis $v \neq 0$ is needed for uniqueness. If $v = 0$, then $u = c \cdot 0 + u$ with $u \cdot 0 = 0$ for every $c$, so $c$ is not unique, and the formula divides by $0$.
- Perpendicularity in part 1 is needed for uniqueness too. Without $q \cdot v = 0$, each $c$ works with $q = u - cv$.

### Consequences

- The projection formula $\operatorname{proj}_v u = \frac{u \cdot v}{v \cdot v}\, v$.
- Pythagoras for the parts: $\|u\|^2 = \|p\|^2 + \|q\|^2$, because $p \cdot q = c\,(v \cdot q) = 0$.
- The distance from the point $u$ to the line $\mathbb{R} v$ through the origin is $\|q\| = \|u - \operatorname{proj}_v u\|$, by part 3.
- From $\|p\|^2 \leq \|u\|^2$ we get $\frac{(u \cdot v)^2}{\|v\|^2} \leq \|u\|^2$, which is the [[Cauchy-Schwarz inequality|0RFWW56Y22]] for $\mathbb{R}^n$.
- Each step of the [[Gram-Schmidt process|0VT6P0GNQR]] uses this decomposition.

### Converse

If $u = cv + q$ with $q \cdot v = 0$, then $cv$ is the projection of $u$ along $v$, by part 1.
If $tv$ is the multiple of $v$ nearest to $u$, then $u - tv$ is perpendicular to $v$, by part 3.

### Generalizations

For a subspace $W$ of $\mathbb{R}^n$ there is the same unique decomposition $u = \hat u + u^\perp$ with $\hat u \in W$ and $u^\perp \perp W$: the [[orthogonal decomposition relative to a subspace|JM1382S489]].
With an orthogonal basis of $W$, $\hat u$ is the sum of the projections along the basis vectors, by the [[projection formula for an orthogonal basis|6ARG1JYE34]].
The same holds in every inner product space, and for closed subspaces of Hilbert spaces.

## Explanations

### L1 human

Every arrow can be split into two arrows: one along a chosen direction, and one at a right angle to it.
For $(3, 4)$ and the direction $(1, 0)$, the parts are $(3, 0)$ and $(0, 4)$.
There is only one such split.
The part along the direction is also the point on that line that is nearest to the tip of the arrow.

### L2 human

Worked example: $u = (5, 0)$ and $v = (1, 2)$.

1. $u \cdot v = 5$ and $v \cdot v = 5$, so $c = 1$ and $p = (1, 2)$.
2. $q = u - p = (4, -2)$, and $q \cdot v = 4 - 4 = 0$.
3. The distance from $(5, 0)$ to the line through $0$ in the direction $(1, 2)$ is $\|q\| = \sqrt{20} = 2\sqrt{5}$.

The typical use is part 3: the nearest point on a line, and so the distance to a line.
A trap: the formula needs $q \perp v$, so the split along two directions that are not perpendicular is a different problem.

### L3 human

Parts 1 and 2 say that $\mathbb{R}^n = \mathbb{R}v \oplus v^\perp$, a direct sum of the line and its orthogonal complement.
Part 3 is the simplest least squares problem: minimize $\|u - tv\|$ over one unknown $t$; the normal equation is $(v \cdot v)\, t = u \cdot v$.
The sub-areas on [[direct sums|QHKTJ89V6S]] and on [[orthogonality and least squares|8GQVME4SZZ]] extend both views.
