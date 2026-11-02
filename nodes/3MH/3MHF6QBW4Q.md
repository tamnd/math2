---
tag: 3MHF6QBW4Q
kind: statement
role: proposition
name: Number of points of a finite projective plane
msc: ["51E15", "05B25"]
uses: [DANFNN8C4Y, K2YVMTGTBB, 2HWB7P1DZN, QQ8GW1ASZM, 7BPSC4T4M3]
about: [K2YVMTGTBB, 2HWB7P1DZN]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_plane
    locator: Finite projective planes
---

## Statement

Let $\Pi$ be a finite [[projective plane|DANFNN8C4Y]] of [[order|K2YVMTGTBB]] $n$.
Then every point of $\Pi$ lies on exactly $n + 1$ lines, and $\Pi$ has exactly $n^2 + n + 1$ points and exactly $n^2 + n + 1$ lines.

## Remarks

Fix a point $P$.
It lies on $n + 1$ lines, and each of them has $n$ points other than $P$.
Every other point $Q$ lies on exactly one line through $P$, namely $PQ$, so the number of points is $1 + (n + 1) n = n^2 + n + 1$.
The count of lines follows by the same argument in the dual plane, which is again a projective plane of order $n$.

Example: the [[Fano plane|QQ8GW1ASZM]] has order $2$ and $4 + 2 + 1 = 7$ points.
The plane $PG(2, q)$ has $(q^3 - 1)/(q - 1) = q^2 + q + 1$ points, as it should.
In Mathlib the count of points is `Configuration.ProjectivePlane.card_points`.

## Explanations

### L1 human

Once one knows how many points lie on a line of a finite projective plane, one knows the size of the whole plane.
With $n + 1$ points on each line, there are $n^2 + n + 1$ points and the same number of lines.
For order $2$ this gives the $7$ points of the Fano plane, and for order $3$ it gives $13$.

### L2 human

The proof is a standard double count from a single point, and the same method gives the counts of flags and of triangles.
It shows that a projective plane of order $n$ is a symmetric block design with parameters $(n^2 + n + 1, n + 1, 1)$, a [[Steiner system|7BPSC4T4M3]] $S(2, n + 1, n^2 + n + 1)$.
This turns existence questions for planes into questions about designs, which is the setting of the Bruck–Ryser–Chowla theorem.
