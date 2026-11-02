---
tag: Z9HNJ529DF
kind: definition
name: Flag variety
msc: [14M15, 14M17]
defines: NHRWCQQKTH
uses: [5JSYA1JNCC, 2XS84PWE3S, 85TWR6E75P, A4H4CZ2V35, CYPA882RB9]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_flag_variety
---

## Definition

Let $k$ be a field, let $V$ be a vector space of dimension $n$ over $k$, and let $0 < d_1 < \cdots < d_m < n$ be integers.
A *flag* of type $(d_1, \ldots, d_m)$ in $V$ is a chain of subspaces $V_1 \subset \cdots \subset V_m$ with $\dim V_i = d_i$.
The *flag variety* $\mathrm{Fl}(d_1, \ldots, d_m; V)$ is the set of these flags.
It is a closed subvariety of the product of [[Grassmannians|CYPA882RB9]] $\prod_i \mathrm{Gr}(d_i, V)$, so it is a [[projective variety|A4H4CZ2V35]].
The *full flag variety* is the case $(d_1, \ldots, d_m) = (1, 2, \ldots, n - 1)$.

## Remarks

The group $\mathrm{GL}(V)$ acts transitively on the flags of a given type, so the flag variety is a [[homogeneous space|85TWR6E75P]].
The stabilizer of a full flag is a [[Borel subgroup|5JSYA1JNCC]], conjugate to the upper triangular matrices, so the full flag variety is $\mathrm{GL}_n / B$.

General form: let $G$ be a connected [[reductive group|2XS84PWE3S]] over an algebraically closed field.
A closed subgroup $P$ of $G$ is *parabolic* if it contains a Borel subgroup.
The *generalized flag variety* is $G / P$, a smooth projective homogeneous variety.

Example: for $m = 1$, the flag variety $\mathrm{Fl}(d_1; V)$ is the Grassmannian $\mathrm{Gr}(d_1, V)$, and for $d_1 = 1$ it is the projective space $\mathbb{P}(V)$.

Non-example: let $T$ be the diagonal torus of $\mathrm{GL}_2$, the stabilizer of the pair of coordinate lines.
The quotient $\mathrm{GL}_2 / T$ is the space of ordered pairs of distinct lines in $k^2$, which is $\mathbb{P}^1 \times \mathbb{P}^1$ minus its diagonal.
It is not projective, since $T$ contains no Borel subgroup, and it is not a flag variety.
