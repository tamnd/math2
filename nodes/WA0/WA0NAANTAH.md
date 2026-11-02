---
tag: WA0NAANTAH
kind: definition
name: Sieve
msc: [18F10, 18F20]
defines: CNCXNWKC6R
uses: [A2DE66937D, KCCHH87H6E]
sources:
  - url: https://en.wikipedia.org/wiki/Sieve_(category_theory)
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $c$ be an object of $\mathcal{C}$.
A *sieve* on $c$ is a set $S$ of morphisms with codomain $c$ with the following property.
For every $f \colon d \to c$ in $S$ and every morphism $g \colon e \to d$, the composite $f \circ g$ is in $S$.

## Remarks

Equivalently, a sieve on $c$ is a subfunctor $S \subseteq \Hom_{\mathcal{C}}(-, c)$ of the [[representable functor|KCCHH87H6E]], with $S(d)$ the set of members of $S$ with domain $d$.
The *maximal sieve* on $c$ is the set of all morphisms with codomain $c$.
For a sieve $S$ on $c$ and a morphism $h \colon d \to c$, the *pullback sieve* $h^*S = \set{g : h \circ g \in S}$ is a sieve on $d$.
Example: view the poset of open subsets of a space $X$ as a category, and let $\set{U_i}$ be an open cover of $U$.
The open sets $V \subseteq U$ that lie in some $U_i$ form a sieve on $U$, since $W \subseteq V \subseteq U_i$ gives $W \subseteq U_i$.
Non-example: in the same category, the set $\set{U_1}$ alone is not a sieve on $U$ when $U_1$ has a smaller open subset $W \ne U_1$, since the composite $W \subseteq U_1 \subseteq U$ is missing.
