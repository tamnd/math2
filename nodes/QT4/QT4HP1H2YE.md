---
tag: QT4HP1H2YE
kind: definition
name: Seifert surface
msc: [57K10]
defines: K866ND3WF7
uses: [QYEAZTYGPT, 1A5WRCNTM3, VGJJVBZ1MQ, 702SNFQG0W, NJ787GZS1N]
sources:
  - url: https://en.wikipedia.org/wiki/Seifert_surface
---

## Definition

Let $L \subset S^3$ be an oriented tame [[link|1A5WRCNTM3]], for example an oriented [[knot|QYEAZTYGPT]].
A *Seifert surface* for $L$ is a subset $\Sigma \subset S^3$ such that:

1. $\Sigma$ is a compact connected [[surface|VGJJVBZ1MQ]] with boundary, embedded in $S^3$ in a tame way;
2. $\Sigma$ is [[orientable|702SNFQG0W]];
3. the boundary of $\Sigma$ is $L$, and the orientation of $L$ is the boundary orientation induced by an orientation of $\Sigma$.

## Remarks

The *genus* $g(K)$ of a knot $K$ is the least [[genus|NJ787GZS1N]] of a Seifert surface for $K$.
Example: the unknot $\set{(x, y, 0) : x^2 + y^2 = 1}$ in $\R^3 \subset S^3$ bounds the flat disk $\set{(x, y, 0) : x^2 + y^2 \le 1}$, which is compact, connected, orientable and has the unknot as boundary; so the unknot has genus $0$.
Conversely, a knot of genus $0$ bounds a disk and is the unknot.
Non-example: a band with one half-twist, a Möbius band, has the unknot as boundary, but it is not orientable, so it is not a Seifert surface.
A band with three half-twists is a Möbius band whose boundary is the trefoil, so it fails for the same reason; the trefoil has genus $1$ instead.
Seifert's algorithm builds a Seifert surface from any diagram.
One smooths each crossing according to the orientation, fills the resulting circles with disks, and joins the disks by twisted bands at the crossings.
