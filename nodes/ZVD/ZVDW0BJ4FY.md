---
tag: ZVDW0BJ4FY
kind: definition
name: Bilinear interpolation
msc: [65D05, 41A05]
defines: 5QJYCNRYMQ
uses: [SS1YMS2NPC, BM703GV34G]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_interpolation
---

## Definition

Let $x_1 < x_2$ and $y_1 < y_2$ be real numbers, let $R = [x_1, x_2] \times [y_1, y_2]$, and let $f_{ij} \in \R$ be given values at the corners $(x_i, y_j)$ for $i, j \in \set{1, 2}$.
The *bilinear interpolant* is the unique function $p \colon R \to \R$ of the form $p(x, y) = a + b x + c y + d x y$ with $p(x_i, y_j) = f_{ij}$ for all $i, j$.
In terms of $s = (x - x_1)/(x_2 - x_1)$ and $t = (y - y_1)/(y_2 - y_1)$, it is
$$p(x, y) = (1 - s)(1 - t) f_{11} + s (1 - t) f_{21} + (1 - s) t f_{12} + s t f_{22}.$$
For data on a rectangular grid, *bilinear interpolation* uses this formula on each grid cell.

## Remarks

The formula has the required form and takes the value $f_{ij}$ at each corner, which shows existence.
Uniqueness holds because a function $a + bx + cy + dxy$ vanishing at the four corners has $a = b = c = d = 0$, as one checks on the unit square.
Example: for $f(x, y) = 2 + 3x - y + xy$, the bilinear interpolant on any rectangle is $f$ itself, since $f$ already has the required form.
Non-example: $p(x, y) = x^2$ on the unit square has corner values $0, 1, 0, 1$, but it is not of the form $a + bx + cy + dxy$, so it is not the bilinear interpolant; that interpolant is $x$.
The interpolant is linear along every horizontal and vertical line, but not linear in general: along the diagonal $x = y$ of the unit square, $xy$ restricts to $x^2$.
On a grid, the cellwise interpolants agree on shared edges, so the result is continuous, but its gradient jumps across cell edges in general.

## Explanations

### L1 human

Bilinear interpolation fills in a rectangle from its four corner values by mixing them with weights given by the areas of the opposite sub-rectangles.
It is linear in each variable separately, which is where the name comes from.
