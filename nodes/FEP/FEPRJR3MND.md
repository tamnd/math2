---
tag: FEPRJR3MND
kind: concept
name: Eilenberg–Moore category
msc: [18C20]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Summary

The Eilenberg–Moore category of a [[monad|FF6XXA6D1A]] $T$ on a category $\mathcal{C}$ is the category of [[algebras over|QG1ZXRC8EH]] $T$ and their morphisms.
It comes with a forgetful functor to $\mathcal{C}$ and a free algebra functor, and these form an adjunction whose monad is $T$ again.
It is the terminal adjunction that gives $T$, and so it shows that every monad comes from an adjunction.

## Explanations

### L1 human

Given a monad, collect all the ways of evaluating its formal expressions, that is, all its algebras.
Together with the maps that respect evaluation, they form a new category.
For the list monad on sets, this new category is the category of monoids.
So the Eilenberg–Moore category rebuilds an algebraic category from its monad.
