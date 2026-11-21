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

A vector records a move: how far, and in which direction.
We draw it as an arrow, and two arrows give the same vector when a translation slides one onto the other, so a vector has no fixed starting point.
In [[Cartesian coordinates|0RWKYX8339]] a Euclidean vector in [[Euclidean space|0XPR1E85W0]] $\mathbb{R}^n$ is a list of $n$ real numbers, its components:
$$v = (v_1, v_2, \dots, v_n).$$
The arrow from a point $A$ to a point $B$ gives the vector $\overrightarrow{AB} = B - A$, end minus start, component by component.
Vectors are added component by component, and a real number $c$, a scalar, multiplies each component; the [[formal definition|00EBGSR5NY]] states these rules exactly.

## Motivation

A walk of "3 steps east and 4 steps north" means the same thing wherever you start.
Two walks done one after the other make a third walk, and that is the sum of two vectors.
Forces and velocities behave the same way: each has a size and a direction, and two of them combine into one resultant.
A single number cannot record a direction, and points cannot be added in any useful way, so geometry needs a new object for "how far and which way".

Once vectors have coordinates, their operations become operations on lists of numbers.
That turns geometry in the plane and in space into algebra, and the same algebra works for lists of any length, such as the four sales figures of a week or the thousand pixels of an image.
Every later page of the sub-area, from the [[length|0XKBKGTCPC]] of a vector to the [[cross product|0N5N15HWZ7]], builds on these two operations.

## Notation

Books write a vector as $v$, as $\mathbf{v}$ in bold, or as $\vec v$, and handwriting usually uses $\vec v$ or $\underline{v}$.
The vector from $A$ to $B$ is $\overrightarrow{AB}$, and the position vector of a point $P$ is $\overrightarrow{OP}$, where $O$ is the origin.
The components can be written as a row $(v_1, v_2, v_3)$, as a column $\begin{pmatrix} v_1 \\ v_2 \\ v_3 \end{pmatrix}$, or as $v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$.
Matrix books such as Strang and Lay treat vectors as columns, while some books write points as rows and vectors as columns; read the convention before you compare formulas.

## Remarks

### A first computation

Take the points $A = (1, 2)$ and $B = (4, 6)$ in the plane.
The vector from $A$ to $B$ is end minus start:
$$\overrightarrow{AB} = (4 - 1, \; 6 - 2) = (3, 4).$$
Add the vector $v = (2, -1)$ to it, component by component:
$$(3, 4) + (2, -1) = (5, 3).$$
If you draw $(3, 4)$ and $(2, -1)$ from the same point and complete the parallelogram, the diagonal from that point is $(5, 3)$; the [[parallelogram example|DPADSQ4DFJ]] checks every corner.
A scalar stretches the arrow: $2 \cdot (3, 4) = (6, 8)$ points the same way and is twice as long, and $-1 \cdot (3, 4) = (-3, -4)$ points the opposite way.

### Special vectors and vectors that are lists

Some vectors get names.
The zero vector $0 = (0, \dots, 0)$ is the move that goes nowhere, and $v + 0 = v$ for every $v$.
The standard unit vectors of space are $\mathbf{i} = (1, 0, 0)$, $\mathbf{j} = (0, 1, 0)$ and $\mathbf{k} = (0, 0, 1)$, and every vector of $\mathbb{R}^3$ is $v_1 \mathbf{i} + v_2 \mathbf{j} + v_3 \mathbf{k}$.
Each point $P$ has exactly one position vector $\overrightarrow{OP}$, with the same components as $P$.

A vector need not be an arrow that you can draw.
A velocity of 3 m/s east and 4 m/s north is the vector $(3, 4)$ of the plane, but the sales of a shop on four days, $(20, 18, 25, 22)$, are a vector of $\mathbb{R}^4$.
The [[example on lists of measurements|30AYM35BMY]] adds and scales such lists with the same rules.

### The rules you can use

Each rule of vector arithmetic follows from the same rule for real numbers, applied in each component.
Addition is commutative and associative, $0$ is neutral, and $v + (-v) = 0$.
For scalars $a$ and $b$,
$$a(u + v) = au + av, \quad (a + b)v = av + bv, \quad (ab)v = a(bv), \quad 1v = v.$$
These eight rules make $\mathbb{R}^n$ a [[vector space|000AYPA9AJ]] over $\mathbb{R}$.
In the plane two rules have pictures: the triangle rule $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$, and the parallelogram rule, which says that if $ABCD$ is a parallelogram then $\overrightarrow{AB} + \overrightarrow{AD} = \overrightarrow{AC}$.
A multiple $cv$ is parallel to $v$, with the same direction when $c > 0$ and the opposite direction when $c < 0$.

