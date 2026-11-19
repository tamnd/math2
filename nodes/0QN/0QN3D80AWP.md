---
tag: 0QN3D80AWP
kind: concept
name: Euclidean vector
aliases: [vector, geometric-vector]
msc: ["51N20", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
uses: [0XPR1E85W0, 0RWKYX8339]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_vector
    locator: lead section
  - book: isbn:9781733146678
    locator: Chapter 1
  - url: https://understandinglinearalgebra.org/
    locator: Section 2.1
same_as:
  wikidata: Q44528
  wikipedia: Euclidean vector
---

## Summary

A Euclidean vector in the plane or in space is a quantity with a length and a direction.
We draw it as an arrow, and two arrows give the same vector when a translation moves one onto the other.
In [[Cartesian coordinates|0RWKYX8339]] a vector in [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$ is a list $v = (v_1, \dots, v_n)$ of $n$ real numbers, its components.
The arrow from the point $A$ to the point $B$ gives the vector $\overrightarrow{AB} = B - A$, computed component by component.
We add two vectors component by component, and we multiply a vector by a real number (a scalar) component by component.
The [[formal definition|00EBGSR5NY]] gives these operations exactly.
Vectors matter because they describe displacements, forces and velocities, and because their algebra turns many geometric problems into calculations.

## Motivation

A displacement "3 steps east and 4 steps north" does not depend on the start point.
Two such displacements, done one after the other, give a third displacement.
A force or a velocity has the same behaviour: it has a size and a direction, and two of them combine to a resultant.
Numbers alone cannot record a direction, and points alone cannot be added in a meaningful way.
The vector is the object that records "how far and in which direction", and that we can add and stretch.
With coordinates, these operations become operations on lists of numbers.
So geometry in the plane and in space becomes algebra, and the same algebra then works for lists of any length.

## Notation

- Books write a vector as $v$, $\mathbf{v}$ (bold), $\vec v$ or $\underline{v}$. Handwriting usually uses $\vec v$ or $\underline{v}$.
- The vector from $A$ to $B$ is $\overrightarrow{AB}$. The position vector of a point $P$ is $\overrightarrow{OP}$, where $O$ is the origin.
- Components are written as a row $(v_1, v_2, v_3)$, as a column $\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}$, or as $v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$.
- Some books use rows for points and columns for vectors. Matrix books (for example Strang and Lay) use columns for vectors.
- The zero vector is $0$, $\mathbf{0}$ or $\vec 0$.

## Remarks

### Examples

- The vector from $A = (1, 2)$ to $B = (4, 6)$ is $\overrightarrow{AB} = (3, 4)$. The [[worked example|~8b8b3ceb]] adds it to another vector by the parallelogram rule.
- The position vector of the point $P = (2, -1, 5)$ is $\overrightarrow{OP} = (2, -1, 5)$. Each point has exactly one position vector.
- The standard unit vectors $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ and $\mathbf{k} = (0, 0, 1)$ have length $1$. Each vector of $\mathbb{R}^3$ is $v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$.
- A velocity of $3$ m/s east and $4$ m/s north is the vector $(3, 4)$. Its speed is $5$ m/s.
- A list of $4$ measurements, such as $(20, 18, 25, 22)$, is a vector of $\mathbb{R}^4$. The [[example on lists|~f5e61e59]] computes with such vectors.

### Non-examples

- A point is not a vector. Two points cannot be added in a meaningful way, because the sum depends on the choice of the origin.
- A rotation by a fixed angle about an axis has a size and a direction, but it is not a vector. The [[non-example of rotations|~34c4d369]] shows that two rotations do not commute, while vector addition does.
- A temperature has a size but no direction. It is a scalar, not a vector.

### Basic properties

- Addition is commutative and associative, the zero vector is neutral, and $v + (-v) = 0$.
- For scalars $a$ and $b$: $a(u + v) = au + av$, $(a + b)v = av + bv$, $(ab)v = a(bv)$ and $1v = v$.
- These eight rules make $\mathbb{R}^n$ a [[vector space|000AYPA9AJ]] over $\mathbb{R}$.
- For any three points: $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ (the triangle rule).
- The parallelogram rule: if $u = \overrightarrow{AB}$ and $v = \overrightarrow{AD}$, then $u + v = \overrightarrow{AC}$, where $ABCD$ is a parallelogram.
- The scalar multiple $cv$ is parallel to $v$. It has the same direction when $c > 0$ and the opposite direction when $c < 0$.

### History

Hamilton introduced the word "vector" in the 1840s, in his work on quaternions.
Grassmann published a general theory of quantities with direction in 1844.
Gibbs and Heaviside separated the vector algebra from the quaternions in the 1880s, and their notation is the one used in physics today.

### Common errors

- Students confuse a point with its position vector. The point $(2, 3)$ is a place, and the vector $(2, 3)$ is a displacement from any start point.
- Students compute $\overrightarrow{AB}$ as $A - B$. The correct rule is "end minus start": $\overrightarrow{AB} = B - A$.
- Students think that vectors at different places are different. A vector has no fixed start point, so arrows of equal length and direction are equal.

## Explanations

### L1 human

A vector is an instruction for a move: how far and in which direction.
The vector $(3, 4)$ in the plane means "3 to the right and 4 up".
The start point does not matter, so all arrows with this length and direction show the same vector.
Two moves done one after the other give a new move.
For example, $(3, 4)$ and then $(2, -1)$ give $(5, 3)$, because $3 + 2 = 5$ and $4 - 1 = 3$.
Doubling a vector doubles the move: $2 \cdot (3, 4) = (6, 8)$.

### L2 human

Worked example: the points $A = (1, 0, 2)$, $B = (3, 1, 0)$ and $C = (0, 4, 1)$ in space.

1. $\overrightarrow{AB} = B - A = (3 - 1, 1 - 0, 0 - 2) = (2, 1, -2)$.
2. $\overrightarrow{BC} = C - B = (0 - 3, 4 - 1, 1 - 0) = (-3, 3, 1)$.
3. The sum is $\overrightarrow{AB} + \overrightarrow{BC} = (-1, 4, -1)$.
4. Directly, $\overrightarrow{AC} = C - A = (-1, 4, -1)$. This agrees with step 3, as the triangle rule says.
5. The midpoint $M$ of $AB$ has the position vector $\tfrac{1}{2}(A + B) = (2, \tfrac{1}{2}, 1)$.

The typical use is to translate a geometric statement into an equation between vectors.
For example, "$ABCD$ is a parallelogram" becomes $\overrightarrow{AB} = \overrightarrow{DC}$.
A trap: the equation $\overrightarrow{AB} = \overrightarrow{CD}$ does not say that the segments are the same, only that they are parallel, of equal length and of the same direction.

### L3 human

The arrows of the plane form a real [[vector space|000AYPA9AJ]] of dimension $2$, and a choice of origin and of two axes identifies it with $\mathbb{R}^2$.
The points of the plane do not form a vector space but an [[affine space|09XNAPTJQ7]]: we can subtract two points, but we cannot add them.
The later sub-area on [[vector spaces and bases|MVH97H8B2J]] keeps only the eight rules of addition and scalar multiplication, and studies all sets that satisfy them.
Length and angle are extra structure, which the dot product gives; the sub-area on [[inner product spaces|1D4JTZ9VS3]] generalizes this structure.
In physics, the "vector" of a quantity also says how its components change under a rotation of the axes.
