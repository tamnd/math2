---
tag: A66VNJ7BED
kind: definition
name: Arc in a finite plane
msc: ["51E21", "51E15"]
defines: 6FFVXT5KMH
uses: [DANFNN8C4Y, K2YVMTGTBB, CSMB49BDPT]
sources:
  - url: https://en.wikipedia.org/wiki/Arc_(projective_geometry)
---

## Definition

Let $\Pi$ be a finite [[projective plane|DANFNN8C4Y]] and let $k \ge 1$ be an integer.
A *$k$-arc* of $\Pi$ is a set of $k$ points of $\Pi$ such that no three of them lie on a common line.

## Remarks

Let $\Pi$ have [[order|K2YVMTGTBB]] $n$, so each point lies on $n + 1$ lines.
If $P$ is a point of a $k$-arc $K$, the lines joining $P$ to the other $k - 1$ points of $K$ are distinct.
Hence $k - 1 \le n + 1$, that is, $k \le n + 2$.
When $n$ is odd, $k \le n + 1$.
An arc with $n + 1$ points is called an oval, and one with $n + 2$ points a hyperoval.

Example: in the [[plane $\mathrm{PG}(2, q)$|CSMB49BDPT]], let $K$ consist of the points $(1 : t : t^2)$ for $t \in \F_q$ and the point $(0 : 0 : 1)$.
Three points $(1 : s : s^2)$, $(1 : t : t^2)$, $(1 : u : u^2)$ with distinct $s, t, u$ are not collinear, because their Vandermonde determinant $(t - s)(u - s)(u - t)$ is nonzero.
For $(1 : s : s^2)$, $(1 : t : t^2)$ and $(0 : 0 : 1)$ the determinant is $t - s \ne 0$.
So $K$ is a $(q + 1)$-arc.

Non-example: the $n + 1$ points of a line, for $n \ge 2$, contain three collinear points, so they do not form an arc.

More generally, a $(k, d)$-arc is a set of $k$ points with at most $d$ on any line, so that a $k$-arc is a $(k, 2)$-arc.
