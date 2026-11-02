---
tag: VJXS8AK67E
kind: concept
name: Hom functor
msc: [18A25, 18A05]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Hom_functor
same_as:
  wikidata: Q5887297
  wikipedia: Hom functor
---

## Summary

In a locally small [[category|A2DE66937D]] $\mathcal{C}$, each object $A$ gives a [[functor|28NQ0KRHD3]] $\Hom(A, -)$ from $\mathcal{C}$ to the category of sets.
It sends an object $X$ to the set of morphisms $A \to X$.
Dually, $\Hom(-, A)$ is a contravariant functor.
Hom functors are the basic examples of functors into sets, and the Yoneda lemma says that they control all other such functors.

## Explanations

### L1 human

An object $A$ can be studied by the arrows that leave it: for each object $X$, collect all arrows from $A$ to $X$ into a set.
An arrow $X \to Y$ then turns each arrow $A \to X$ into an arrow $A \to Y$, by following one and then the other.
This turns $\Hom(A, -)$ into a functor.
For example, in the category of sets with $A = \{*\}$ a one-point set, a map $\{*\} \to X$ is the same as a point of $X$, so $\Hom(\{*\}, -)$ is essentially the identity functor.
