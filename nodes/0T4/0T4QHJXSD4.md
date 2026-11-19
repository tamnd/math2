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

Let $a$ and $b$ be vectors in $\mathbb{R}^3$, and let $a \times b$ be their [[cross product|0N5N15HWZ7]].
Let $u \cdot v = u_1 v_1 + u_2 v_2 + u_3 v_3$ be the [[dot product|0S52TNNTH9]].
Then
$$a \cdot (a \times b) = 0 \quad \text{and} \quad b \cdot (a \times b) = 0.$$
So $a \times b$ is [[perpendicular|03NK6RSRQ1]] to $a$ and to $b$.

## Remarks

### Why each hypothesis is needed

The statement holds for all $a, b \in \mathbb{R}^3$, including the zero vector and parallel vectors; in these cases $a \times b = 0$, and the zero vector is perpendicular to every vector.

### Consequences

- If $a$ and $b$ are not parallel, then $a \times b$ is a normal vector of the plane through $0$ spanned by $a$ and $b$, as the row on the [[equation of a plane|07SDJ5DNE4]] uses.
- $a \times b$ is perpendicular to each linear combination $sa + tb$, by the linearity of the dot product.
- The scalar triple products $a \cdot (a \times b)$ and $b \cdot (a \times b)$ are $0$, which matches the fact that the [[scalar triple product|34VJYG6GVD]] of three coplanar vectors is $0$.

### Converse

If $a$ and $b$ are not parallel, then every vector perpendicular to both is a multiple of $a \times b$.
The reason: such vectors solve two independent linear equations in three unknowns, so they form a line, and $a \times b \neq 0$ lies on it.
If $a$ and $b$ are parallel, the perpendicular vectors form a plane, and $a \times b = 0$ does not span it.

### Generalizations

In $\mathbb{R}^n$, a vector perpendicular to $n - 1$ given vectors comes from the formal determinant with the first row $e_1, \dots, e_n$; this generalized cross product takes $n - 1$ factors.
In $\mathbb{R}^7$ there is also a product of two vectors that is perpendicular to both factors.

## Explanations

### L1 human

Lay two pencils flat on a table, starting at the same point.
Their cross product points straight up from the table, or straight down.
So it makes a right angle with each pencil.

### L2 human

Check with $a = (1, 2, 3)$, $b = (4, 5, 6)$ and $a \times b = (-3, 6, -3)$.

1. $a \cdot (a \times b) = -3 + 12 - 9 = 0$.
2. $b \cdot (a \times b) = -12 + 30 - 18 = 0$.

The typical use is a quick check of a computed cross product: if one of these dot products is not $0$, there is an arithmetic error.
A trap: perpendicularity does not fix the sign of $a \times b$; the right-hand rule does.

### L3 human

In the language of determinants, $c \cdot (a \times b) = \det(c, a, b)$, and this vanishes for $c = a$ or $c = b$ because a determinant with two equal rows is $0$.
So the statement is a special case of the alternating property of the determinant, treated in the sub-area on [[determinants|DTBK11SR77]].
