---
tag: 6HYGN2WAQQ
kind: definition
name: Blocking set
msc: ["51E21", 05B25]
defines: ZD8FVT10D8
uses: [DANFNN8C4Y, K2YVMTGTBB, CSMB49BDPT]
sources:
  - url: https://en.wikipedia.org/wiki/Blocking_set
---

## Definition

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]].
A *blocking set* of $\Pi$ is a set $B$ of points such that every line of $\Pi$ contains a point of $B$.
A blocking set is *nontrivial* if it contains no line of $\Pi$.

## Remarks

Some authors include "contains no line" in the definition of a blocking set.

Bruen's bound: a nontrivial blocking set in a plane of [[order|K2YVMTGTBB]] $n$ has at least $n + \sqrt{n} + 1$ points, with equality exactly for the point set of a Baer subplane.

Example: let $q$ be a prime power and view the [[plane $\mathrm{PG}(2, q)$|CSMB49BDPT]] as a subplane of $\mathrm{PG}(2, q^2)$.
Its $q^2 + q + 1$ points form a nontrivial blocking set of $\mathrm{PG}(2, q^2)$.
Check: each point of the subplane lies on $q^2 + 1$ lines of the large plane, of which $q + 1$ are lines of the subplane.
A line of the large plane through two points of the subplane is a line of the subplane, so the other $q^2 - q$ lines meet the subplane in one point.
This gives $(q^2 + q + 1)(q^2 - q) = q^4 - q$ such lines, and with the $q^2 + q + 1$ lines of the subplane that is $q^4 + q^2 + 1$, all lines of $\mathrm{PG}(2, q^2)$.
No line of the large plane lies inside the subplane, since it has $q^2 + 1 > q + 1$ points.

Non-example: the point set of a line $\ell$ meets every line, but it contains $\ell$, so it is a trivial blocking set.
