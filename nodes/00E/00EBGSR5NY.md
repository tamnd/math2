---
tag: 00EBGSR5NY
kind: definition
name: Euclidean vector
msc: ["51N20"]
topics: [VKVAJ94SKZ]
audience: school
defines: 0QN3D80AWP
uses: [0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: In Cartesian space
---

## Definition

A Euclidean vector is a list of real numbers, with addition and scaling done entry by entry.
Let $n$ be a positive integer.
A Euclidean vector in the [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$ is an element $v = (v_1, \dots, v_n)$ of $\mathbb{R}^n$, and the real numbers $v_1, \dots, v_n$ are its components.
For two points $A = (a_1, \dots, a_n)$ and $B = (b_1, \dots, b_n)$, the vector from $A$ to $B$ is
$$\overrightarrow{AB} = (b_1 - a_1, \dots, b_n - a_n).$$
The sum of two vectors $u$ and $v$ and the product of a real number $c$ and a vector $v$ are
$$u + v = (u_1 + v_1, \dots, u_n + v_n), \qquad c v = (c v_1, \dots, c v_n).$$
The zero vector is $0 = (0, \dots, 0)$, and the negative of $v$ is $-v = (-1)v$.

## Notation

The symbols $v$, $\mathbf{v}$ and $\vec v$ all denote vectors.
The position vector of a point $P$ is $\overrightarrow{OP}$, where $O$ is the origin, and its components are the coordinates of $P$.
In $\mathbb{R}^3$ the standard unit vectors are $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ and $\mathbf{k} = (0, 0, 1)$.

## Remarks

The definition identifies a vector with its components, and this hides the picture of an arrow that the [[concept of a Euclidean vector|0QN3D80AWP]] starts from.
The two views agree because the arrow from $A$ to $B$ and the arrow from $A'$ to $B'$ have the same components exactly when a translation moves one onto the other.
So $\overrightarrow{AB}$ depends only on the difference $B - A$, not on where the arrow starts.

The condition that the entries are real numbers matters.
For example, $(2, -1, 5)$ is a vector of $\mathbb{R}^3$, but $(1, i)$ is not a vector of $\mathbb{R}^2$, because $i$ is not real; it is a vector of $\mathbb{C}^2$, which the later sub-areas treat.
The length $n$ matters too: $(1, 2)$ and $(1, 2, 0)$ live in different spaces, and their sum is not defined.

With the sum and the product by real numbers, the vectors of $\mathbb{R}^n$ form a real vector space of dimension $n$.
For any three points the triangle rule $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ holds, because $(B - A) + (C - B) = C - A$ in each component.
A unit vector is a vector whose [[Euclidean length|0XKBKGTCPC]] is $1$.

## Explanations

### L1 human

A vector tells how to move: how far, and in which direction.
The vector $(3, 4)$ in the plane says "move 3 to the right and 4 up".
The start point does not matter, so arrows of the same length and direction are the same vector.

### L2 human

To find the vector between two points, subtract the start from the end in each component.
For $A = (1, 2, 3)$ and $B = (4, 0, 3)$ this gives
$$\overrightarrow{AB} = (4 - 1, \; 0 - 2, \; 3 - 3) = (3, -2, 0).$$
Then $2\overrightarrow{AB} = (6, -4, 0)$ and $\overrightarrow{AB} + (1, 1, 1) = (4, -1, 1)$.
Watch out: the order of the points matters, and $\overrightarrow{BA} = -\overrightarrow{AB} = (-3, 2, 0)$.
