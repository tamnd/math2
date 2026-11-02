---
tag: SPFP3GHVYJ
kind: statement
role: theorem
name: Segre's theorem
msc: ["51E21", "51E15"]
uses: [7B03TB64N9, R3TMVHTP3A, CSMB49BDPT, 0ZXZ82FTX2]
about: [7B03TB64N9, R3TMVHTP3A]
sources:
  - url: https://en.wikipedia.org/wiki/Segre%27s_theorem
same_as:
  wikidata: Q23021008
  wikipedia: Segre's theorem
---

## Statement

Let $q$ be an odd prime power, let $\F_q$ be the [[finite field|0ZXZ82FTX2]] with $q$ elements, and let $\mathrm{PG}(2, q)$ be the [[projective plane over $\F_q$|CSMB49BDPT]].
An [[oval|7B03TB64N9]] of $\mathrm{PG}(2, q)$ is a set of $q + 1$ points with no three on a common line.
Then every oval of $\mathrm{PG}(2, q)$ is a non-degenerate [[conic|R3TMVHTP3A]].

## Remarks

The theorem was proved by Beniamino Segre.
The key step is the "lemma of tangents" for an oval in $\mathrm{PG}(2, q)$ with $q$ odd.
It says that any triangle of points of the oval and the triangle of tangent lines at these points are in perspective.
Its proof uses that the product of all nonzero elements of $\F_q$ is $-1$.
From this one shows that the oval agrees with the conic through five of its points.

The hypothesis that $q$ is odd is necessary.
Let $q = 2^h$ with $h \ge 3$, let $C$ be a conic and let $N$ be its nucleus, the common point of all its tangent lines.
Removing a point $P \ne N$ of $C$ from $C \cup \set{N}$ gives an oval.
It is not a conic: it shares $q \ge 8$ points with $C$, while two distinct conics share at most $4$ points.

## Explanations

### L1 human

In a finite plane over a field with an odd number of elements, take $q + 1$ points with no three on a line.
This is the largest such set possible, and conics are one way to get it.
Segre's theorem says that conics are the only way.
So a purely combinatorial condition forces an algebraic shape, a curve of degree two.

### L2 human

Segre's theorem is the starting point of Galois geometry, the study of point sets in projective spaces over finite fields.
It shows that in $\mathrm{PG}(2, q)$ with $q$ odd the ovals have a single type up to projective equivalence.
In even characteristic the picture is different: every oval extends to a hyperoval of $q + 2$ points, and many non-conic examples exist.
The same circle of ideas classifies ovoids of $\mathrm{PG}(3, q)$ for $q$ odd as elliptic quadrics.
