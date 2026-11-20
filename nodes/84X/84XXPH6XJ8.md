---
tag: 84XXPH6XJ8
kind: definition
name: Reduced product
msc: ["03C20", "08B25"]
topics: [HZG1YP26AB]
audience: grad
defines: F4WRD396PB
uses: [983GZBQYT4, WDVVEYD6AT, 15PF73BKY6, 09CEDJYBKP, 0G8VEZ3WTK, WJ73XYBNE4]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_product
    locator: lead section
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], let $I$ be a nonempty set, and let $F$ be a [[filter|15PF73BKY6]] on $I$.
For each $i \in I$ let $\mathcal{M}_i$ be an $L$-[[structure|983GZBQYT4]] with nonempty domain $M_i$, and let $P = \prod_{i \in I} M_i$ be the [[Cartesian product|09CEDJYBKP]].
For $a, b \in P$ write $a \sim_F b$ when $\set{i \in I : a(i) = b(i)} \in F$, and let $[a]_F$ be the class of $a$.
The *reduced product* $\prod_{i \in I} \mathcal{M}_i / F$ is the $L$-structure with domain $P / {\sim_F}$ and these interpretations.

1. For an $n$-ary function symbol $f$: $f([a_1]_F, \dots, [a_n]_F) = [b]_F$, where $b(i) = f^{\mathcal{M}_i}(a_1(i), \dots, a_n(i))$.
2. For an $n$-ary relation symbol $R$: $R([a_1]_F, \dots, [a_n]_F)$ holds when $\set{i \in I : (a_1(i), \dots, a_n(i)) \in R^{\mathcal{M}_i}} \in F$.
3. For a constant symbol $c$: its value is $[b]_F$, where $b(i) = c^{\mathcal{M}_i}$.

If all $\mathcal{M}_i$ equal one structure $\mathcal{M}$, the reduced product is the *reduced power* $\mathcal{M}^I / F$.

## Remarks

We check that $\sim_F$ is an [[equivalence relation|0G8VEZ3WTK]] and that clauses 1 and 2 do not depend on the representatives.

1. Reflexivity: $\set{i : a(i) = a(i)} = I$, and $I \in F$.
2. Symmetry: the set $\set{i : a(i) = b(i)}$ does not change when $a$ and $b$ are exchanged.
3. Transitivity: $\set{i : a(i) = c(i)}$ contains $\set{i : a(i) = b(i)} \cap \set{i : b(i) = c(i)}$, which lies in $F$; a filter is closed under intersections and supersets.
4. Clause 1: if $a_k \sim_F a'_k$ for $k = 1, \dots, n$, then the two values of $f$ agree on the intersection of the sets $\set{i : a_k(i) = a'_k(i)}$, which lies in $F$.
5. Clause 2: the two truth sets of $R$ agree on the same intersection $X \in F$. If one of them is in $F$, its intersection with $X$ is in $F$, and so is the other set, which contains this intersection.

Example: for $F = \set{I}$, $\sim_F$ is equality, and the reduced product is the [[direct product|WJ73XYBNE4]].
For a nonempty $J \subseteq I$ and $F = \set{X \subseteq I : J \subseteq X}$, the reduced product is isomorphic to $\prod_{j \in J} \mathcal{M}_j$.

Non-example: on $I = \set{1, 2, 3}$, the family $G = \set{\set{1, 2}, \set{2, 3}, I}$ is not a filter, since $\set{1, 2} \cap \set{2, 3} = \set{2} \notin G$.
With it, the analogous relation on $\Z^3$ is not transitive.
The element $(0, 0, 0)$ is related to $(0, 0, 1)$, which is related to $(1, 0, 1)$, but $(0, 0, 0)$ and $(1, 0, 1)$ agree only on $\set{2}$.

When $F$ is an [[ultrafilter|J64Y3JC0RE]], the reduced product is the [[ultraproduct|AX9Q86GB8M]] $\prod_{i \in I} \mathcal{M}_i / F$.

## Explanations

### L1 human

We take all lists with one entry from each structure.
Two lists count as equal when the set of positions where they agree is "large", that is, in the filter.
Operations act position by position, and a relation holds when it holds at a large set of positions.

### L2 human

We compute in the reduced power $\Z^{\set{1,2,3}} / F$ with $F = \set{X : \set{1, 2} \subseteq X}$.

1. The filter $F$ has the members $\set{1, 2}$ and $\set{1, 2, 3}$.
2. So $(a_1, a_2, a_3) \sim_F (b_1, b_2, b_3)$ exactly when $a_1 = b_1$ and $a_2 = b_2$.
3. The map $[(a_1, a_2, a_3)]_F \mapsto (a_1, a_2)$ is well defined, bijective and respects $+$ and $\cdot$.
4. So the reduced power is isomorphic to the ring $\Z \times \Z$.

A trap is to use a family of "large" sets that is not closed under intersection; then $\sim_F$ fails to be transitive.
