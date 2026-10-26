---
tag: 0AT1ZSNM25
kind: definition
name: Normaliser
aliases: [normalizer]
msc: [20A05]
defines: 0YGN3VAA0D
uses: [0N0PXCTYA7, 0D6WHTTH7T]
sources:
  - url: https://en.wikipedia.org/wiki/Centralizer_and_normalizer
    locator: Group and semigroup
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $S$ be a subset of $G$.
The normaliser of $S$ in $G$ is the set $N_G(S) = \{g \in G : gSg^{-1} = S\}$, where $gSg^{-1} = \{gsg^{-1} : s \in S\}$.

## Remarks

The normaliser $N_G(S)$ is a [[subgroup|0X1JXT47GA]] of $G$, and it contains the [[centraliser|02YYV36BFM]] $C_G(S)$.
If $H$ is a subgroup of $G$, then $H$ is a [[normal subgroup|0CB0DX5BVV]] of $N_G(H)$. Also, $N_G(H)$ is the largest subgroup of $G$ with this property.
Thus $H$ is normal in $G$ exactly when $N_G(H) = G$.
The number of [[conjugates|0H11ZPX4ND]] of $H$ in $G$ is the index $[G : N_G(H)]$.

## Explanations

### L1 human

The normaliser of a subgroup is the set of elements that do not move the subgroup when they conjugate it.
They may move the elements of the subgroup around, but the subgroup as a set stays in place.
The normaliser is big when the subgroup is close to normal.
