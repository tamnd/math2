---
tag: JXRXV92WN5
kind: definition
name: Oval
msc: ["51E21", "51E15"]
defines: 7B03TB64N9
uses: [DANFNN8C4Y, R3TMVHTP3A, K2YVMTGTBB]
sources:
  - url: https://en.wikipedia.org/wiki/Oval_(projective_plane)
---

## Definition

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]].
A line is a *tangent* of a set $O$ of points at $P \in O$ if it meets $O$ only in $P$.
A set $O$ of points of $\Pi$ is an *oval* if:

1. every line of $\Pi$ meets $O$ in at most two points;
2. for every point $P \in O$ there is exactly one tangent of $O$ at $P$.

## Remarks

If $\Pi$ is finite of [[order|K2YVMTGTBB]] $n$, a set $O$ is an oval if and only if $O$ has $n + 1$ points and no three of them on a line.
Indeed, suppose $O$ has no three points on a line, and let $P \in O$.
Of the $n + 1$ lines through $P$, exactly $\abs{O} - 1$ meet $O$ again.
So $P$ has $n + 2 - \abs{O}$ tangents, and this equals $1$ exactly when $\abs{O} = n + 1$.

Example: in $PG(2, q)$ the non-degenerate [[conic|R3TMVHTP3A]] $xz = y^2$ has the $q + 1$ points $[1 : t : t^2]$, $t \in \F_q$, and $[0 : 0 : 1]$.
A line $ax + by + cz = 0$, with $(a, b, c) \ne 0$, meets it in the points $[1 : t : t^2]$ with $a + bt + ct^2 = 0$, and in $[0 : 0 : 1]$ exactly when $c = 0$.
If $c \ne 0$, the polynomial has at most two roots.
If $c = 0$, it has at most one root, and the line also contains $[0 : 0 : 1]$.
In both cases the line meets the conic in at most two points.
So the conic is a set of $q + 1$ points with no three on a line, hence an oval.

Non-example: three non-collinear points $A, B, C$ in $PG(2, 3)$.
No line contains all three, so clause 1 holds.
Through $A$ there are $4$ lines, and only $AB$ and $AC$ meet the set again.
So $A$ has two tangents, and clause 2 fails.
