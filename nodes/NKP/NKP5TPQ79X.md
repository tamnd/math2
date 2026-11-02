---
tag: NKP5TPQ79X
kind: concept
name: Subobject classifier
msc: [18B25, 03G30]
sources:
  - url: https://en.wikipedia.org/wiki/Subobject_classifier
same_as:
  wikidata: Q7631737
  wikipedia: Subobject classifier
---

## Summary

A subobject classifier in a [[category|A2DE66937D]] with finite limits is an object $\Omega$ with a morphism $\top \colon 1 \to \Omega$.
Every [[subobject|FS1FKAE89H]] of every object $X$ must be the pullback of $\top$ along exactly one morphism $X \to \Omega$.
In the category of sets, $\Omega = \set{0, 1}$ and the morphism $X \to \Omega$ of a subset is its [[characteristic function|0V5B6D6BQH]].
It is one of the defining features of a [[topos|6837RS7N82]], and $\Omega$ plays the role of the object of truth values.
In a sheaf topos, $\Omega$ need not have two elements, and its internal logic is in general [[intuitionistic|Q11N8X99FK]].

## Explanations

### L1 human

In sets, a subset $A \subseteq X$ is the same as a yes/no question on $X$: "is $x$ in $A$?".
A subobject classifier is an object $\Omega$ of answers that makes this work in another category.
For example, in sheaves on a space $X$, the answers over an open set $U$ are the open subsets of $U$.
The truth value of "$s = t$" for two sections is the open set where they agree.
So truth values come in many shades, not just true and false.
