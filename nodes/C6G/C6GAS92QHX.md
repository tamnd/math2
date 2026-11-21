---
tag: C6GAS92QHX
kind: concept
name: Distances between points, lines and planes
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0NPPGHQNXQ, 0399QFDFS8, 07SDJ5DNE4, 0JW13B48YP, 0N5N15HWZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_plane
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    locator: Vector formulation
  - url: https://en.wikipedia.org/wiki/Skew_lines
    locator: Distance
---

## Summary

The shortest path from a point to a line or a plane, or between two lines, always meets them at right angles, and that one picture turns every distance problem into a dot or cross product.
The distance between two sets $S$ and $T$ in $\mathbb{R}^3$ is the least [[Euclidean distance|0NPPGHQNXQ]] $\|s - t\|$ for $s \in S$ and $t \in T$.
For points, [[lines|0399QFDFS8]] and [[planes|07SDJ5DNE4]] this least value exists, and three formulas give it.

- Point $q$ and plane $n \cdot r = d$: $\dfrac{|n \cdot q - d|}{\|n\|}$.
- Point $q$ and line $a + t d$: $\dfrac{\|(q - a) \times d\|}{\|d\|}$.
- Lines $a + t d$ and $b + s e$ with $d \times e \neq 0$: $\dfrac{|(b - a) \cdot (d \times e)|}{\|d \times e\|}$.

The [[point-plane theorem|0K1E2S6Z69]] proves the first formula, and the [[distance theorem|Q6YGYNSY5H]] proves the other two.

## Motivation

Think of the shortest rope from a point $q$ to a sloping roof.
Pulled tight, it meets the roof at a right angle, so it runs along the normal $n$, and its length is the part of $q - a$ along $n$, for any point $a$ on the plane.
That part is a scalar [[projection|0JW13B48YP]], $|(q - a) \cdot n| / \|n\|$, and since $n \cdot a = d$ it equals the first formula.

For a line the shortest path is again perpendicular, now to the direction $d$.
Its length is the height of the parallelogram with sides $q - a$ and $d$, which is the area $\|(q - a) \times d\|$ divided by the base $\|d\|$.
For two skew lines the shortest segment is perpendicular to both, so it runs along the [[cross product|0N5N15HWZ7]] $d \times e$, and its length is the part of $b - a$ along that direction.

## Notation

The three distances are written $\operatorname{dist}(q, P)$, $\operatorname{dist}(q, L)$ and $\operatorname{dist}(L_1, L_2)$.
If the plane is in Hesse normal form $\hat n \cdot r = p$ with a unit normal $\hat n$, the first formula loses its denominator: $\operatorname{dist}(q, P) = |\hat n \cdot q - p|$.

## Remarks

### A first computation

Take the point $q = (1, 2, 3)$ and the plane $6x + 3y + 2z = 6$.
The normal $(6, 3, 2)$ has length $7$, and
$$\operatorname{dist}(q, P) = \frac{|6 + 6 + 6 - 6|}{7} = \frac{12}{7}.$$
The [[point example|QJJHWYGDQN]] also finds the closest point of the plane.

For a line, take $q = (1, 1, 1)$ and the line $t(1, 2, 2)$ through the origin.
Then $(q - 0) \times (1, 2, 2) = (0, -1, 1)$ has length $\sqrt{2}$, and $\|(1, 2, 2)\| = 3$, so the distance is $\tfrac{\sqrt{2}}{3}$.

For two lines, take $(1, 0, 0) + t(1, 1, 0)$ and $(0, 0, 2) + s(0, 1, 1)$.
Here $d \times e = (1, -1, 1)$ and $(b - a) \cdot (d \times e) = (-1, 0, 2) \cdot (1, -1, 1) = 1$, so the distance is $\tfrac{1}{\sqrt{3}}$.
The [[skew lines example|GQY9X52ZPJ]] finds the two closest points.

### The rules you can use

The distance is $0$ exactly when the two sets meet.
The closest point of the plane to $q$, the foot of the perpendicular, is $q - \dfrac{n \cdot q - d}{n \cdot n} \, n$.
The closest point of the line to $q$ is $a + \dfrac{(q - a) \cdot d}{d \cdot d} \, d$, by the [[projection theorem|NA6Q7ME9G0]].
Parallel lines $a + t d$ and $b + s d$ are at the distance of $b$ from the first line, $\|(b - a) \times d\| / \|d\|$.
Parallel planes $n \cdot r = d_1$ and $n \cdot r = d_2$ are at the distance $|d_1 - d_2| / \|n\|$.
Without the absolute value, the sign of $n \cdot q - d$ tells on which side of the plane $q$ lies.

### Watch out

The distance between two lines is not the distance between their base points.
For the two lines above, the base points are $\sqrt{5}$ apart, while the lines come within $\tfrac{1}{\sqrt{3}}$; the [[non-example|Q68F0665HJ]] works this out.

Do not forget the denominators $\|n\|$, $\|d\|$ and $\|d \times e\|$.
The number $|n \cdot q - d|$ alone is not a distance, because it doubles when the equation of the plane is multiplied by $2$, while the plane stays the same.
And the skew lines formula does not apply to parallel lines, where $d \times e = 0$ and it reads $\tfrac{0}{0}$; use the point-line formula instead.

### History

The distance from a point to a line in the plane, $|a x_0 + b y_0 + c| / \sqrt{a^2 + b^2}$, is a classical result of analytic geometry.
The vector forms with the cross product came with the vector analysis of Gibbs and Heaviside in the 1880s.

### Try it

How far is the origin from the plane $x + y + z = 3$, and which point of the plane is closest?
The distance is $\tfrac{3}{\sqrt{3}} = \sqrt{3}$, and the foot is $0 - \tfrac{-3}{3}(1, 1, 1) = (1, 1, 1)$.

How far apart are the parallel planes $x - 2y + 2z = 1$ and $x - 2y + 2z = 7$?
The normal has length $3$, so the distance is $\tfrac{|7 - 1|}{3} = 2$.

## Explanations

### L1 human

The distance from a point to a wall is the length of the shortest string from the point to the wall.
The shortest string meets the wall at a right angle.
The formulas find the length of this string without drawing it.

### L2 human

Here is a typical problem: find the distance from $q = (2, 0, 1)$ to the plane $x - 2y + 2z = 1$, and the closest point.
The normal $n = (1, -2, 2)$ has length $3$, and $n \cdot q - d = 2 - 0 + 2 - 1 = 3$, so the distance is $\tfrac{3}{3} = 1$.
The foot is
$$q - \tfrac{3}{9} n = (2, 0, 1) - \tfrac{1}{3}(1, -2, 2) = (\tfrac{5}{3}, \tfrac{2}{3}, \tfrac{1}{3}),$$
and $\tfrac{5}{3} - \tfrac{4}{3} + \tfrac{2}{3} = 1$ confirms that it lies on the plane.
The same steps serve collision tests in graphics and the fitting of points to planes.
Watch out: the formula needs the plane as $n \cdot r = d$; for $n \cdot r + c = 0$ the numerator becomes $|n \cdot q + c|$.

### L3 human

All three formulas are cases of one fact: the distance from a point to an affine subspace is the length of the component perpendicular to the subspace.
The sub-area on [[orthogonality and least squares|8GQVME4SZZ]] proves this for subspaces of any dimension, with the [[orthogonal projection|0B8KZRT28M]].
The skew lines case is the projection of $b - a$ onto the orthogonal complement of $\operatorname{span}\{d, e\}$.
