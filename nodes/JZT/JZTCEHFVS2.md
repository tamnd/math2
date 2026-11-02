---
tag: JZTCEHFVS2
kind: statement
role: theorem
name: Existence of limits from products and equalizers
msc: [18A35, 18A30]
uses: [A2DE66937D, S5744QZV4N, CTJ5AD8ST5, CHS5AFJGWE, FWGPKXCPB7, PYSBNWCHCF]
about: [CHS5AFJGWE, FWGPKXCPB7]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_category
---

## Statement

Let $\mathcal{C}$ be a [[category|A2DE66937D]] that has [[equalizers|CTJ5AD8ST5]] of all pairs of parallel morphisms.

1. If $\mathcal{C}$ has all small [[products|S5744QZV4N]], then $\mathcal{C}$ is [[complete|FWGPKXCPB7]].
2. If $\mathcal{C}$ has all finite products, then $\mathcal{C}$ is [[finitely complete|PYSBNWCHCF]].

## Remarks

Let $F \colon J \to \mathcal{C}$ be a diagram with $J$ small, and write $u \colon j \to k$ for the morphisms of $J$.
Form the products $P = \prod_{j} F(j)$ over the objects and $Q = \prod_{u \colon j \to k} F(k)$ over the morphisms.
Two morphisms $s, t \colon P \to Q$ are given on the factor of $u \colon j \to k$ by $F(u) \circ \pi_j$ and by $\pi_k$.
The equalizer of $s$ and $t$ is a [[limit|CHS5AFJGWE]] of $F$.
If $J$ is finite, only finite products are used.

The converse is clear, since products and equalizers are limits.
For example, in the category of groups the limit of a diagram is the subgroup of the product cut out by the equations $F(u)(x_j) = x_k$.
Dually, a category with all small coproducts and all coequalizers is cocomplete.

## Explanations

### L1 human

Every limit can be built from two simple ones.
First take the product of all the objects of the diagram.
Then cut it down with an equalizer to the families that agree with all the maps.
So to show that a category has all limits, it is enough to check products and equalizers.

### L2 human

This is the usual way to prove that a category is complete.
For sets, groups, rings and topological spaces the products and equalizers are easy to write down, and the theorem does the rest.
The same construction shows that a functor which preserves products and equalizers preserves all limits.
It also gives the finite version: a terminal object, binary products and equalizers give all finite limits.
