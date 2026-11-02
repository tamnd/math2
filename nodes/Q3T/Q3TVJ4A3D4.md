---
tag: Q3TVJ4A3D4
kind: definition
name: Grothendieck topology
msc: [18F10, 14F20]
defines: GDRFSJ8E2B
uses: [A2DE66937D, CNCXNWKC6R]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_topology
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
For a [[sieve|CNCXNWKC6R]] $S$ on $c$ and a morphism $h \colon d \to c$, let $h^*S = \set{g : h \circ g \in S}$ be the pullback sieve on $d$.
A *Grothendieck topology* $J$ on $\mathcal{C}$ assigns to each object $c$ a set $J(c)$ of sieves on $c$, the *covering sieves*, such that:

1. (maximal sieve) the sieve of all morphisms with codomain $c$ is in $J(c)$;
2. (stability) if $S \in J(c)$ and $h \colon d \to c$ is a morphism, then $h^*S \in J(d)$;
3. (transitivity) if $S \in J(c)$ and $R$ is a sieve on $c$ such that $h^*R \in J(d)$ for every $h \colon d \to c$ in $S$, then $R \in J(c)$.

## Remarks

Example: let $X$ be a topological space and $\mathcal{O}(X)$ the poset of open sets as a category.
Let $J(U)$ be the set of sieves $S$ on $U$ whose members have union $U$.
Clause 1 holds because $U \subseteq U$ is in the maximal sieve.
Clause 2 holds because the sets $V \cap W$ with $V \in S$ cover $W$ when $S$ covers $U \supseteq W$.
Clause 3 holds because covers of the members of a cover together give a cover.
Non-example: on $\mathcal{O}(X)$ with $X$ nonempty, the rule $J(U) = \emptyset$ for all $U$ fails clause 1.
On every category, the rule in which only maximal sieves cover is a Grothendieck topology, and so is the rule in which every sieve covers.
Many authors start from a *pretopology*, a choice of covering families of morphisms; it generates a Grothendieck topology by taking the sieves that contain a covering family.
