---
tag: 0DZS7ZG0QY
kind: definition
name: Length of a vector
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
defines: 0XKBKGTCPC
uses: [0QN3D80AWP]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: Length
---

## Definition

The length of a vector is the square root of the sum of the squares of its components.
Let $n$ be a positive integer and let $v = (v_1, \dots, v_n)$ be a [[vector|0QN3D80AWP]] in $\mathbb{R}^n$.
The length of $v$ is the nonnegative real number
$$\|v\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}.$$
A unit vector is a vector of length $1$.
The distance between two points $A$ and $B$ of $\mathbb{R}^n$ is $\|B - A\|$.

## Notation

Other names for the length are the magnitude and the Euclidean norm.
The notation $|v|$ is also common, mainly in physics and in school books.
With the [[dot product|0S52TNNTH9]] the formula reads $\|v\| = \sqrt{v \cdot v}$.

## Remarks

The definition is the Pythagorean theorem applied to the components, and the [[concept page on length|0XKBKGTCPC]] draws the right triangles behind it.
The square root is taken of a sum of squares, so it always exists and is never negative.
The squares are what make the sign of a component irrelevant: $(3, -4)$ and $(3, 4)$ both have length $5$.

Two consequences follow at once.
First, $\|v\| = 0$ only when every $v_i^2 = 0$, that is, only for the zero vector.
Second, for each real number $c$ we get $\|cv\| = \sqrt{c^2 (v_1^2 + \dots + v_n^2)} = |c| \, \|v\|$, so for $v \neq 0$ the vector $v / \|v\|$ is a unit vector.
The zero vector fails here: it has length $0$, and $0 / 0$ has no meaning, so the zero vector has no unit vector in its direction.

## Explanations

### L1 human

The length of a vector is how far the vector moves you.
In the plane, the vector $(3, 4)$ is the long side of a right triangle with legs 3 and 4.
So its length is $\sqrt{3^2 + 4^2} = 5$.

### L2 human

To compute a length, square each component, add the squares, and take the square root.
For $v = (1, 2, 2)$ this gives
$$\|v\| = \sqrt{1 + 4 + 4} = \sqrt{9} = 3.$$
Watch out: square the negative components too, so $\|(1, -2)\|^2 = 1 + 4 = 5$, not $1 - 4$.
