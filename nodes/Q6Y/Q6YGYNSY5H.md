---
tag: Q6YGYNSY5H
kind: statement
role: theorem
name: Distance from a point to a line and between two lines in space
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [C6GAS92QHX]
uses: [C6GAS92QHX, 0NPPGHQNXQ, 0399QFDFS8, 0N5N15HWZ7, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Vector formulation
  - url: https://en.wikipedia.org/wiki/Skew_lines
    locator: Distance
---

## Statement

In space the cross product measures how far a point is from a line and how far two lines are from each other.
Let $\operatorname{dist}(S, T)$ be the least [[distance|0NPPGHQNXQ]] $\|s - t\|$ for $s \in S$ and $t \in T$, as in the [[concept|C6GAS92QHX]].
Let $q \in \mathbb{R}^3$.

1. Let $L$ be the [[line|0399QFDFS8]] $a + t d$ with $d \neq 0$. Then the least value is reached, and
   $$\operatorname{dist}(q, L) = \frac{\|(q - a) \times d\|}{\|d\|}.$$
2. Let $L_1 = \{a + t d\}$ and $L_2 = \{b + s e\}$ be lines with $m = d \times e \neq 0$. Then the least value is reached, and
   $$\operatorname{dist}(L_1, L_2) = \frac{|(b - a) \cdot m|}{\|m\|}.$$

The distance from a point to a plane is the [[point-plane formula|0K1E2S6Z69]].

## Remarks

### Why each hypothesis is needed

The condition $d \neq 0$ makes $L$ a line rather than a single point.
The condition $d \times e \neq 0$ says that the two lines are not parallel.
For parallel lines $m = 0$ and the formula of part 2 reads $\tfrac{0}{0}$, so it says nothing; part 1 gives the distance instead.

### What it gives you

Two non-parallel lines meet exactly when $(b - a) \cdot (d \times e) = 0$, since that is when their distance is $0$.
The closest points are the two ends of the common perpendicular, and the proof constructs them.
Two parallel lines $a + t d$ and $b + s d$ are at the distance $\|(b - a) \times d\| / \|d\|$, by part 1 with $q = b$.

For a quick check, take $q = (1, 1, 1)$ and the line $t(1, 2, 2)$.
Then $q \times (1, 2, 2) = (0, -1, 1)$, so the distance is $\tfrac{\sqrt{2}}{3}$.
For the lines $(1, 0, 0) + t(1, 1, 0)$ and $(0, 0, 2) + s(0, 1, 1)$, part 2 gives $\tfrac{1}{\sqrt{3}}$, as the [[skew lines example|GQY9X52ZPJ]] shows.

### The converse

The formulas give the distance, and the proof shows more: in both parts the closest points are unique.
In the plane $\mathbb{R}^2$ there is no cross product, and the [[point-line formula|01AAYNSBN6]] uses a normal vector instead.

### Beyond three dimensions

The distance from a point $q$ to an affine subspace $a + W$ of $\mathbb{R}^n$ is $\|u - \operatorname{proj}_W u\|$ with $u = q - a$.
The sub-area on [[orthogonality and least squares|8GQVME4SZZ]] proves this with the [[orthogonal projection|0B8KZRT28M]].
Both parts of the theorem are special cases: in part 2, $W$ is the plane spanned by $d$ and $e$.

## Explanations

### L1 human

The shortest way from a point to a pole, or between two poles, goes straight and meets them at right angles.
These two formulas measure that shortest way, for a point and a line, and for two lines that are not parallel.

### L2 human

Each formula is a length divided by a length.
In part 1 the numerator is the area of the parallelogram on $q - a$ and $d$, and dividing by the base $\|d\|$ leaves the height.
In part 2 the numerator is the volume of the box on $b - a$, $d$ and $e$, and dividing by the base area $\|d \times e\|$ leaves the height.
Watch out: in part 1 the cross product is taken with $q - a$, not with $q$ itself.
