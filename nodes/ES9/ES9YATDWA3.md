---
tag: ES9YATDWA3
kind: concept
name: Algebra over an operad
msc: [18M60, 18M75, 55P48]
sources:
  - url: https://en.wikipedia.org/wiki/Operad_algebra
same_as:
  wikidata: Q16827071
  wikipedia: Operad algebra
---

## Summary

An operad lists abstract operations with several inputs and one output, together with rules for plugging operations into each other.
An algebra over an operad is an object on which these abstract operations act as actual operations, compatibly with plugging, units and permutations of inputs.
Monoids, commutative monoids, Lie algebras and loop spaces are all algebras over suitable operads.
The notion lets one treat many algebraic structures, and their homotopy-coherent versions, in one framework.

## Explanations

### L1 human

Think of an operad as a menu of recipes, each taking $n$ ingredients and producing one dish.
An algebra over the operad is a kitchen that can actually cook every recipe on the menu with its own ingredients.
Cooking a recipe whose ingredients are dishes of other recipes must give the same result as cooking the combined recipe.
Take the operad with exactly one $n$-ary recipe for every $n$.
An algebra over it is a set with an associative and commutative multiplication with a unit, that is, a commutative [[monoid|0N6R902FG1]].
Loop spaces are algebras over the [[little cubes operad|FWT0003QS1]], which is the origin of the theory.
