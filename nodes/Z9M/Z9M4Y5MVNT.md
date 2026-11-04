---
tag: Z9M4Y5MVNT
kind: proof
name: Proof that orbits partition the set
msc: [20B05]
proves: 0ZC7FYE0NZ
uses: [0YSE802YCQ, 00F2JFA41J, 0SGTMBEWRF, 082RMRSY26, 01HT2CH8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbits and stabilizers
---

## Proof

We check the three axioms of an equivalence relation, then identify the classes. Let $e$ be the identity of $G$.

1. Reflexivity. By the first axiom of an [[action|0YSE802YCQ]], $x = e \cdot x$. So $x \sim x$ for each $x \in X$.
2. Symmetry. Let $x \sim y$, so $y = g \cdot x$ for some $g \in G$. By the two axioms of an action, $g^{-1} \cdot y = g^{-1} \cdot (g \cdot x) = (g^{-1} g) \cdot x = e \cdot x = x$.
3. So $x = g^{-1} \cdot y$ with $g^{-1} \in G$, and $y \sim x$.
4. Transitivity. Let $x \sim y$ and $y \sim z$, so $y = g \cdot x$ and $z = h \cdot y$ with $g, h \in G$. By the second axiom, $z = h \cdot (g \cdot x) = (hg) \cdot x$.
5. Since $hg \in G$, we get $x \sim z$. By steps 1 to 4, $\sim$ is an [[equivalence relation|0SGTMBEWRF]] on $X$.
6. The [[equivalence class|082RMRSY26]] of $x$ is $\set{y \in X : x \sim y} = \set{g \cdot x : g \in G}$. This is the [[orbit|00F2JFA41J]] $G \cdot x$. So the equivalence classes are exactly the orbits.
7. The [[equivalence classes form a partition|01HT2CH8BH]] of $X$. So each point of $X$ lies in exactly one orbit.

## Idea

The group axioms are exactly what is needed: the identity gives reflexivity, inverses give symmetry, and closure under products gives transitivity. Equivalence classes always partition a set, so the orbits do too.
