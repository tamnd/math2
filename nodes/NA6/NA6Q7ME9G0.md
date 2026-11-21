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

Every vector splits in exactly one way into a part along a given direction and a part perpendicular to it, and the part along the direction is the nearest point of the line.
Let $n$ be a positive integer, let $u, v \in \mathbb{R}^n$, and assume $v \neq 0$.
Let $u \cdot v$ be the [[dot product|0S52TNNTH9]] and $\|\cdot\|$ the [[length|0XKBKGTCPC]].

1. There is exactly one pair $(c, q)$ of a real number $c$ and a vector $q \in \mathbb{R}^n$ with $u = cv + q$ and $q \cdot v = 0$.
2. This pair is $c = \dfrac{u \cdot v}{v \cdot v}$ and $q = u - cv$, so $p = cv$ is the [[vector projection|0JW13B48YP]] $\operatorname{proj}_v u$.
3. For each real number $t$, $\|u - tv\| \geq \|q\|$, with equality if and only if $t = c$.

## Remarks

### Why each hypothesis is needed

The hypothesis $v \neq 0$ is what makes the pair unique.
If $v = 0$, then $u = c \cdot 0 + u$ with $u \cdot 0 = 0$ for every $c$, so every number $c$ works, and the formula for $c$ would divide by $0$.

The perpendicularity of $q$ is just as essential.
Without the condition $q \cdot v = 0$, every $c$ works with $q = u - cv$, and the split carries no information.
The condition singles out one $c$ because it is one linear equation in one unknown.

### What it gives you

The theorem is the source of the projection formula $\operatorname{proj}_v u = \frac{u \cdot v}{v \cdot v}\, v$.
It also gives Pythagoras for the two parts, $\|u\|^2 = \|p\|^2 + \|q\|^2$, because $p \cdot q = c\,(v \cdot q) = 0$.

Part 3 turns a minimization into a formula.
The distance from the point $u$ to the line $\mathbb{R} v$ through the origin is
$$\|q\| = \|u - \operatorname{proj}_v u\|,$$
and the [[distance formulas|C6GAS92QHX]] for lines and planes are built on this.

A third consequence is an inequality.
From $\|p\|^2 \leq \|u\|^2$ we get $\frac{(u \cdot v)^2}{\|v\|^2} \leq \|u\|^2$, which is the [[Cauchy-Schwarz inequality|0RFWW56Y22]] in $\mathbb{R}^n$.
Each step of the [[Gram-Schmidt process|0VT6P0GNQR]] also uses this decomposition, to remove from a vector its parts along the vectors already chosen.

### The converse

If $u = cv + q$ with $q \cdot v = 0$, then $cv$ is the projection of $u$ along $v$, by part 1.
In the other direction, if $tv$ is the multiple of $v$ nearest to $u$, then $t = c$ by part 3, so $u - tv$ is perpendicular to $v$.
So "nearest" and "perpendicular remainder" describe the same point.

### Beyond one direction

For a subspace $W$ of $\mathbb{R}^n$ the same unique split $u = \hat u + u^\perp$ holds, with $\hat u \in W$ and $u^\perp \perp W$.
This is the [[orthogonal decomposition relative to a subspace|JM1382S489]].
With an orthogonal basis of $W$, the vector $\hat u$ is the sum of the projections along the basis vectors, by the [[projection formula for an orthogonal basis|6ARG1JYE34]].
The same results hold in every inner product space, and for closed subspaces of Hilbert spaces.

## Explanations

### L1 human

Every arrow can be split into two arrows: one along a chosen direction, and one at a right angle to it.
For $(3, 4)$ and the direction $(1, 0)$, the parts are $(3, 0)$ and $(0, 4)$.
There is only one such split.
The part along the direction is also the point on that line nearest to the tip of the arrow.

### L2 human

Here is a typical problem: find the distance from the point $(5, 0)$ to the line through $0$ in the direction $v = (1, 2)$.
With $u = (5, 0)$ the dot products are $u \cdot v = 5$ and $v \cdot v = 5$, so $c = 1$ and $p = (1, 2)$.
The remainder is $q = u - p = (4, -2)$, and indeed $q \cdot v = 4 - 4 = 0$.
By part 3 the distance is
$$\|q\| = \sqrt{16 + 4} = 2\sqrt{5}.$$
Watch out: the theorem splits along one direction and its perpendicular.
Splitting a vector along two directions that are not perpendicular is a different problem, solved by a linear system.

### L3 human

Parts 1 and 2 say that $\mathbb{R}^n = \mathbb{R}v \oplus v^\perp$, a direct sum of the line and its orthogonal complement.
Part 3 is the simplest least squares problem: minimize $\|u - tv\|$ over one unknown $t$, with the normal equation $(v \cdot v)\, t = u \cdot v$.
The sub-areas on [[direct sums|QHKTJ89V6S]] and on [[orthogonality and least squares|8GQVME4SZZ]] extend both views.
