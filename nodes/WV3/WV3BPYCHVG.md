---
tag: WV3BPYCHVG
kind: concept
name: Forgetful functor
msc: ["18A22", "08C05"]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Forgetful_functor
same_as:
  wikidata: Q2646117
  wikipedia: Forgetful functor
---

## Summary

A forgetful functor sends a mathematical object to a less structured object by dropping some of its structure.
It sends each morphism to the same map, regarded in the poorer setting.
The basic example sends an algebra to its underlying set and a homomorphism to its underlying function.
Forgetful functors often have left adjoints, the [[free functors|N353JF8RBK]], and the pair produces a monad that encodes the algebraic theory.
They also make a category of algebras into a [[concrete category|ZD0GTPSJS1]].

## Explanations

### L1 human

A group is a set together with a multiplication.
Forgetting the multiplication leaves just the set, and a group homomorphism is still a function between the sets.
The forgetful functor from groups to sets is this act of forgetting, done for all groups and homomorphisms at once.
One can forget less: a ring can be sent to its additive group, forgetting only the multiplication.
