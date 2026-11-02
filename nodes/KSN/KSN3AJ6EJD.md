---
tag: KSN3AJ6EJD
kind: definition
name: Localization of a category
msc: ["18E35"]
defines: DNFR3YP0XF
uses: [A2DE66937D, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_of_a_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $W$ be a class of morphisms of $\mathcal{C}$.
A *localization of $\mathcal{C}$ at $W$* is a category $\mathcal{C}[W^{-1}]$ together with a [[functor|28NQ0KRHD3]] $\gamma \colon \mathcal{C} \to \mathcal{C}[W^{-1}]$ such that:

1. $\gamma(w)$ is an isomorphism for every $w \in W$;
2. for every functor $F \colon \mathcal{C} \to \mathcal{D}$ such that $F(w)$ is an isomorphism for every $w \in W$, there is a unique functor $G \colon \mathcal{C}[W^{-1}] \to \mathcal{D}$ with $F = G \circ \gamma$.

## Remarks

By the universal property, a localization is unique up to a unique isomorphism of categories compatible with $\gamma$.
It always exists if size issues are ignored.
Its objects are those of $\mathcal{C}$, and its morphisms are equivalence classes of zigzags of morphisms of $\mathcal{C}$ whose backward arrows are in $W$.
The hom-sets of this construction may fail to be small; conditions such as a calculus of fractions or a model structure give control over them.
Many authors use a weaker universal property, asking that precomposition with $\gamma$ be an equivalence between functor categories onto the functors that invert $W$.

Example: let $\mathcal{C}$ have two objects $0$ and $1$ and one non-identity morphism $a \colon 0 \to 1$, and let $W = \set{a}$.
The category $\mathcal{L}$ with objects $0, 1$ and exactly one morphism between any two objects is a localization, with $\gamma$ the identity on objects.
Indeed $\gamma(a)$ is invertible, and a functor $F$ inverting $a$ factors uniquely by sending the morphism $1 \to 0$ of $\mathcal{L}$ to $F(a)^{-1}$.

Non-example: the identity functor $\mathcal{C} \to \mathcal{C}$ satisfies clause 2 for the functors that invert $a$, but it fails clause 1, since $a$ is not an isomorphism in $\mathcal{C}$.
