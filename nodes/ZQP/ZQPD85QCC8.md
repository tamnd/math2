---
tag: ZQPD85QCC8
kind: statement
role: theorem
name: The center of the endomorphism algebra consists of the scalar maps
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug2
about: [5JA4CYT1TB, MVT64B3B6H]
uses: [7BDGQ1Q46E, CQSZTPMSEP]
sources:
  - url: https://en.wikipedia.org/wiki/Center_(ring_theory)
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Center_(ring_theory)
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Statement

The only endomorphisms that commute with every endomorphism are the multiples of the identity.

Let $F$ be a field and let $V$ be a vector space over $F$, of any dimension.
Then the [[center|CQSZTPMSEP]] of the [[algebra of endomorphisms|5JA4CYT1TB]] $\End(V)$ is the set of scalar maps,
$$Z(\End(V)) = \{a\, \id_V : a \in F\}.$$
So an endomorphism $T$ satisfies $TS = ST$ for every $S \in \End(V)$ if and only if $T = a \id_V$ for some $a \in F$.
If $V \ne \{0\}$, the map $a \mapsto a \id_V$ is an isomorphism of $F$ onto the center.

## Remarks

### Why the hypotheses are needed

The theorem quantifies over all $S \in \End(V)$.
A single endomorphism $T$ commutes with many maps that are not scalar, since every polynomial in $T$ commutes with $T$.
The scalars must commute with each other.
Over a noncommutative division ring, the map $v \mapsto av$ is not linear in general, since $a(bv) \ne b(av)$ can happen.
For $V = \{0\}$, the algebra is $\{0\}$, and the statement still holds, but $a \mapsto a \id_V$ is no longer injective.

### What it gives you

For $\dim V = n$, the center of the [[matrix ring|AB2MD5CD13]] $M_n(F)$ is the set of [[scalar matrices|067NKSBEWT]] $aI$, which is the [[matrix form of the theorem|DVZ1V4A884]].
For $\dim V \ge 2$, the algebra $\End(V)$ is not commutative, since its center is a proper subspace.

### The converse

The scalar maps lie in the center for every $V$, since $(a\id)S = aS = S(a\id)$ by homogeneity of $S$.
This is the easy direction of the theorem.

### Generalizations

For a commutative ring $R$, the center of the matrix ring $M_n(R)$ consists of the scalar matrices $rI$ with $r \in R$.
For a module $M$ over a commutative ring $R$, the maps $r \id_M$ always lie in the center of $\End_R(M)$.

## History

The letter $Z$ for the center comes from the German word *Zentrum*.
The basis-free form proved here also holds in infinite dimension, where matrices are not available.

## Explanations

### L1 human

A scalar map $v \mapsto av$ commutes with every linear map, since linear maps respect scaling.
The theorem says that no other endomorphism commutes with all of them.

### L2 human

To test whether $T$ is central, it is enough to compare $T$ with projections onto lines.
If $T$ commutes with a projection onto the line through $v$, then $T(v)$ lies on that line.
A linear map that sends each vector to a multiple of itself is a scalar map.
Watch out: checking a few maps $S$ is not enough, since the condition involves every $S$.

### L3 human

The theorem shows that $\End(V)$ is a central algebra over $F$.
For finite-dimensional $V \ne \{0\}$, it is also simple, so it is a central simple algebra, and its class in the Brauer group of $F$ is trivial.
In representation theory, the same argument shows that the commutant of $\End(V)$ acting on $V$ is $F$.
