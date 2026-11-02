---
tag: GDXX60SNG5
kind: statement
role: theorem
name: Ham sandwich theorem
msc: [52A37, 55M20, 28A75]
uses: [2Z2QVWZ262, P0P21KDV6E, QHJ0GBQE2E]
sources:
  - url: https://en.wikipedia.org/wiki/Ham_sandwich_theorem
same_as:
  wikidata: Q730222
  wikipedia: Ham sandwich theorem
---

## Statement

Let $d \ge 1$ and let $\mu_1, \dots, \mu_d$ be finite Borel measures on $\R^d$ that are [[absolutely continuous|P0P21KDV6E]] with respect to [[Lebesgue measure|2Z2QVWZ262]].
Then there is an affine hyperplane $H$ of $\R^d$ such that, for each $i$, the two open half-spaces bounded by $H$ have measure $\frac{1}{2} \mu_i(\R^d)$ each.

## Remarks

The usual proof applies the [[Borsuk–Ulam theorem|QHJ0GBQE2E]].
A unit vector $u = (u_0, u_1, \dots, u_d)$ of $\R^{d+1}$ gives the half-space $H_u^+ = \set{x \in \R^d : u_0 + u_1 x_1 + \cdots + u_d x_d > 0}$.
The map $f \colon S^d \to \R^d$ with $f_i(u) = \mu_i(H_u^+) - \mu_i(H_{-u}^+)$ is continuous and odd, so it has a zero $u$.
At such a zero the hyperplane $u_0 + u_1 x_1 + \cdots + u_d x_d = 0$ bisects every $\mu_i$; the points $u = (\pm 1, 0, \dots, 0)$ are not zeros as long as the measures are nonzero.
For $d = 2$: any two bounded regions of the plane, such as two pancakes, can be cut in half at once by one straight line.
Absolute continuity is needed: for $d = 1$ and $\mu_1$ a single point mass, no point splits $\mu_1$ into two open halves of measure $\frac12$ each.

## Explanations

### L1 human

Take a sandwich made of bread, ham and cheese, placed in space in any way.
One straight cut with a knife can halve the bread, the ham and the cheese at the same time.
In the plane, two shapes can always be halved by one straight line.
In general, $d$ objects in $d$-dimensional space can be halved by one flat cut.

### L2 human

The theorem is a standard first application of the [[Borsuk–Ulam theorem|QHJ0GBQE2E]] to combinatorial geometry.
It has a discrete version for finite point sets, where the hyperplane may contain some points and each open side has at most half of each set.
It is used for partitioning point sets in computational geometry, and it is related to the [[necklace splitting problem|WFS3PHFHA1]].
