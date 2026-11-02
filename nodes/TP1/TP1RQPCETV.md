---
tag: TP1RQPCETV
kind: definition
name: Stable vector bundle
msc: [14H60, 14D20]
defines: RQRJ5H4Y3E
uses: [XJM2MT4S3Y, P4DZM975BV, Z9DN23DAE2]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_vector_bundle
---

## Definition

Let $k$ be an algebraically closed field and let $C$ be a smooth projective connected [[algebraic curve|XJM2MT4S3Y]] over $k$.
For a nonzero [[vector bundle|P4DZM975BV]] $E$ on $C$ of rank $r$, let $\deg E$ be the degree of a [[divisor|Z9DN23DAE2]] of its determinant line bundle $\det E = \Lambda^r E$.
The *slope* of $E$ is $\mu(E) = \deg E / \rank E$.
The bundle $E$ is *stable* if
$$\mu(F) < \mu(E)$$
for every subbundle $F \subset E$ with $0 < \rank F < \rank E$.
It is *semistable* if $\mu(F) \le \mu(E)$ for every such $F$.

## Remarks

Example: every line bundle is stable, since it has no subbundle of intermediate rank.
Non-example: let $L_1, L_2$ be line bundles with $\deg L_1 > \deg L_2$.
Then $L_1$ is a subbundle of $E = L_1 \oplus L_2$ with $\mu(L_1) = \deg L_1 > (\deg L_1 + \deg L_2)/2 = \mu(E)$, so $E$ is not even semistable.
The bundle $\mathcal{O}_C \oplus \mathcal{O}_C$ is semistable but not stable, since $\mathcal{O}_C$ has the same slope $0$.
One may test with all nonzero proper coherent subsheaves instead of subbundles; the condition is the same.
A stable bundle $E$ is simple: its only endomorphisms are the scalars.
On a smooth projective variety of higher dimension with an ample class $H$, slope stability (Mumford–Takemoto stability) uses torsion-free subsheaves and the degree $c_1(F) \cdot H^{n-1}$.
