---
tag: HSR36SAQY3
kind: statement
role: theorem
name: A finite abelian group is isomorphic to its dual
msc: [20K01, 43A40]
uses: [082GHNPJ53, FPRA2KEHFF, 07CQR9BW3R, 0KVGH0J5B3, PZMGQMDN25]
about: [FPRA2KEHFF]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Statement

Let $G$ be a finite [[abelian group|082GHNPJ53]], and let $\widehat{G}$ be its [[character group|FPRA2KEHFF]].
Then $G$ and $\widehat{G}$ are [[isomorphic|PZMGQMDN25]] groups.
Moreover, the map $G \to \widehat{\widehat{G}}$ that sends $x$ to the evaluation $\chi \mapsto \chi(x)$ is an isomorphism.

## Remarks

Proof idea: for the [[cyclic group|0KVGH0J5B3]] $\Z/n\Z$, the map $\chi \mapsto \chi(1)$ is an isomorphism from $\widehat{\Z/n\Z}$ to the group of $n$-th roots of unity, which is cyclic of order $n$.
Duals of products are products of duals, so the [[classification of finite abelian groups|07CQR9BW3R]] gives $G \cong \widehat{G}$.
The evaluation map is injective because characters separate points, and both groups have the same order.

Example: for $G = \Z/6\Z$, the character $\chi(a) = e^{2\pi i a/6}$ generates $\widehat{G}$, and $k \mapsto \chi^k$ is an isomorphism $\Z/6\Z \to \widehat{G}$.

The first isomorphism is not canonical: in general it depends on a choice of generators, and there is no natural isomorphism $G \to \widehat{G}$.
The second one, to the double dual, needs no choice.
Without the hypothesis that $G$ is abelian the statement fails: $\widehat{S_3}$ has order $2$.

## Explanations

### L1 human

A finite abelian group and its group of characters have the same shape.
But to match them up one has to make choices, while matching the group with the characters of its characters needs no choice.
This is like a finite-dimensional vector space, which is isomorphic to its dual space but canonically isomorphic only to its double dual.

### L2 human

The result is the finite case of Pontryagin duality, where the second statement holds for every locally compact abelian group.
The first statement fails beyond the finite case: the circle and its dual $\Z$ are not isomorphic.
It is often used to transfer statements about subgroups of $G$ to statements about subgroups of $\widehat{G}$ through annihilators.
