---
tag: 03NK6RSRQ1
kind: statement
role: theorem
name: Vectors are perpendicular if and only if their dot product is zero
msc: ["51N20", "15A63"]
topics: [VKVAJ94SKZ]
audience: school
about: [0S52TNNTH9, 0ZEHZY85E6]
uses: [0ZEHZY85E6, 070TXS9AXM, 0S52TNNTH9, 0XKBKGTCPC]
sources:
  - url: https://en.wikipedia.org/wiki/Dot_product
    locator: Scalar projection and first properties
  - url: https://en.wikipedia.org/wiki/Perpendicular
    locator: lead section
---

## Statement

The theorem turns the geometric question "is this a right angle?" into one line of arithmetic.
Let $n$ be a positive integer, and let $u, v \in \mathbb{R}^n$, with [[dot product|0S52TNNTH9]] $u \cdot v = u_1 v_1 + \dots + u_n v_n$.
Call $u$ and $v$ perpendicular, written $u \perp v$, when $u = 0$, or $v = 0$, or the [[angle between $u$ and $v$|0ZEHZY85E6]] is $\theta = \tfrac{\pi}{2}$.
Then
$$u \perp v \iff u \cdot v = 0.$$
In particular, the zero vector is perpendicular to every vector, and it is the only vector with this property.

## Remarks

### Why each hypothesis is needed

The convention for the zero vector is needed because the zero vector has no angle with anything.
The product $0 \cdot v = 0$ holds for every $v$, so without the convention the right side of the equivalence would be true and the left side would have no meaning.

The meaning of "angle" depends on the dimension.
For $n = 2$ or $3$ it is the angle of elementary geometry, and the theorem says something about pictures.
For $n \ge 4$ it is the angle of the [[definition by the arccosine|0PRAS55318]], so the theorem there rests on the Cauchy-Schwarz inequality, through that definition.

### What it gives you

The first gift is the Pythagorean theorem in vector form.
Expanding a square of a sum gives $\|u + v\|^2 = \|u\|^2 + 2\, u \cdot v + \|v\|^2$, so
$$\|u + v\|^2 = \|u\|^2 + \|v\|^2 \iff u \perp v.$$
For $u = (3, 0)$ and $v = (0, 4)$ this reads $25 = 9 + 16$, the [[Pythagorean theorem|0VP3A1290K]] for the triangle with legs 3 and 4.

The second gift is that perpendicularity passes to combinations.
If $w \perp u$ and $w \perp v$, then $w \cdot (au + bv) = a(w \cdot u) + b(w \cdot v) = 0$, so $w$ is perpendicular to the whole plane that $u$ and $v$ span.
That is the idea behind the [[normal vector of a plane|0WQJJCCTC8]], and the [[vector projection|0JW13B48YP]] rests on the same test.

Finally, a vector perpendicular to itself is zero: $w \perp w$ gives $w \cdot w = \|w\|^2 = 0$, so $w = 0$.
This proves the last sentence of the statement.

### The converse

The statement is already an equivalence, so each direction is the converse of the other.
A nearby claim is false: $u \cdot v = 0$ and $u \cdot w = 0$ do not give $v = w$.
For $u = (1, 0)$, $v = (0, 1)$ and $w = (0, 5)$ both products are $0$, but $v \neq w$.

### Generalizations

In a real or complex [[inner product space|1D4JTZ9VS3]] one defines $u \perp v$ by $\langle u, v \rangle = 0$, so there the statement becomes a definition.
The theorem here is the reason why that definition is the right one: in the plane and in space it agrees with right angles.

## History

Perpendicularity is a basic notion of Euclid's *Elements*.
The test by the dot product is part of the vector analysis of Gibbs and Heaviside in the 1880s.

## Explanations

### L1 human

The theorem gives a quick test for a right angle.
The vectors $(2, 1)$ and $(-1, 2)$ have the dot product $-2 + 2 = 0$, so they are perpendicular.
You do not need to draw them or to measure an angle.

### L2 human

Here is a typical problem: find all vectors $(x, y)$ perpendicular to $(3, -2)$.
The condition is one linear equation:
$$(x, y) \cdot (3, -2) = 3x - 2y = 0.$$
So $y = \tfrac{3}{2} x$, and the solutions are the multiples $t(2, 3)$ of $(2, 3)$.
Check: $(2, 3) \cdot (3, -2) = 6 - 6 = 0$.
The problem shows the common pattern: the vectors perpendicular to a given vector are the solutions of a linear equation.
Watch out: in space the vectors perpendicular to one vector form a whole plane, not a line, and you need two conditions to cut them down to a line.

### L3 human

Perpendicularity is the relation $\langle u, v \rangle = 0$ of a bilinear form, and it is symmetric because the form is symmetric.
For any symmetric bilinear form one defines the orthogonal complement of a subspace, and the sub-area on [[orthogonality and least squares|8GQVME4SZZ]] uses it to split $\mathbb{R}^n$ into a subspace and its complement.
For the Minkowski form a nonzero vector can be perpendicular to itself, which is why positivity matters for that splitting.
