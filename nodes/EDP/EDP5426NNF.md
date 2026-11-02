---
tag: EDP5426NNF
kind: definition
name: Galois category
msc: [14F35, 18B99]
defines: 3RGBA24QVA
uses: [A2DE66937D, 28NQ0KRHD3, EK85VSSRMR, Q05K04QJ71, 4FJ0S71P58, E70DQGM8X5, DVSTWGVCSZ, Y2NP1JFR86]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck%27s_Galois_theory
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $F \colon \mathcal{C} \to \mathbf{FinSet}$ be a [[functor|28NQ0KRHD3]] to the category of finite sets.
Let $q \colon Y \to X$ be a morphism of $\mathcal{C}$ such that the [[pullback|Q05K04QJ71]] $Y \times_X Y$ exists.
The morphism $q$ is a *strict epimorphism* when it is the [[coequalizer|DVSTWGVCSZ]] of the two projections $Y \times_X Y \to Y$, its [[kernel pair|E70DQGM8X5]].
The pair $(\mathcal{C}, F)$ is a *Galois category*, and $F$ is a *fibre functor*, when these axioms hold:

1. $\mathcal{C}$ has a [[terminal object|EK85VSSRMR]] and all fibre products.
2. $\mathcal{C}$ has finite [[coproducts|4FJ0S71P58]], in particular an initial object, and for each object $X$ and each finite subgroup $G$ of $\Aut(X)$ the quotient $X/G$ exists.
3. Each morphism $u \colon Y \to X$ factors as $u = u' \circ u''$ with $u''$ a strict epimorphism and $u'$ a [[monomorphism|Y2NP1JFR86]].
Moreover, each monomorphism $Y \to X$ is an isomorphism of $Y$ onto a direct summand of $X$, that is, onto a coproduct component.
4. $F$ sends a terminal object to a terminal object and preserves fibre products.
5. $F$ preserves finite coproducts, sends strict epimorphisms to surjections, and preserves quotients by finite groups of automorphisms.
6. If $u$ is a morphism of $\mathcal{C}$ and $F(u)$ is a bijection, then $u$ is an isomorphism.

## Remarks

Here $X/G$ means the coequalizer of the family of maps $g \colon X \to X$, $g \in G$.
Example: for a [[profinite group|KA0YDB6QXE]] $\pi$, the category of finite sets with a continuous action of $\pi$, with $F$ the functor that forgets the action, satisfies all six axioms.
Main theorem: for every Galois category $(\mathcal{C}, F)$, the group $\pi = \Aut(F)$ is profinite and $F$ induces an equivalence of $\mathcal{C}$ with finite continuous $\pi$-sets.
Non-example: the category of all finite sets with $F$ the functor that doubles each set, $F(X) = X \sqcup X$, fails axiom 4, since it sends the one-point set to a two-point set.
The axioms follow Grothendieck's SGA 1; for a field $k$, finite étale $k$-algebras with arrows reversed form a Galois category whose group is the absolute Galois group of $k$.
