---
tag: ZC4BHVHWE9
kind: definition
name: Beth number
msc: ["03E10"]
defines: SS6WMEN6KX
uses: [0QKPNZKNEA, 0RDJK7EQYY, 0BC7KX51Z8, 0ZHQMQ2C1N, 0BTMQ04556, 0V2H5PGJ9B]
sources:
  - url: https://en.wikipedia.org/wiki/Beth_number
---

## Definition

Assume ZFC, so that each set has a [[cardinal number|0QKPNZKNEA]] and $2^\kappa$ is the cardinality of the [[power set|0BC7KX51Z8]] of a set of cardinality $\kappa$.
The beth numbers $\beth_\alpha$, for [[ordinals|0RDJK7EQYY]] $\alpha$, are defined by [[transfinite recursion|0ZHQMQ2C1N]]:

1. $\beth_0 = \aleph_0$, the cardinality of $\N$, see [[aleph-null|0V2H5PGJ9B]].
2. $\beth_{\alpha + 1} = 2^{\beth_\alpha}$.
3. $\beth_\lambda = \sup_{\beta < \lambda} \beth_\beta$ for each nonzero limit ordinal $\lambda$, the [[supremum|0BTMQ04556]] of the earlier beths.

## Remarks

Example: $\beth_1 = 2^{\aleph_0}$ is the cardinality of $\R$, since $\R$ is in bijection with the power set of $\N$.
$\beth_2 = 2^{2^{\aleph_0}}$ is the cardinality of the power set of $\R$, and also of the set of all functions $\R \to \R$.
Non-example: $\aleph_1$ is a beth number only if $\aleph_1 = \beth_1$, which is the continuum hypothesis and is not provable in ZFC.
By Cantor's theorem $\beth_{\alpha+1} > \beth_\alpha$, and by induction $\beth_\alpha \ge \aleph_\alpha$ for every $\alpha$.
Another notation is $\beth_\alpha = \beth_\alpha(\aleph_0)$; more generally $\beth_0(\kappa) = \kappa$ and $\beth_{\alpha+1}(\kappa) = 2^{\beth_\alpha(\kappa)}$.