### What is not a vector

A point is not a vector.
If you add the points $(1, 0)$ and $(0, 1)$ you get $(1, 1)$, but move the origin to $(1, 0)$ and the same two points become $(0, 0)$ and $(-1, 1)$, whose sum names a different place; the sum depends on the choice of origin.
A temperature has a size but no direction, so it is a scalar.
A rotation about an axis has a size, the angle, and a direction, the axis, but it is still not a vector.
The [[example of two quarter turns|AW7Q0F3M8J]] shows that the result of two rotations depends on their order, while $u + v = v + u$ for vectors.

### Watch out

The most common slip is to compute $\overrightarrow{AB}$ as $A - B$.
For $A = (1, 2)$ and $B = (4, 6)$ that gives $(-3, -4)$, the arrow from $B$ back to $A$; the correct rule is end minus start, $\overrightarrow{AB} = B - A = (3, 4)$.
A second slip is to think that arrows at different places are different vectors.
The arrow from $(0, 0)$ to $(3, 4)$ and the arrow from $(5, 5)$ to $(8, 9)$ are the same vector $(3, 4)$.

### History

Hamilton introduced the word "vector" in the 1840s, in his work on quaternions.
Grassmann published a general theory of quantities with direction in 1844.
In the 1880s Gibbs and Heaviside separated vector algebra from the quaternions, and their notation is the one physics uses today.

### Try it

Find $\overrightarrow{PQ}$ for $P = (2, -1, 5)$ and $Q = (0, 3, 5)$.
End minus start gives $(0 - 2, 3 + 1, 5 - 5) = (-2, 4, 0)$.

Find the number $c$ with $c \, (2, -1) + (1, 3) = (7, 0)$.
The first component gives $2c + 1 = 7$, so $c = 3$, and the second component agrees: $-3 + 3 = 0$.

## Explanations

### L1 human

A vector is an instruction for a move: how far and in which direction.
The vector $(3, 4)$ in the plane means "3 to the right and 4 up".
The start point does not matter, so all arrows with this length and direction show the same vector.
Two moves done one after the other give a new move.
For example, $(3, 4)$ and then $(2, -1)$ give $(5, 3)$, because $3 + 2 = 5$ and $4 - 1 = 3$.
Doubling a vector doubles the move: $2 \cdot (3, 4) = (6, 8)$.

### L2 human

Here is a typical computation with the three points $A = (1, 0, 2)$, $B = (3, 1, 0)$ and $C = (0, 4, 1)$ in space.
First find the two sides that meet at $B$:
$$\overrightarrow{AB} = B - A = (2, 1, -2), \qquad \overrightarrow{BC} = C - B = (-3, 3, 1).$$
Their sum is $(-1, 4, -1)$.
Check: directly, $\overrightarrow{AC} = C - A = (-1, 4, -1)$, as the triangle rule says.
The midpoint $M$ of $AB$ is halfway along $\overrightarrow{AB}$, so its position vector is
$$A + \tfrac{1}{2} \overrightarrow{AB} = \tfrac{1}{2}(A + B) = \left(2, \tfrac{1}{2}, 1\right).$$

The typical use is to turn a statement of geometry into an equation between vectors.
For example, "$ABCD$ is a parallelogram" becomes $\overrightarrow{AB} = \overrightarrow{DC}$, and the [[vector proofs in plane geometry|ZVEKWJTSV7]] work in this way.
Watch out: $\overrightarrow{AB} = \overrightarrow{CD}$ does not say that the segments are the same, only that they are parallel, equally long and point the same way.

### L3 human

The arrows of the plane form a real [[vector space|000AYPA9AJ]] of dimension $2$, and a choice of origin and of two axes identifies it with $\mathbb{R}^2$.
The points of the plane form an [[affine space|09XNAPTJQ7]] instead: you can subtract two points to get a vector, and add a vector to a point, but you cannot add two points.
The sub-area on [[vector spaces and bases|MVH97H8B2J]] keeps only the eight rules of addition and scalar multiplication, and studies every set that obeys them.
Length and angle are extra structure, given by the [[dot product|0S52TNNTH9]], and the sub-area on [[inner product spaces|1D4JTZ9VS3]] studies that structure in general.
In physics a vector quantity also carries a rule for how its components change when the axes rotate, which is the first step toward tensors.
