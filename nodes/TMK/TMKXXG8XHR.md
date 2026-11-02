---
tag: TMKXXG8XHR
kind: definition
name: Semiprimitive ring
msc: [16N20]
defines: 1B2DBKV1C9
uses: [0894J980RK, XA0DCNH7WY, 5N2CJZ47D4]
sources:
  - url: https://en.wikipedia.org/wiki/Semiprimitive_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity.
$R$ is *semiprimitive* if its [[Jacobson radical|XA0DCNH7WY]] $J(R)$, the intersection of all maximal [[left ideals|5N2CJZ47D4]] of $R$, is $0$.

## Remarks

Example: $\Z$ is semiprimitive, since its maximal ideals are $p\Z$ for primes $p$ and $\bigcap_p p\Z = 0$.
Non-example: the local ring $\Z_{(p)}$ of fractions with denominator prime to $p$ is not semiprimitive, since $J(\Z_{(p)}) = p\Z_{(p)} \ne 0$.
Equivalently, $R$ is a subdirect product of left [[primitive rings|8F6EHDVJ62]], or $R$ has a faithful semisimple left module.
The definition is left-right symmetric, because $J(R)$ is also the intersection of the maximal right ideals.
Other names are *Jacobson semisimple* and *J-semisimple*.
