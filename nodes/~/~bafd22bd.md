---
tag: ~bafd22bd
kind: statement
role: theorem
name: Length of the cross product and the area of a parallelogram
msc: ["15A72", "51N20"]
topics: [VKVAJ94SKZ]
audience: school
about: [0N5N15HWZ7]
uses: [0N5N15HWZ7, 0ZEHZY85E6, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Cross_product
    locator: Geometric meaning
---

## Statement

Let $a, b \in \mathbb{R}^3$ be nonzero vectors, and let $\theta \in [0, \pi]$ be the [[angle|0ZEHZY85E6]] between them.
Then the [[length|0XKBKGTCPC]] of the cross product is
$$\|a \times b\| = \|a\| \, \|b\| \sin \theta.$$
This number is the area of the parallelogram with the sides $a$ and $b$, drawn from one point.
Also, for all $a, b \in \mathbb{R}^3$ (zero or not), $a \times b = 0$ if and only if $a$ and $b$ are parallel, that is, one of them is a multiple of the other.

## Remarks

### Why each hypothesis is needed

- The vectors must be nonzero for the angle to exist. For $a = 0$ the product is $0$, and the parallelogram is a segment or a point of area $0$.
- The angle must be taken in $[0, \pi]$. There $\sin \theta \geq 0$, so the right side is not negative, like a length.

### Consequences

- The area of the triangle with vertices $P$, $Q$ and $R$ is $\tfrac{1}{2} \|(Q - P) \times (R - P)\|$.
- The cross product is largest, for given lengths, when $a \perp b$; then $\|a \times b\| = \|a\| \, \|b\|$.
- Two nonzero vectors are parallel if and only if their cross product is $0$; this is a quick test for collinearity of three points.
- The distance from a point $P$ to the line through $A$ with direction $d$ is $\dfrac{\|(P - A) \times d\|}{\|d\|}$, the height of a parallelogram; see the row on [[distances|~1297517b]].

### Converse

If a vector $n$ is perpendicular to $a$ and $b$, has the length $\|a\| \, \|b\| \sin \theta$, and makes $(a, b, n)$ right-handed, then $n = a \times b$, for $a$ and $b$ not parallel.
Without the orientation condition, both $a \times b$ and $-(a \times b)$ qualify.

### Generalizations

For $a, b \in \mathbb{R}^n$, the area of the parallelogram is $\sqrt{\|a\|^2 \|b\|^2 - (a \cdot b)^2} = \|a\| \, \|b\| \sin \theta$ in every dimension, by Lagrange's identity in $\mathbb{R}^n$.
The volume of the parallelepiped spanned by three vectors is the absolute value of the [[scalar triple product|~d7839aac]].

## History

The interpretation of the length as an area belongs to the vector analysis of Gibbs and Heaviside in the 1880s.

## Explanations

### L1 human

Two arrows from one point span a parallelogram.
The cross product of the arrows is a new arrow whose length is the area of that parallelogram.
For $(2, 0, 0)$ and $(0, 3, 0)$ the parallelogram is a $2$ by $3$ rectangle with area $6$.
The cross product is $(0, 0, 6)$, and its length is $6$.

### L2 human

Worked example: the area of the parallelogram spanned by $a = (1, 1, 0)$ and $b = (1, 0, 1)$.

1. $a \times b = (1 \cdot 1 - 0 \cdot 0, \; 0 \cdot 1 - 1 \cdot 1, \; 1 \cdot 0 - 1 \cdot 1) = (1, -1, -1)$.
2. The area is $\|a \times b\| = \sqrt{3}$.
3. Check by the angle: $\|a\| = \|b\| = \sqrt{2}$ and $\theta = 60^\circ$, so $\|a\| \, \|b\| \sin \theta = 2 \cdot \tfrac{\sqrt{3}}{2} = \sqrt{3}$.

The typical use is the area of a triangle or a parallelogram in space from the coordinates of its vertices.
A trap: the triangle has half the area of the parallelogram, so do not forget the factor $\tfrac{1}{2}$.

### L3 human

The length of $a \times b$ is the $2$-dimensional volume of the parallelogram, which is $\sqrt{\det G}$ for the Gram matrix $G$ of $a$ and $b$.
The same formula gives the $k$-dimensional volume of a parallelotope in $\mathbb{R}^n$, and it is the base of the surface area formula $\iint \|r_u \times r_v\| \, du \, dv$ of calculus.
The link between determinants and volume is the topic of the [[determinant as signed volume|04X3PR72VJ]].
