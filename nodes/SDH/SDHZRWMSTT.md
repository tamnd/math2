---
tag: SDHZRWMSTT
kind: statement
role: theorem
name: Shoelace formula
msc: [51M25, 51N20]
uses: [8VEFWD3EJB]
about: [8VEFWD3EJB]
sources:
  - url: https://en.wikipedia.org/wiki/Shoelace_formula
same_as:
  wikidata: Q3748369
  wikipedia: Shoelace formula
---

## Statement

Let $P$ be a simple [[polygon|8VEFWD3EJB]] in $\R^2$ with vertices $(x_1, y_1), \ldots, (x_n, y_n)$ listed in order along its boundary.
Put $(x_{n+1}, y_{n+1}) = (x_1, y_1)$.
Then the area $A$ of the region bounded by $P$ is
$$A = \frac{1}{2} \abs{\sum_{i=1}^{n} \left(x_i y_{i+1} - x_{i+1} y_i\right)}.$$

## Remarks

Without the absolute value, the sum gives the signed area, which is positive when the vertices run counterclockwise.
Each term $\frac{1}{2}(x_i y_{i+1} - x_{i+1} y_i)$ is the signed area of the triangle with vertices $0$, $P_i$, $P_{i+1}$, and these signed areas add up to the area of $P$.
Equivalently, the formula is [[Green's theorem|0HR3N02317]] applied to the line integral $\frac{1}{2}\oint (x \, dy - y \, dx)$ along the boundary.
Example: for the triangle $(0, 0), (4, 0), (0, 3)$ the sum is $0 + 12 + 0 = 12$, so $A = 6$.
Simplicity is needed: for a self-crossing figure eight the two lobes have opposite orientation, and the sum gives the difference of their areas.

## Explanations

### L1 human

The shoelace formula computes the area of a polygon from the coordinates of its corners alone.
Write the coordinates in two columns, multiply them crosswise like the laces of a shoe, and take half the difference of the two totals.

### L2 human

The formula is the standard way to compute polygon areas in computational geometry and surveying.
It is a discrete case of Green's theorem, and it is also the main tool in many proofs of [[Pick's theorem|K9SBQZMWB9]].
