---
tag: YH75M7XAM1
kind: definition
name: Semilocal ring
msc: [16L30]
defines: ZDCDS6EWGX
uses: [0894J980RK, XA0DCNH7WY, NY25HXA478]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-local_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity and $J(R)$ its [[Jacobson radical|XA0DCNH7WY]].
$R$ is *semilocal* if the quotient ring $R/J(R)$ is [[semisimple|NY25HXA478]], that is, semisimple as a left module over itself.

## Remarks

By the [[Artin–Wedderburn theorem|R1F271180N]], $R$ is semilocal exactly when $R/J(R) \cong M_{n_1}(D_1) \times \cdots \times M_{n_k}(D_k)$ for division rings $D_i$ and integers $n_i \ge 1$.
Example: $M_n(\Z_{(p)})$ is semilocal, since its Jacobson radical is $M_n(p\Z_{(p)})$ and the quotient is $M_n(\mathbb{F}_p)$.
Non-example: $\Z$ is not semilocal: $J(\Z) = 0$ and $\Z$ is not semisimple, since the ideal $2\Z$ has no complement.
A commutative ring is semilocal if and only if it has finitely many maximal ideals; this is the [[commutative notion|6DYAGW68AV]].
The definition is left-right symmetric, and the spelling *semi-local* is also used.
