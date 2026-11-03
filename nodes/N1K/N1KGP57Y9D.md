---
tag: N1KGP57Y9D
kind: statement
role: theorem
name: Bott–Milnor–Kervaire theorem on division algebras
msc: [17A35, 55Q25, 57R25]
uses: [8H3JKHAAHE, 7WX14GWD4M, P9CM4GQ2T0]
about: [8H3JKHAAHE]
sources:
  - url: https://en.wikipedia.org/wiki/Division_algebra
---

## Statement

Let $A$ be a [[division algebra|8H3JKHAAHE]] over $\R$ of finite dimension $n$, not necessarily associative and not necessarily unital.
Then $n \in \set{1, 2, 4, 8}$.

## Remarks

Equivalently: if a bilinear map $\R^n \times \R^n \to \R^n$ has no zero divisors, then $n$ is $1$, $2$, $4$ or $8$.
The proof is topological.
A division algebra structure on $\R^n$ makes the [[sphere|P9CM4GQ2T0]] $S^{n-1}$ [[parallelizable|7WX14GWD4M]].
In 1958 Bott and Milnor, and independently Kervaire, showed with the Bott periodicity theorem that $S^{n-1}$ is parallelizable only for $n = 1, 2, 4, 8$.
Earlier, Hopf had shown with homology that $n$ must be a power of $2$.
All four dimensions occur: $\R$, $\C$, the quaternions and the [[octonions|1HRMT3DSX2]].
Adams later gave another proof through his theorem on maps of [[Hopf invariant one|ZJVKZ8D64P]].

## Explanations

### L1 human

Suppose you want to multiply vectors in $\R^n$ so that a product of nonzero vectors is never zero.
This is possible in dimensions $1$, $2$, $4$ and $8$, and the theorem says it is impossible in any other dimension.
The known proofs use the topology of spheres, not just algebra.

### L2 human

Compared with [[Hurwitz's theorem|WZ81H3S4KK]], the theorem asks much less: no unit, no norm, no associativity, only the absence of zero divisors.
So it is not a classification; there are many non-isomorphic division algebras in dimensions $2$, $4$ and $8$, such as the [[Okubo algebra|YYKQX7JX8K]].
The same topological methods decide which spheres are parallelizable.
