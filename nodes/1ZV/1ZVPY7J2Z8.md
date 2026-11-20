---
tag: 1ZVPY7J2Z8
kind: proof
name: Outline of the proof of Morley's theorem on countable models via Scott analysis
msc: ["03C15", "03C75", "03E15"]
topics: [6XEXRME4C1]
audience: research
proves: JFG783DEG8
uses: [KAWWZ2DF0G, PQG7VAZ1R2, 3RWWZYPAFV, H47ZGRR13V, 584GXXY73M, W6XM5NVNRP]
methods: [0WCP0PVET6]
sources:
  - book: isbn:9780387987606
---

## Proof

This is an outline; the descriptive set theory in steps 3 and 4 is only sketched.
Let $T$ be a theory in a countable signature $L$.

### Setup

1. A countable model with universe $\N$ is coded by the set of atomic facts true in it, a point of the Cantor space. The codes of models of $T$ form a Borel subset of this [[Polish space|584GXXY73M]].
2. A *fragment* is a countable set of formulas of [[$L_{\omega_1 \omega}$|PQG7VAZ1R2]] that contains the first-order formulas and is closed under subformulas, finite Boolean operations and quantifiers. For a fragment $F$, an $F$-type is the set of $F$-formulas that a tuple satisfies.
3. Build fragments $F_\alpha$ for $\alpha < \omega_1$. $F_0$ is first-order logic. If the $F_\alpha$-types realized in countable models of $T$ form a countable set, $F_{\alpha+1}$ adds the conjunction of each of these types. At limits take unions.

### Case 1: some fragment has uncountably many types

1. Suppose that for some $\alpha$, uncountably many $F_\alpha$-types are realized in countable models of $T$.
2. The $F_\alpha$-types form a Polish space, and the set of realized ones is the image of a Borel set under a continuous map, so it is an [[analytic set|3RWWZYPAFV]].
3. An uncountable analytic set contains a perfect set, by the [[perfect set property|H47ZGRR13V]]. So $2^{\aleph_0}$ types are realized.
4. Each countable model realizes countably many types, so $T$ has $2^{\aleph_0}$ countable models, as in the counting argument for [[small theories|W6XM5NVNRP]].

### Case 2: every fragment has countably many types

1. Suppose that for every $\alpha < \omega_1$, only countably many $F_\alpha$-types are realized.
2. For a countable model $M$, the Scott analysis of [[this theorem|KAWWZ2DF0G]] gives a countable ordinal $\alpha$ such that the Scott sentence of $M$ lies in $F_\alpha$, by the construction in step 3 of the setup.
3. So the isomorphism type of $M$ is fixed by its complete $F_\alpha$-theory, which is the $F_\alpha$-type of the empty tuple.
4. For each $\alpha$ there are countably many such theories, and there are $\aleph_1$ ordinals $\alpha < \omega_1$. So $T$ has at most $\aleph_1 \cdot \aleph_0 = \aleph_1$ countable models.

## Idea

Approximate isomorphism by agreement in larger and larger countable fragments of $L_{\omega_1 \omega}$.
If some approximation already has uncountably many classes, descriptive set theory turns this into a perfect set and continuum many models.
If no approximation does, then countably many classes at each of $\aleph_1$ levels give at most $\aleph_1$ models.

## Variants

A theory in Case 2 for all $\alpha$ is called *scattered*.
The analysis shows that a counterexample to the Vaught conjecture must be scattered and have exactly $\aleph_1$ countable models.
The same argument works for a sentence of $L_{\omega_1 \omega}$ in place of $T$.
