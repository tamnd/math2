---
tag: TEWH75TX8Y
kind: definition
name: Aleph number
msc: ["03E10"]
defines: 6Q9Z2BM1XR
uses: [0RDJK7EQYY, 0QKPNZKNEA, 0ZHQMQ2C1N, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Aleph_number
---

## Definition

Identify each [[cardinal number|0QKPNZKNEA]] of a well-orderable set with the least [[ordinal|0RDJK7EQYY]] of that cardinality.
For an infinite cardinal $\kappa$, let $\kappa^+$ be the least cardinal greater than $\kappa$.
The aleph numbers $\aleph_\alpha$, for ordinals $\alpha$, are defined by [[transfinite recursion|0ZHQMQ2C1N]]:

1. $\aleph_0 = \omega$, the set of natural numbers.
2. $\aleph_{\alpha + 1} = (\aleph_\alpha)^+$.
3. $\aleph_\lambda = \sup_{\beta < \lambda} \aleph_\beta$ for each nonzero limit ordinal $\lambda$, the [[supremum|0BTMQ04556]] of the earlier alephs.

## Remarks

Example: $\aleph_1$ is the set of countable ordinals, which is the least uncountable ordinal $\omega_1$.
Check: each countable ordinal is smaller than $\omega_1$, and $\omega_1$ itself is uncountable, so it is the least cardinal above $\aleph_0$.
Non-example: $\omega + 1$ is an infinite ordinal but not an aleph, since it has the same cardinality as the smaller ordinal $\omega$.
The cardinal $\kappa^+$ exists in ZF by Hartogs' theorem, without the axiom of choice.
The map $\alpha \mapsto \aleph_\alpha$ is a normal function, and every infinite well-orderable cardinal is $\aleph_\alpha$ for exactly one $\alpha$.
The ordinal $\aleph_\alpha$ is also written $\omega_\alpha$ when it is viewed as an ordinal.
