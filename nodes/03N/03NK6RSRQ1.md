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

Let $n$ be a positive integer, and let $u, v \in \mathbb{R}^n$, with [[dot product|0S52TNNTH9]] $u \cdot v = u_1 v_1 + \dots + u_n v_n$.
Call $u$ and $v$ perpendicular, written $u \perp v$, when $u = 0$, or $v = 0$, or the [[angle between $u$ and $v$|0ZEHZY85E6]] is $\theta = \tfrac{\pi}{2}$.
Then
$$u \perp v \iff u \cdot v = 0.$$
In particular, the zero vector is perpendicular to every vector, and it is the only vector with this property.

## Remarks

### Why each hypothesis is needed

- The convention for the zero vector is needed. Without it, $0 \cdot v = 0$ holds, but the angle between $0$ and $v$ is not defined, so "$\theta = \tfrac{\pi}{2}$" would be meaningless.
- For $n \geq 4$ the angle is the one of the [[definition by the arccosine|0PRAS55318]]. So the statement for $n \geq 4$ depends on the Cauchy-Schwarz inequality through that definition.

### Consequences

- The [[Pythagorean theorem|0VP3A1290K]] in vector form: $\|u + v\|^2 = \|u\|^2 + \|v\|^2$ if and only if $u \perp v$, because $\|u + v\|^2 = \|u\|^2 + 2\, u \cdot v + \|v\|^2$.
- A vector $w$ perpendicular to both $u$ and $v$ is perpendicular to each linear combination $au + bv$, since $w \cdot (au + bv) = a(w \cdot u) + b(w \cdot v)$.
- If $w \perp w$, then $w \cdot w = \|w\|^2 = 0$, so $w = 0$. This proves the last sentence of the statement.
- The [[vector projection|0JW13B48YP]] and the [[normal vector of a plane|0WQJJCCTC8]] rest on this test.

### Converse

The statement is already an equivalence.
A related claim is false: $u \cdot v = 0$ and $u \cdot w = 0$ do not give $v = w$; for $u = (1, 0)$, $v = (0, 1)$ and $w = (0, 5)$ both products are $0$.

### Generalizations

In a real or complex [[inner product space|1D4JTZ9VS3]], one defines $u \perp v$ by $\langle u, v \rangle = 0$, so the statement becomes a definition there.
The theorem above is the reason why this definition is the right one.

## History

Perpendicularity is a basic notion of Euclid's Elements.
The test by the dot product is part of the vector analysis of Gibbs and Heaviside in the 1880s.

## Explanations

### L1 human

This gives a quick test for a right angle.
The vectors $(2, 1)$ and $(-1, 2)$ have the dot product $-2 + 2 = 0$, so they are perpendicular.
We do not need to draw them or to measure an angle.

### L2 human

Worked example: find all vectors $(x, y)$ perpendicular to $(3, -2)$.

1. The condition is $(x, y) \cdot (3, -2) = 3x - 2y = 0$.
2. So $y = \tfrac{3}{2} x$, and the solutions are the multiples $t(2, 3)$ of $(2, 3)$.
3. Check: $(2, 3) \cdot (3, -2) = 6 - 6 = 0$.

The typical use is to find a vector perpendicular to given vectors, as in step 2, or to test a right angle in a figure.
A trap: in space, the vectors perpendicular to one vector form a whole plane, not one line.

### L3 human

Perpendicularity is the relation $\langle u, v \rangle = 0$ of a bilinear form, and it is symmetric because the form is symmetric.
For any symmetric bilinear form one defines the orthogonal complement of a subspace, and the sub-area on [[orthogonality and least squares|8GQVME4SZZ]] uses it to split $\mathbb{R}^n$ into a subspace and its complement.
For the Minkowski form, a nonzero vector can be perpendicular to itself, and this is the reason why positivity matters.
