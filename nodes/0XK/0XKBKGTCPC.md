---
tag: 0XKBKGTCPC
kind: concept
name: Length of a vector
aliases: [magnitude-of-a-vector, euclidean-norm]
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Length
  - url: https://en.wikipedia.org/wiki/Norm_(mathematics)
    locator: Euclidean norm
  - book: isbn:9781733146678
    locator: Section 1.2
---

## Summary

The length of a [[vector|0QN3D80AWP]] says how far its move goes, and the Pythagorean theorem computes it from the components.
For $v = (v_1, \dots, v_n)$ in $\mathbb{R}^n$ the length, also called the magnitude or the Euclidean norm, is the nonnegative number
$$\|v\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}.$$
It is the distance from the start to the end of any arrow that represents $v$, and the [[formal definition|0DZS7ZG0QY]] states it for every $n$.
With the length come unit vectors, which keep only a direction, and the distance $\|B - A\|$ between two points.

## Motivation

In the plane the arrow of $v = (v_1, v_2)$ is the long side of a right triangle whose legs have lengths $|v_1|$ and $|v_2|$.
The [[Pythagorean theorem|0VP3A1290K]] gives the length $\sqrt{v_1^2 + v_2^2}$.
In space the arrow of $(v_1, v_2, v_3)$ is the diagonal of a box with edges $|v_1|$, $|v_2|$ and $|v_3|$.
The diagonal of the bottom face has length $\sqrt{v_1^2 + v_2^2}$, and a second right triangle, standing on that diagonal, gives $\sqrt{v_1^2 + v_2^2 + v_3^2}$.
For $n \ge 4$ there is no picture, so we take the same formula as the definition.

Length is the first piece of geometry added to the algebra of vectors.
It measures the size of a force, the speed of a velocity and the error of an approximation.
The [[dot product|0S52TNNTH9]] on the next pages adds angles, and it contains the length as the special case $\|v\|^2 = v \cdot v$.

## Notation

The length is written $\|v\|$ or $|v|$; physics books often write $v$ in plain type for the length of the bold vector $\mathbf{v}$.
The unit vector in the direction of $v \neq 0$ is $\hat v = v / \|v\|$.
The distance between points $A$ and $B$ is $d(A, B) = \|B - A\|$, the [[Euclidean distance|0NPPGHQNXQ]].
Later sub-areas write $\|v\|_2$ to tell this length apart from other [[norms|0V2WP9B1MF]], such as $\|v\|_1 = |v_1| + \dots + |v_n|$.

## Remarks

### A first computation

Square each component, add, and take the square root.
For $v = (3, 4)$ this gives
$$\|v\| = \sqrt{3^2 + 4^2} = \sqrt{25} = 5.$$
In space, $\|(2, -1, 2)\| = \sqrt{4 + 1 + 4} = 3$, and in $\mathbb{R}^4$, $\|(1, 1, 1, 1)\| = \sqrt{4} = 2$.
Each standard unit vector $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ has length $1$, because it has one component $1$ and the others $0$.

### Unit vectors and distances

Dividing a nonzero vector by its length gives a vector of length $1$ with the same direction.
For $v = (2, -1, 2)$ the unit vector is $\tfrac{1}{3} v = \left(\tfrac{2}{3}, -\tfrac{1}{3}, \tfrac{2}{3}\right)$, and the [[worked example|PHDF089S8P]] checks that its length is $1$.
The distance between two points is the length of the vector between them.
From $A = (1, 2, 3)$ to $B = (4, 6, 15)$ the vector is $(3, 4, 12)$, so
$$d(A, B) = \sqrt{9 + 16 + 144} = \sqrt{169} = 13,$$
and the [[distance example|M2J9EPM1WJ]] shows how two Pythagorean triples hide in this number.

### The rules you can use

