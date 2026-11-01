---
tag: 998RQZYBZ8
kind: definition
name: Injective hull
msc: [13C11, 18G05]
defines: QCJN05GN64
uses: [0B1261B5ED, 0NZ8JA25WK, 05WDSN597C, 85H7PRHDPZ]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_hull
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
An *essential extension* of $M$ is an injective homomorphism $i \colon M \to E$ of $R$-modules such that every nonzero [[submodule|05WDSN597C]] $N$ of $E$ satisfies $N \cap i(M) \ne 0$.
An *injective hull* (or injective envelope) of $M$ is an essential extension $i \colon M \to E$ such that $E$ is an [[injective module|85H7PRHDPZ]].
It is written $E(M)$ or $E_R(M)$.

## Remarks

Every module has an injective hull, and two injective hulls $i \colon M \to E$ and $i' \colon M \to E'$ are related by an isomorphism $f \colon E \to E'$ with $f \circ i = i'$.
Equivalently, an injective hull is a maximal essential extension, or a minimal injective module containing $M$.
Example: over $R = \Z$, the inclusion $\Z \to \Q$ is an injective hull; $\Q$ is divisible, hence injective, and a nonzero subgroup $N$ of $\Q$ containing $a/b \ne 0$ also contains $b \cdot (a/b) = a \in N \cap \Z$.
Non-example: the inclusion $\Z \to \Q \oplus \Q/\Z$, $n \mapsto (n, 0)$, has an injective target but is not essential, since the submodule $0 \oplus \Q/\Z$ meets the image only in $0$.
For a prime $p$, the injective hull of $\Z/p\Z$ over $\Z$ is the Prüfer group $\Z[1/p]/\Z$.
