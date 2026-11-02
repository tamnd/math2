---
tag: DE2KEQ85ZT
kind: concept
name: Inverse limit of algebras
msc: [08B25, 18A30]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_limit
---

## Summary

The inverse limit of an inverse system of algebras is the algebra of all compatible families of elements.
Such a family has one element in each algebra of the system.
It is a subalgebra of the [[direct product|WJ73XYBNE4]] of the algebras.
It is the limit of the system in the category of algebras of the given signature.
Inverse limits build large algebras, such as the $p$-adic integers and profinite groups, out of a coherent family of smaller ones.

## Explanations

### L1 human

Picture a tower of algebras, each one mapping to the one below it by a [[homomorphism|KBXSZC6BV1]].
A point of the inverse limit is a choice of one element on every floor, such that each choice maps to the choice on the floor below.
For example, take the rings $\Z/2\Z$, $\Z/4\Z$, $\Z/8\Z$, and so on, with reduction maps between them.
A compatible family such as $(1, 3, 7, 15, \ldots)$ is an element of the inverse limit, which is the ring of $2$-adic integers.
