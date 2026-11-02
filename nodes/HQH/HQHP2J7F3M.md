---
tag: HQHP2J7F3M
kind: definition
name: Algebraic space
msc: [14A20]
defines: MTV9TFKF3X
uses: [5A35TYZD02, SWWW9X4A3N, 1DZMT4S9FB, H84VHC8PX2, TB6TM6R4MD]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_space
---

## Definition

Let $S$ be a [[scheme|5A35TYZD02]], and let $\mathcal{C}$ be the category of schemes over $S$ with the fppf topology.
For an $S$-scheme $U$, let $h_U$ be its [[functor of points|SWWW9X4A3N]].
An *algebraic space* over $S$ is a functor $F \colon \mathcal{C}^{\mathrm{op}} \to \mathrm{Sets}$ such that:

1. $F$ is a [[sheaf|TB6TM6R4MD]] for the fppf topology.
2. For all $S$-schemes $T_1, T_2$ and maps $h_{T_1} \to F$, $h_{T_2} \to F$, the [[fiber product|1DZMT4S9FB]] $h_{T_1} \times_F h_{T_2}$ is isomorphic to $h_T$ for some scheme $T$.
3. There are an $S$-scheme $U$ and a map $h_U \to F$ with the following property.
For every $S$-scheme $T$ and map $h_T \to F$, the induced morphism $U \times_F T \to T$ is surjective and [[étale|H84VHC8PX2]].

## Remarks

Every $S$-scheme $X$ gives an algebraic space $h_X$.
Clause 1 holds because representable functors are fppf sheaves, clause 2 because $h_{T_1} \times_{h_X} h_{T_2} = h_{T_1 \times_X T_2}$, and clause 3 holds with $U = X$.
A functor that is not a sheaf is not an algebraic space.
For example, the constant presheaf with value $\set{0, 1}$ fails clause 1: on the disjoint union of two copies of $S$ it should have four sections, but it has two.
Clause 2 says that the diagonal $F \to F \times F$ is representable by schemes, and clause 3 then makes sense.
Some authors use the étale topology in clause 1 and add a quasi-compactness condition on the diagonal, as in Knutson's book.
