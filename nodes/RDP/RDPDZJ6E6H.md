---
tag: RDPDZJ6E6H
kind: definition
name: Semiprimary ring
msc: [16L30, 16N20]
defines: XVP517QRH5
uses: [0894J980RK, XA0DCNH7WY, YH75M7XAM1, C2H26BYWHE]
sources:
  - url: https://en.wikipedia.org/wiki/Hopkins%E2%80%93Levitzki_theorem
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity and $J = J(R)$ its [[Jacobson radical|XA0DCNH7WY]].
$R$ is *semiprimary* if the following hold.

1. $R$ is [[semilocal|YH75M7XAM1]], that is, $R/J$ is a semisimple ring.
2. $J$ is a [[nilpotent ideal|C2H26BYWHE]]: $J^n = 0$ for some integer $n \ge 1$.

## Remarks

Example: the ring $R$ of upper triangular $2 \times 2$ matrices over a field $k$ is semiprimary: $J$ is the set of strictly upper triangular matrices, $J^2 = 0$, and $R/J \cong k \times k$ is semisimple.
Non-example: $\Z_{(p)}$ satisfies clause 1, since $\Z_{(p)}/p\Z_{(p)} \cong \mathbb{F}_p$, but not clause 2, since $p^n \ne 0$ for every $n$.
Every left Artinian ring is semiprimary, and a semiprimary ring is left Artinian if and only if it is left Noetherian.
The definition is left-right symmetric.
