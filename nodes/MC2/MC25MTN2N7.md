---
tag: MC25MTN2N7
kind: concept
name: Relational clone
msc: [08A40, 08A02]
sources:
  - url: https://en.wikipedia.org/wiki/Clone_(algebra)
---

## Summary

A relational clone on a set $A$ is a set of finitary relations on $A$ that is closed under primitive positive definitions.
It must also contain the equality relation and the empty relation.
Primitive positive definitions are those that use only conjunction, existential quantification and equality.
Relational clones are dual to [[clones|PTKR703G6A]] of operations.
On a finite set, the operators $\operatorname{Pol}$ and $\operatorname{Inv}$ give a bijection between them.
Another common name is co-clone.

## Explanations

### L1 human

A relational clone is a family of relations that is closed under the simplest ways of building new relations from old ones.
One may combine relations with "and", hide some coordinates with "there exists", and identify coordinates with "equals".
For example, from the order $\le$ on a set one can define $\set{(x, z) : \exists y \, (x \le y \wedge y \le z)}$, and a relational clone containing $\le$ contains this relation too.
The set of all relations preserved by a fixed set of operations is always a relational clone.
