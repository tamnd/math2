---
tag: N353JF8RBK
kind: concept
name: Free functor
msc: ["08C05", "18A40", "08B20"]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Free_object
---

## Summary

A free functor is a left adjoint to a [[forgetful functor|WV3BPYCHVG]].
It sends a set $X$ to the [[free algebra|GTS4DRRMZR]] on $X$ in a variety, together with the inclusion of $X$.
It sends a map of sets to the homomorphism that extends it.
The universal property of free algebras is exactly the statement that this assignment is left adjoint to forgetting.
The composite of the forgetful functor with the free functor is the monad whose algebras are the algebras of the variety.

## Explanations

### L1 human

Given a set of letters, the free group on them consists of all reduced words in the letters and their inverses.
A function between two sets of letters renames letters, and so it turns words into words; this is a group homomorphism.
The free functor is this construction, done for all sets and maps at once.
It is "free" because the words satisfy no relation beyond the group axioms, so every map from the letters into a group extends uniquely to a homomorphism.
