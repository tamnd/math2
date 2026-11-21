---
tag: N95H8HNXVH
kind: example
name: Disc, circle and exterior do not form a cylindrical decomposition
aliases: [disc-circle-exterior-not-cylindrical]
msc: ["14P10", "03C10"]
topics: [1A9JSC5YG8]
audience: grad
not_instance_of:
  - target: GE8FCGKPTR
    note: the open disc projects onto the interval from minus one to one and the exterior onto the whole line, which overlap without being equal, and the circle and the exterior are not cells
uses: [08J2M1JYAG, BX5WSK8ZCT, 0QT00PB5G2, 57NRC0SCCX]
sources:
  - url: https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition
---

## Example

Let $f(x, y) = x^2 + y^2 - 1$.
Consider the partition of $\R^2$ into three [[semialgebraic sets|BX5WSK8ZCT]]: the open disc $D = \set{f < 0}$, the circle $S = \set{f = 0}$ and the exterior $E = \set{f > 0}$.
It is adapted to $f$, since $f$ has constant sign on each piece, but it is not a cylindrical algebraic decomposition.

1. Projections. In a CAD of $\R^2$, the projections of two cells to the $x$-axis are cells of a CAD of $\R$, so they are equal or disjoint. Here $D$ projects onto $(-1, 1)$ and $E$ projects onto $\R$, which overlap and are not equal.
2. Cells. Each cell of a CAD is [[homeomorphic|0QT00PB5G2]] to an open cube $(0, 1)^d$. The circle $S$ is compact and nonempty, so it is not homeomorphic to $(0, 1)$ or to a point. The exterior $E$ contains loops around the disc that cannot be contracted in $E$, so it is not homeomorphic to $(0, 1)^2$.
3. Stacks. Over the point $x = 0$, the vertical line meets $E$ in two pieces, $y < -1$ and $y > 1$. In a CAD, each cell meets a vertical line over its base in one connected set.

So the decomposition fails cylindricity, and two of its pieces are not cells.

## Remarks

The example shows that sign invariance alone is not the point of a CAD: the decomposition $\set{D, S, E}$ has the fewest pieces adapted to $f$, but it cannot be used to eliminate quantifiers by walking down stacks.
Refining it along the vertical lines $x = \pm 1$ and the horizontal order gives [[the 13-cell CAD of the circle|57NRC0SCCX]].

When the curve changes, the result can change.
For the line $f = y$, the three pieces $\set{y < 0}$, $\set{y = 0}$, $\set{y > 0}$ already form a CAD over the one-cell CAD of $\R$.

## Explanations

### L1 human

The circle cuts the plane into the inside, the circle itself and the outside.
These three pieces are not "stacked" in vertical columns: the outside surrounds the disc, and seen from above it covers the whole $x$-axis while the disc covers only part of it.
A cylindrical decomposition needs pieces that sit in columns, one above the other.

### L2 human

We test the stack condition on the vertical line $x = 0$.

1. On the line $x = 0$, the value is $f(0, y) = y^2 - 1$.
2. It is positive for $y < -1$ and for $y > 1$, zero at $y = \pm 1$, and negative for $-1 < y < 1$.
3. So the line meets $E$ in two separate pieces and $S$ in two points.
4. In a CAD each cell over a base cell is a graph or a band, which meets each vertical line in one point or one interval.

So $E$ and $S$ would each have to split into two cells.
The typical use of this non-example is to remember that a CAD is about columns, not only about signs.
A trap is to think that the components of the sign conditions already form a CAD.
