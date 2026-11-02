---
tag: GYXTW7PF56
kind: definition
name: Quasi-Frobenius ring
msc: [16L60, 16D50]
defines: KP1PP7A6JR
uses: [0B1261B5ED, AK1ZRCXR32, KQKJENEMSN]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-Frobenius_ring
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity.
The ring $R$ is *quasi-Frobenius* if:

1. $R$ is left Noetherian, that is, $R$ is a [[Noetherian module|AK1ZRCXR32]] as a left module over itself;
2. $R$ is [[left self-injective|KQKJENEMSN]].

## Remarks

The definition is left-right symmetric: a ring satisfying the two clauses is also right Noetherian and right self-injective, and it is left and right Artinian.
Example: $\Z/n\Z$ for $n \ge 1$.
It is finite, so clause 1 holds, and it is self-injective by Baer's criterion, so clause 2 holds.
Non-example: $\Z$ is Noetherian but not self-injective, since the map $2\Z \to \Z$, $2m \mapsto m$, does not extend to $\Z$; clause 2 fails.
Non-example: $k[x, y]/(x^2, xy, y^2)$ over a field $k$ is Artinian, hence Noetherian, but not self-injective, so clause 2 fails.
Equivalent forms: $R$ is quasi-Frobenius if and only if every projective left $R$-module is injective, if and only if every injective left $R$-module is projective.
Every [[Frobenius algebra|8EVP1K2CZH]] is quasi-Frobenius.
