---
tag: 1WV2THA6NY
kind: concept
name: Pseudo-element
msc: ["18E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_category
---

## Summary

A pseudo-element of an object $A$ in an [[abelian category|Y9CZ3MTNF1]] is an equivalence class of morphisms with codomain $A$.
Two such morphisms are identified when they agree after composing with suitable [[epimorphisms|RVXDSY04KG]].
Pseudo-elements behave enough like elements of a module to allow diagram chasing inside any abelian category.
With them, one proves diagram lemmas such as the [[snake lemma|Q8AYGD93CW]] without an embedding theorem.

## Explanations

### L1 human

In a category of modules one proves diagram lemmas by following elements around the diagram.
A general abelian category has objects without elements, so one uses morphisms $x \colon X \to A$ as "generalized elements" instead.
Two generalized elements are treated as the same if they cover each other after pulling back along surjections.
For example, in abelian groups the maps $\Z \to \Z$ given by $n \mapsto n$ and $n \mapsto -n$ give the same pseudo-element of $\Z$.
So pseudo-elements are coarser than elements, but they detect zero, monomorphisms, epimorphisms and exactness.
