---
tag: 0XYP2KKSPC
kind: definition
name: Normal vector
aliases: [normal]
msc: [51N20]
defines: 0WQJJCCTC8
uses: [0V3XAMF3C1, 0MP9BCF6DP, 03NK6RSRQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_(geometry)
    locator: Normal to planes and polygons
---

## Definition

Let $H$ be a [[line|0MP9BCF6DP]] in $\mathbb{R}^2$ or a [[plane|0V3XAMF3C1]] in $\mathbb{R}^3$. Let $\cdot$ be the dot product.
A normal vector of $H$ is a nonzero vector $n$ such that $n \cdot (x - y) = 0$ for all points $x$ and $y$ of $H$.

## Remarks

If $n$ is a normal vector of $H$, then the normal vectors of $H$ are exactly the vectors $c n$ with $c \neq 0$.
The plane $\{(x, y, z) : a x + b y + c z = d\}$ with $(a, b, c) \neq (0, 0, 0)$ has the normal vector $(a, b, c)$. The line $\{(x, y) : a x + b y = c\}$ with $(a, b) \neq (0, 0)$ has the normal vector $(a, b)$.
For the plane $\{p + s u + t v : s, t \in \mathbb{R}\}$, the [[cross product|0N5N15HWZ7]] $u \times v$ is a normal vector.
A unit normal vector is a normal vector of length 1.

## Explanations

### L1 human

A normal vector sticks straight out of a flat object. Think of a pencil standing upright on a table: it is normal to the table. Each arrow that lies in the table makes a right angle with the pencil, so its dot product with the pencil is $0$.
