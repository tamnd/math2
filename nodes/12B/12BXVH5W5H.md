---
tag: 12BXVH5W5H
kind: statement
role: theorem
name: Rokhlin's theorem
msc: [57K40, 57R15, 57R20]
uses: [8H58Q6YJCH, F45VQ47GPV, RSPZ9TCFQ8, 07EZA80NEH, WK8GKRKAVD]
about: [8H58Q6YJCH]
sources:
  - url: https://en.wikipedia.org/wiki/Rokhlin%27s_theorem
same_as:
  wikidata: Q7359997
  wikipedia: Rokhlin's theorem
---

## Statement

Let $M$ be a closed, oriented, [[smooth|F45VQ47GPV]] [[4-manifold|8H58Q6YJCH]] that admits a [[spin structure|RSPZ9TCFQ8]].
Then the [[signature|07EZA80NEH]] $\sigma(M)$ of its [[intersection form|WK8GKRKAVD]] is divisible by $16$.

## Remarks

Vladimir Rokhlin proved the theorem in 1952.
One modern proof uses the Atiyah–Singer index theorem: the index of the Dirac operator of $M$ equals $-\sigma(M)/8$.
In dimension $4$ the spinor bundles are quaternionic, so the kernel and cokernel of the Dirac operator are quaternionic vector spaces and the index is even.
Hence $\sigma(M)/8$ is even.
The K3 surface is a spin $4$-manifold of signature $-16$, so $16$ cannot be replaced by a larger number.
Without smoothness the theorem fails: the [[$E_8$ manifold|BNDRN0G9BR]] is a closed topological $4$-manifold with even form and signature $8$.
Without the spin condition it fails: the complex projective plane has signature $1$.
Algebra alone gives less: an even unimodular form always has signature divisible by $8$.
For a simply connected $M$, being spin is the same as having an even intersection form.

## Explanations

### L1 human

The signature is a single integer that measures the crossings of surfaces in a four-dimensional space.
Rokhlin's theorem says that for smooth spaces of a special kind, called spin, this integer is always a multiple of $16$.
Algebra only predicts a multiple of $8$, and the gap of a factor $2$ is a purely smooth phenomenon.

### L2 human

The theorem is the first sign that smooth $4$-manifolds are more rigid than topological ones.
It shows that the $E_8$ manifold has no smooth structure.
It defines the Rokhlin invariant of an integral homology $3$-sphere: the signature of a smooth spin $4$-manifold it bounds, divided by $8$, modulo $2$.
The [[11/8 conjecture|90RA6TAT7H]] and Furuta's $10/8$ theorem refine it for spin $4$-manifolds.
