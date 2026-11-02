---
tag: 212QCPWWA9
kind: definition
name: Crossing number
msc: [57K10]
defines: SWJZ4QRF9W
uses: [QYEAZTYGPT, GZQ5ZE3X6G]
sources:
  - url: https://en.wikipedia.org/wiki/Crossing_number_(knot_theory)
---

## Definition

Let $K$ be a tame [[knot|QYEAZTYGPT]] in $\R^3$.
A *diagram* of $K$ is a projection of $K$ to a plane that is injective except at finitely many transverse double points, called *crossings*.
At each crossing the diagram records which strand passes over.
The *crossing number* $c(K)$ is the least number of crossings of a diagram of a knot equivalent to $K$.

## Remarks

Since the minimum is taken over all knots equivalent to $K$, the number $c(K)$ is a [[knot invariant|GZQ5ZE3X6G]].
Example: $c(\text{unknot}) = 0$, since the round circle has a diagram with no crossings.
For the trefoil, $c = 3$: it has a diagram with $3$ crossings, and every diagram with at most $2$ crossings represents the unknot, which is not equivalent to the trefoil.
Non-example: a diagram of the unknot with one twist has $1$ crossing, but $1$ is not the crossing number of the unknot, because the minimum is $0$.
For a reduced alternating diagram, the number of crossings equals the crossing number; this was one of the Tait conjectures, proved with the Jones polynomial.
The same definition applies to links.
