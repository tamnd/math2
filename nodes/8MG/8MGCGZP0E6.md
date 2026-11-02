---
tag: 8MGCGZP0E6
kind: definition
name: Hyperoval
msc: ["51E21", "51E15"]
defines: RNG2A8BFVZ
uses: [DANFNN8C4Y, K2YVMTGTBB, 7B03TB64N9, QQ8GW1ASZM]
sources:
  - url: https://en.wikipedia.org/wiki/Oval_(projective_plane)
---

## Definition

Let $\Pi$ be a finite [[projective plane|DANFNN8C4Y]] of [[order|K2YVMTGTBB]] $n$.
A *hyperoval* of $\Pi$ is a set of $n + 2$ points of $\Pi$ such that no three of them lie on a line.

## Remarks

Every line meets a hyperoval $H$ in $0$ or $2$ points.
Suppose a line met $H$ in exactly one point $P$.
The other $n$ lines through $P$ would then cover the remaining $n + 1$ points of $H$, each at most one of them, which is impossible.

Example: in the [[Fano plane|QQ8GW1ASZM]], of order $2$, let $H$ be the four points off a fixed line $\ell$.
Any other line meets $\ell$ in one point, so it has exactly $2$ points in $H$; hence no three points of $H$ are collinear, and $\abs{H} = 4 = 2 + 2$.

Non-example: $PG(2, 3)$ has no hyperoval.
More generally, a plane of odd order $n$ has none.
Suppose $S$ were a hyperoval, and take a point $P$ outside $S$.
Every line through $P$ meets $S$ in $0$ or $2$ points, so these lines split $S$ into pairs.
Then $\abs{S}$ is even, while $n + 2$ is odd.

For $n$ even, the tangents of an [[oval|7B03TB64N9]] all pass through one point, its nucleus, and adding the nucleus gives a hyperoval.
