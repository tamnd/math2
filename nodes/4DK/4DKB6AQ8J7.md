---
tag: 4DKB6AQ8J7
kind: concept
name: Yoneda embedding
msc: [18A25, 18A22]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Yoneda_lemma
---

## Summary

The Yoneda embedding of a locally small [[category|A2DE66937D]] $\mathcal{C}$ is a [[functor|28NQ0KRHD3]] into presheaves.
It sends each object $A$ to its [[hom functor|VJXS8AK67E]] $\Hom(-, A)$, a [[presheaf|AND2WHZC8P]] on $\mathcal{C}$.
By the [[Yoneda lemma|D6DF1ARPVD]] it is fully faithful, so $\mathcal{C}$ is equivalent to a full subcategory of a category of presheaves.
This lets one study objects of any category through set-valued functors, where many constructions are easy.

## Explanations

### L1 human

Replace each object $A$ by the record of all arrows that end at $A$, one set for each possible starting object.
The Yoneda embedding says that this record loses nothing.
Two objects with matching records in a natural way are isomorphic, and arrows between objects are the same as natural maps between their records.
For a group $G$ seen as a one-object category, the record of the single object is $G$ itself with $G$ acting by multiplication, and this gives Cayley's theorem.
