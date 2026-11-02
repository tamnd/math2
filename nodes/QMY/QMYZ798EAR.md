---
tag: QMYZ798EAR
kind: definition
name: Identity component
msc: [22A05, 54D05]
defines: SDQTNBDJ2H
uses: [92700QAB5Y, 0JG9W3KA6B, 0CB0DX5BVV, 417ZRDCHY6, AW3J9AQSA0]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_component
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] with identity element $e$.
The *identity component* of $G$, written $G_0$ or $G^\circ$, is the [[connected component|0JG9W3KA6B]] of $G$ that contains $e$.

## Remarks

$G_0$ is a closed [[normal subgroup|0CB0DX5BVV]] of $G$.
It is a subgroup because $G_0 G_0^{-1}$ is the image of the connected set $G_0 \times G_0$ under $(x, y) \mapsto xy^{-1}$ and contains $e$, so it lies in $G_0$.
It is normal because each inner automorphism $x \mapsto gxg^{-1}$ is a homeomorphism fixing $e$.
The [[quotient|417ZRDCHY6]] $G/G_0$ is a [[totally disconnected group|AW3J9AQSA0]].
Example: for $G = \mathrm{GL}_n(\R)$, the identity component is the subgroup of matrices with positive determinant.
For $G = (\Q, +)$ with the topology from $\R$, the identity component is $\set{0}$, since $\Q$ is totally disconnected.
