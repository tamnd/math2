---
tag: 5Y3SAEWBZM
kind: definition
name: Noetherian scheme
msc: [14A15, "13E05"]
defines: ND6XEY68P4
uses: [5A35TYZD02, B3V3XJ2W8G, 0670T59HGE, 2VQX2E8EAH]
sources:
  - url: https://en.wikipedia.org/wiki/Noetherian_scheme
---

## Definition

A [[scheme|5A35TYZD02]] $X$ is *locally Noetherian* if it can be covered by open [[affine schemes|B3V3XJ2W8G]] $\operatorname{Spec} A_i$ in which every $A_i$ is a [[Noetherian ring|0670T59HGE]].
It is *Noetherian* if it can be covered by finitely many such open sets.

## Remarks

A scheme is locally Noetherian if and only if $A$ is Noetherian for every open affine subscheme $\operatorname{Spec} A$.
So $\operatorname{Spec} A$ is Noetherian if and only if $A$ is a Noetherian ring.
The underlying space of a Noetherian scheme is a [[Noetherian topological space|2VQX2E8EAH]].
Example: projective space $\mathbb{P}^n_k$ over a field $k$ is Noetherian, being covered by $n+1$ copies of $\operatorname{Spec} k[x_1, \ldots, x_n]$, which are Noetherian by the Hilbert basis theorem.
Non-example: $\operatorname{Spec} k[x_1, x_2, \ldots]$ is not Noetherian, since the ideal $(x_1, x_2, \ldots)$ is not finitely generated.
Non-example: a disjoint union of infinitely many copies of $\operatorname{Spec} k$ is locally Noetherian but not Noetherian, since it is not quasi-compact.
