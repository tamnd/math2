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

Let $\operatorname{dist}(S, T)$ be the least [[distance|0NPPGHQNXQ]] $\|s - t\|$ for $s \in S$, $t \in T$, as in the [[concept|C6GAS92QHX]].
Let $q \in \mathbb{R}^3$.

1. Let $L$ be the [[line|0399QFDFS8]] $a + t d$ with $d \neq 0$. Then $\operatorname{dist}(q, L) = \dfrac{\|(q - a) \times d\|}{\|d\|}$, and the least value is reached.
2. Let $L_1 = \{a + t d\}$ and $L_2 = \{b + s e\}$ with $m = d \times e \neq 0$. Then $\operatorname{dist}(L_1, L_2) = \dfrac{|(b - a) \cdot m|}{\|m\|}$, and the least value is reached.

The distance from a point to a plane is the [[point-plane formula|0K1E2S6Z69]].

## Remarks

### Why each hypothesis is needed

- The condition $d \neq 0$ makes $L$ a line.
- The condition $d \times e \neq 0$ says that the lines are not parallel. For parallel lines, $m = 0$ and the formula is $\tfrac{0}{0}$; part 1 gives the distance instead.

### Consequences

- Non-parallel lines meet if and only if $(b - a) \cdot (d \times e) = 0$.
- The closest points are the feet of the common perpendicular, as the proof constructs.
- Parallel lines $a + t d$ and $b + s d$ have the distance $\dfrac{\|(b - a) \times d\|}{\|d\|}$, by part 1 with $q = b$.
- In the plane $\mathbb{R}^2$ the [[point-line formula|01AAYNSBN6]] uses a normal vector instead of a cross product.

### Converse

The formulas give the distance, and the proof gives the closest points.
The closest points are unique in both parts.

### Generalizations

The distance from a point to an affine subspace $a + W$ of $\mathbb{R}^n$ is $\|u - \operatorname{proj}_W u\|$ with $u = q - a$.
The sub-area on [[orthogonality and least squares|8GQVME4SZZ]] proves this with the [[orthogonal projection|0B8KZRT28M]].

## Explanations

### L1 human

The shortest way from a point to a wall, or to a pole, goes straight, at a right angle.
These two formulas measure the shortest way for a point and a line, and for two lines that are not parallel.

### L2 human

Each formula is a length divided by a length: the numerator is the size of a projection or a cross product, and the denominator removes the size of the normal or direction.
A trap: in part 1 the numerator is a cross product with $q - a$, not with $q$.
