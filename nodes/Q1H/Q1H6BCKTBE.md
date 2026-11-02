---
tag: Q1H6BCKTBE
kind: statement
role: theorem
name: Kissing number problem in three dimensions
msc: [52C17, 05B40]
uses: [B408FZYXF9]
about: [B408FZYXF9]
sources:
  - url: https://en.wikipedia.org/wiki/Kissing_number
---

## Statement

The [[kissing number|B408FZYXF9]] in dimension $3$ is $\tau(3) = 12$.
That is, at most $12$ unit balls in $\R^3$ with pairwise disjoint interiors can touch a given unit ball, and $12$ is attained.

## Remarks

The lower bound comes from the face-centred cubic packing: the $12$ vectors $(\pm 1, \pm 1, 0)$, $(\pm 1, 0, \pm 1)$, $(0, \pm 1, \pm 1)$, scaled to norm $2$, are pairwise at distance at least $2$.
The configuration of the $12$ vertices of a regular icosahedron also works, and in it no two outer balls touch, so they can move.
The question goes back to a discussion between Isaac Newton, who held that the answer is $12$, and David Gregory, who thought $13$ might fit.
Kurt Schütte and B. L. van der Waerden gave the first complete proof in 1953.
Later proofs bound the number of points on the sphere with pairwise angular distance at least $60^\circ$, for example with a refined form of the [[Delsarte linear programming bound|7RPEDHAT7R]].

## Explanations

### L1 human

Hold one ball and try to make as many equal balls as possible touch it.
Twelve fit, with some space left over, so it seems a thirteenth might squeeze in after shuffling.
The theorem says it never does.

### L2 human

The plain linear programming bound gives only $\tau(3) \le 13$, so the three-dimensional case needs extra geometric arguments.
In dimensions $8$ and $24$ the same linear programming method is exactly sharp and gives $240$ and $196560$.
Dimension $4$ was settled by Oleg Musin, who showed $\tau(4) = 24$.
