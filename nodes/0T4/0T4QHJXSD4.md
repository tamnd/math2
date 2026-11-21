---
tag: 0T4QHJXSD4
kind: statement
role: proposition
name: The cross product is perpendicular to its factors
msc: ["15A72"]
topics: [VKVAJ94SKZ]
audience: school
about: [0N5N15HWZ7]
uses: [0N5N15HWZ7, 0S52TNNTH9, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Statement

This is the property that makes the cross product useful: it hands you a vector at a right angle to two given vectors.
Let $a$ and $b$ be vectors in $\mathbb{R}^3$, and let $a \times b$ be their [[cross product|0N5N15HWZ7]].
Let $u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$ be the [[dot product|0S52TNNTH9]].
Then
$$a \cdot (a \times b) = 0 \quad \text{and} \quad b \cdot (a \times b) = 0.$$
So $a \times b$ is [[perpendicular|03NK6RSRQ1]] to $a$ and to $b$.

## Remarks

### Why each hypothesis is needed

The statement holds for all $a, b \in \mathbb{R}^3$, with no exceptions.
If $a$ or $b$ is zero, or if they are parallel, then $a \times b = 0$, and the zero vector is perpendicular to every vector.
In those cases the statement is true but tells you nothing.

### What it gives you

When $a$ and $b$ are not parallel, they span a plane through $0$, and $a \times b$ is a normal vector of that plane.
That is how the page on the [[equation of a plane|07SDJ5DNE4]] finds a normal from two direction vectors.
By the linearity of the dot product, $a \times b$ is also perpendicular to every combination $sa + tb$, that is, to the whole plane.

The statement fits with volumes too.
The scalar triple products $a \cdot (a \times b)$ and $b \cdot (a \times b)$ are $0$, as they must be, since the [[scalar triple product|34VJYG6GVD]] of three vectors in one plane is $0$.

### The converse

If $a$ and $b$ are not parallel, then every vector perpendicular to both is a multiple of $a \times b$.
Such vectors solve two independent linear equations in three unknowns, so they form a line, and the nonzero vector $a \times b$ lies on it.
If $a$ and $b$ are parallel, the perpendicular vectors form a whole plane, and $a \times b = 0$ does not span it.

### Beyond three dimensions

In $\mathbb{R}^n$, a vector perpendicular to $n - 1$ given vectors comes from the formal determinant with first row $e_1, \dots, e_n$.
This generalized cross product takes $n - 1$ factors.
In $\mathbb{R}^7$ there is also a product of two vectors that is perpendicular to both factors.

## Explanations

### L1 human

Lay two pencils flat on a table, starting at the same point.
Their cross product points straight up from the table, or straight down.
So it makes a right angle with each pencil.

### L2 human

Here is the check for $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $a \times b = (-3, 6, -3)$:
$$a \cdot (a \times b) = -3 + 12 - 9 = 0, \qquad b \cdot (a \times b) = -12 + 30 - 18 = 0.$$
The typical use is a quick test of a computed cross product.
If one of these dot products is not $0$, there is an arithmetic error.
Watch out: perpendicularity does not fix the sign of $a \times b$, since $-(a \times b)$ is perpendicular too; the right-hand rule fixes it.

### L3 human

In the language of determinants, $c \cdot (a \times b) = \det(c, a, b)$.
This vanishes for $c = a$ or $c = b$ because a determinant with two equal rows is $0$.
So the statement is a special case of the alternating property of the determinant, treated in the sub-area on [[determinants|DTBK11SR77]].