The length is positive: $\|v\| \ge 0$, and $\|v\| = 0$ only for $v = 0$, because a sum of squares is zero only when each square is zero.
It is homogeneous: $\|cv\| = |c| \, \|v\|$ for each real number $c$, because $\sqrt{c^2 a} = |c| \sqrt{a}$ for $a \ge 0$.
Homogeneity is what makes $v / \|v\|$ a unit vector, since $\|v / \|v\|\| = \|v\| / \|v\| = 1$.
The length also obeys the triangle inequality $\|u + v\| \le \|u\| + \|v\|$: a side of a triangle is never longer than the other two sides together.
Its proof needs the [[Cauchy-Schwarz inequality|0RFWW56Y22]], and the [[triangle inequality for norms|0FJZMBX0ZZ]] gives it in full.

### What is not a length

The sum of the components is not a length: $(1, -1)$ has the sum $0$, but it is not the zero vector, so positivity fails.
The sum of the absolute values is a norm, but a different one.
The [[taxicab example|WW2RB40VYX]] shows that it gives $7$ for $(3, 4)$, not $5$.
The sum of squares $v_1^2 + \dots + v_n^2$ without the root is the square of the length; it fails homogeneity, because doubling $v$ multiplies it by $4$.

### Watch out

The length is not additive.
For $u = (1, 0)$ and $v = (0, 1)$,
$$\|u + v\| = \|(1, 1)\| = \sqrt{2}, \qquad \text{but} \qquad \|u\| + \|v\| = 2.$$
Only the inequality $\le$ holds, with equality when one vector is a nonnegative multiple of the other.
A length is also never negative, so $\|-3v\| = 3\|v\|$, not $-3\|v\|$.
And square the negative components too: $\|(2, -1, 2)\|^2 = 4 + 1 + 4$, not $4 - 1 + 4$.

### History

Descartes and Fermat brought coordinates into geometry in the 17th century, and with coordinates the Pythagorean theorem became the formula for the length.
The double-bar notation $\|v\|$ came into use in the 20th century, with the theory of normed spaces.

### Try it

Find the length of $(1, -2, 2, 4)$ in $\mathbb{R}^4$.
The squares add to $1 + 4 + 4 + 16 = 25$, so the length is $5$.

Find all numbers $t$ with $\|(t, 3)\| = 5$.
You need $t^2 + 9 = 25$, so $t^2 = 16$ and $t = 4$ or $t = -4$.

## Explanations

### L1 human

The length of a vector is how far the vector moves you.
The vector $(3, 4)$ goes 3 to the right and 4 up.
These two moves are the legs of a right triangle, and the vector is the long side.
By the Pythagorean theorem the long side is $\sqrt{3 \cdot 3 + 4 \cdot 4} = \sqrt{25} = 5$.
So the length of $(3, 4)$ is $5$.

### L2 human

Here is a typical problem: find the point at distance $6$ from $A = (0, 1, 0)$ in the direction of $v = (1, -2, 2)$.
First find the length of $v$:
$$\|v\|^2 = 1 + 4 + 4 = 9, \qquad \|v\| = 3.$$
The unit vector in the direction of $v$ is $\hat v = \tfrac{1}{3}(1, -2, 2)$.
A step of length $6$ in that direction is $6 \hat v = (2, -4, 4)$, so the point is
$$A + 6 \hat v = (0, 1, 0) + (2, -4, 4) = (2, -3, 4).$$
Check: $\|(2, -3, 4) - A\| = \|(2, -4, 4)\| = \sqrt{36} = 6$.
The problem shows the two everyday uses of length: to normalize a direction, and to measure a distance.

### L3 human

The length is the norm that the dot product induces, $\|v\| = \sqrt{v \cdot v}$.
Positivity, homogeneity and the triangle inequality are the three axioms of a [[norm|0V2WP9B1MF]], and the Euclidean length is one norm among many, such as the $p$-norms.
It is special because it satisfies the [[parallelogram law|026HPGYGS4]] $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.
By the Jordan-von Neumann theorem, exactly the norms with this law come from an inner product, and the sub-area on [[inner product spaces|1D4JTZ9VS3]] treats them.
The length is also unchanged by rotations and reflections, and these maps form the orthogonal group of the sub-area on [[isometries|AZS5BPF5H3]].
