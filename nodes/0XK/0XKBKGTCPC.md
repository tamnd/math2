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

The length (or magnitude, or Euclidean norm) of a [[vector|0QN3D80AWP]] $v = (v_1, \dots, v_n)$ in $\mathbb{R}^n$ is the nonnegative real number
$$\|v\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}.$$
It is the distance from the start point to the end point of any arrow that represents $v$.
The [[formal definition|0DZS7ZG0QY]] states it for all $n$.
The length matters because it measures sizes and distances, and it is the first piece of the geometry that the [[dot product|0S52TNNTH9]] adds to vector algebra.

## Motivation

In the plane, the arrow of $v = (v_1, v_2)$ is the hypotenuse of a right triangle with legs of lengths $|v_1|$ and $|v_2|$.
The [[Pythagorean theorem|0VP3A1290K]] gives the length $\sqrt{v_1^2 + v_2^2}$.
In space, the arrow of $(v_1, v_2, v_3)$ is the diagonal of a box with edges $|v_1|$, $|v_2|$ and $|v_3|$.
Two uses of the Pythagorean theorem give $\sqrt{v_1^2 + v_2^2 + v_3^2}$.
In $\mathbb{R}^n$ for $n \geq 4$ there is no picture, and we take the same formula as the definition.

## Notation

- The length is written $\|v\|$, $|v|$ or $\lvert \mathbf{v} \rvert$. Physics books often write $v$ for the length of $\mathbf{v}$.
- The unit vector in the direction of $v \neq 0$ is $\hat v = v / \|v\|$.
- The distance between points $A$ and $B$ is $d(A, B) = \|B - A\|$, the [[Euclidean distance|0NPPGHQNXQ]].
- Later sub-areas write $\|v\|_2$ to separate this norm from other [[norms|0V2WP9B1MF]].

## Remarks

### Examples

- $\|(3, 4)\| = \sqrt{9 + 16} = 5$.
- $\|(2, -1, 2)\| = \sqrt{4 + 1 + 4} = 3$, so $(\tfrac{2}{3}, -\tfrac{1}{3}, \tfrac{2}{3})$ is a unit vector. The [[worked example|PHDF089S8P]] gives the details.
- $\|(1, 1, 1, 1)\| = \sqrt{4} = 2$ in $\mathbb{R}^4$.
- The distance from $(1, 2, 3)$ to $(4, 6, 15)$ is $\|(3, 4, 12)\| = 13$. The [[distance example|M2J9EPM1WJ]] computes it step by step.
- Each standard unit vector $\mathbf{i}$, $\mathbf{j}$, $\mathbf{k}$ has length $1$.

### Non-examples

- The sum of the components is not a length: $(1, -1)$ has sum $0$, but it is not the zero vector.
- The sum of the absolute values of the components is a [[norm|0V2WP9B1MF]], but it is not the Euclidean length. The [[taxicab non-example|WW2RB40VYX]] shows that it gives $7$ for $(3, 4)$, not $5$.
- The expression $v_1^2 + v_2^2$ without the square root is the square of the length, not the length. It is not homogeneous of degree $1$: doubling $v$ multiplies it by $4$.

### Basic properties

- Positivity: $\|v\| \geq 0$, and $\|v\| = 0$ if and only if $v = 0$. A sum of squares is zero only when each square is zero.
- Homogeneity: $\|cv\| = |c| \, \|v\|$ for each real number $c$. The reason is $\sqrt{c^2 a} = |c| \sqrt{a}$ for $a \geq 0$.
- So for $v \neq 0$, the vector $v / \|v\|$ is a unit vector with the direction of $v$.
- The triangle inequality $\|u + v\| \leq \|u\| + \|v\|$ holds. Its proof needs the Cauchy-Schwarz inequality, and it is the [[triangle inequality for norms|0FJZMBX0ZZ]].
- In terms of the [[dot product|0S52TNNTH9]], $\|v\| = \sqrt{v \cdot v}$.

### History

Descartes and Fermat introduced coordinates in geometry in the 17th century.
With coordinates, the Pythagorean theorem becomes the formula for the length.
The double bar notation $\|v\|$ came into use in the 20th century, with the theory of normed spaces.

### Common errors

- Students write $\|u + v\| = \|u\| + \|v\|$. This is false in general: $\|(1, 0) + (0, 1)\| = \sqrt{2}$, not $2$.
- Students write $\|-3v\| = -3\|v\|$. A length is never negative, and the correct value is $3\|v\|$.
- Students forget to square negative components: $\|(2, -1, 2)\|^2 = 4 + 1 + 4$, not $4 - 1 + 4$.

## Explanations

### L1 human

The length of a vector is how far the vector moves us.
The vector $(3, 4)$ goes 3 to the right and 4 up.
These two moves are the legs of a right triangle, and the vector is the long side.
By the Pythagorean theorem the long side is $\sqrt{3 \cdot 3 + 4 \cdot 4} = \sqrt{25} = 5$.
So the length of $(3, 4)$ is $5$.

### L2 human

Worked example: the unit vector in the direction of $v = (1, -2, 2)$, and the point at distance $6$ from $A = (0, 1, 0)$ in this direction.

1. $\|v\|^2 = 1 + 4 + 4 = 9$, so $\|v\| = 3$.
2. The unit vector is $\hat v = \tfrac{1}{3}(1, -2, 2) = (\tfrac{1}{3}, -\tfrac{2}{3}, \tfrac{2}{3})$.
3. The point is $A + 6 \hat v = (0, 1, 0) + (2, -4, 4) = (2, -3, 4)$.
4. Check: $\|(2, -3, 4) - A\| = \|(2, -4, 4)\| = \sqrt{36} = 6$.

The typical use is to normalize a direction, as in step 2, and to measure distances, as in step 4.
A trap: the length is not linear.
In general $\|u + v\| \neq \|u\| + \|v\|$, and only the inequality $\leq$ holds.

### L3 human

The length is the norm induced by the dot product: $\|v\| = \sqrt{v \cdot v}$.
Positivity, homogeneity and the triangle inequality are the three axioms of a [[norm|0V2WP9B1MF]], and the Euclidean length is one example among many, such as the $p$-norms.
The Euclidean length is special because it satisfies the [[parallelogram law|026HPGYGS4]] $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.
By the Jordan-von Neumann theorem, exactly the norms with this law come from an inner product; the sub-area on [[inner product spaces|1D4JTZ9VS3]] treats them.
The length is also invariant under rotations and reflections, and these maps form the orthogonal group of the sub-area on [[isometries|AZS5BPF5H3]].
