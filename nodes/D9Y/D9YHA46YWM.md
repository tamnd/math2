---
tag: D9YHA46YWM
kind: concept
name: Kleisli category
msc: ["18C20", "18C15"]
specializes: [A2DE66937D]
sources:
  - url: https://en.wikipedia.org/wiki/Kleisli_category
same_as:
  wikidata: Q1773982
  wikipedia: Kleisli category
---

## Summary

The Kleisli category of a [[monad|FF6XXA6D1A]] $T$ on a category $\mathcal{C}$ has the same objects as $\mathcal{C}$.
A morphism from $X$ to $Y$ in it is a morphism $X \to T Y$ of $\mathcal{C}$.
Composition uses the multiplication of the monad to flatten $T T$ to $T$.
It is equivalent to the full subcategory of free algebras in the [[Eilenberg–Moore category|FEPRJR3MND]].
Among all adjunctions that induce the monad, it gives the initial one.
In computer science, Kleisli morphisms model programs with side effects, such as partiality, nondeterminism or state.

## Explanations

### L1 human

For the powerset monad, a morphism from $X$ to $Y$ in the Kleisli category is a map that sends each element of $X$ to a set of elements of $Y$.
Such a map is the same as a relation between $X$ and $Y$.
Composing two of them means following all possible paths, which is the usual composition of relations.
So the Kleisli category of the powerset monad is the category of sets and relations.
