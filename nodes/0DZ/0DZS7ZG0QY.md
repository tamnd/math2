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

Let $n$ be a positive integer and let $v = (v_1, \dots, v_n)$ be a [[vector|0QN3D80AWP]] in $\mathbb{R}^n$.
The length of $v$ is the nonnegative real number
$$\|v\| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}.$$
A unit vector is a vector of length $1$.
The distance between two points $A$ and $B$ of $\mathbb{R}^n$ is $\|B - A\|$.

## Notation

Other names for the length are the magnitude and the Euclidean norm.
The notation $|v|$ is also common, mainly in physics and in school books.
With the [[dot product|0S52TNNTH9]], the formula reads $\|v\| = \sqrt{v \cdot v}$.

## Remarks

For each vector $v$, $\|v\| \geq 0$, and $\|v\| = 0$ if and only if $v$ is the zero vector.
For each real number $c$, $\|cv\| = |c| \, \|v\|$.
Thus for $v \neq 0$ the vector $v / \|v\|$ is a unit vector.

## Explanations

### L1 human

The length of a vector is how far the vector moves us.
In the plane, the vector $(3, 4)$ is the long side of a right triangle with legs 3 and 4.
So its length is $\sqrt{3^2 + 4^2} = 5$.

### L2 human

To compute a length, square each component, add the squares, and take the square root.
For $v = (1, 2, 2)$: $1 + 4 + 4 = 9$, so $\|v\| = 3$.
A trap: square the negative components too, so $\|(1, -2)\|^2 = 1 + 4 = 5$.
