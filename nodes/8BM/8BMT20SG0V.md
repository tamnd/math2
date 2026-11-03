---
tag: 8BMT20SG0V
kind: definition
name: K1 of a ring
msc: [19B99, 19B14]
defines: SXVNJY4XFY
uses: [0B1261B5ED, G8R9561PXT, E5JXB0E324, 0ASGSTXSBW, 0AQZV0905N]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
    locator: K1
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $GL(R)$ be its [[stable general linear group|G8R9561PXT]].
The group $K_1(R)$ is the [[abelianisation|0AQZV0905N]]
$$K_1(R) = GL(R)/[GL(R), GL(R)],$$
where $[GL(R), GL(R)]$ is the [[commutator subgroup|0ASGSTXSBW]].

## Remarks

Whitehead's lemma says $[GL(R), GL(R)] = E(R)$, the [[elementary subgroup|E5JXB0E324]], so $K_1(R) = GL(R)/E(R)$.
The group $K_1(R)$ is abelian, and the class of a product $AB$ equals the class of $\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}$.
If $R$ is commutative, the determinant $\det \colon GL(R) \to R^\times$ kills $E(R)$, so it induces a surjection $K_1(R) \to R^\times$, split by $u \mapsto [\mathrm{diag}(u, 1, 1, \dots)]$.
Example: for a field $F$, every matrix of determinant $1$ is a product of elementary matrices, so $K_1(F) \cong F^\times$.
Non-example: the group $GL(R)$ itself is not $K_1(R)$ for $R = \Q$, since $GL(\Q)$ is not abelian while $K_1(\Q) \cong \Q^\times$ is.
