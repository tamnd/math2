---
tag: 6PBS6KW0NC
kind: concept
name: Torsion submodule
msc: [13C12, 13C05]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_(algebra)
---

## Summary

Let $M$ be a module over a commutative ring $R$.
Its torsion submodule is the set of elements of $M$ that are killed by some non-zero-divisor of $R$.
It is a [[submodule|05WDSN597C]] of $M$, and it measures how far $M$ is from being torsion-free.
For $R = \Z$ it is the [[torsion subgroup|0DBWXQRXQJ]] of an [[abelian group|082GHNPJ53]].
Over a [[principal ideal domain|0CMD0BCH8T]], a finitely generated module splits as its torsion submodule plus a free module.

## Explanations

### L1 human

Think of the elements of a module that "vanish after scaling" by a harmless scalar.
A harmless scalar is one that is not a zero divisor, such as a nonzero integer.
These elements form the torsion part, and dividing them out leaves a torsion-free module.
For example, in the abelian group $\Z \oplus \Z/6\Z$, the element $(0, 1)$ is torsion because $6 \cdot (0, 1) = 0$.
The element $(1, 0)$ is not torsion, because $n \cdot (1, 0) = (n, 0) \ne 0$ for every $n \ne 0$.
