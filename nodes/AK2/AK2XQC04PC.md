---
tag: AK2XQC04PC
kind: definition
name: Exact functor
msc: ["18E10", 18G10]
defines: S1G61TDW0K
uses: [Y9CZ3MTNF1, KAN07YC9T2, KJKNJMGKZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_functor
---

## Definition

Let $\mathcal{A}$ and $\mathcal{B}$ be [[abelian categories|Y9CZ3MTNF1]] and let $F \colon \mathcal{A} \to \mathcal{B}$ be an [[additive functor|KAN07YC9T2]].
Let $0 \to A' \to A \to A'' \to 0$ denote an arbitrary [[short exact sequence|KJKNJMGKZZ]] in $\mathcal{A}$.

1. $F$ is *left exact* if $0 \to F(A') \to F(A) \to F(A'')$ is exact for every such sequence.
2. $F$ is *right exact* if $F(A') \to F(A) \to F(A'') \to 0$ is exact for every such sequence.
3. $F$ is *exact* if $0 \to F(A') \to F(A) \to F(A'') \to 0$ is exact for every such sequence, that is, if $F$ is both left exact and right exact.

## Remarks

An exact functor preserves all exact sequences, not only the short ones.
A functor is left exact if and only if it preserves kernels, and right exact if and only if it preserves cokernels.
For a contravariant functor the same words are used after replacing $\mathcal{A}$ by its opposite category.

Example: for a ring $R$ and an $R$-module $M$, the functor $\Hom_R(M, -)$ is left exact, and $M \otimes_R -$ is right exact.
The functor $\Q \otimes_{\Z} -$ on abelian groups is exact, because $\Q$ is a flat $\Z$-module.

Non-example: $F = \Z/2\Z \otimes_{\Z} -$ is right exact but not exact.
Apply it to $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$.
The first map becomes multiplication by $2$ on $\Z/2\Z$, which is zero and so not injective.
