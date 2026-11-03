---
tag: TZAZ163QGK
kind: concept
name: Representation of a Lie algebra
msc: [17B10]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_representation
same_as:
  wikidata: Q1136782
  wikipedia: Lie algebra representation
---

## Summary

A representation of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$ realises the elements of $\mathfrak{g}$ as linear maps of a [[vector space|000AYPA9AJ]].
In it, the bracket becomes the commutator of linear maps.
Equivalently, it is a $\mathfrak{g}$-module, or a module over the [[universal enveloping algebra|SCZ8PRVY00]] of $\mathfrak{g}$.
The derivative of a [[representation of a Lie group|7JA7WH92K0]] is a representation of its Lie algebra.
Representations of Lie algebras are central in Lie theory and in quantum physics.

## Explanations

### L1 human

A Lie algebra comes with a bracket $[x, y]$, but its elements need not be matrices.
A representation turns each element into a matrix, in a way that sends the bracket to $AB - BA$.
The same Lie algebra can be represented on spaces of many dimensions.
For example, the Lie algebra of vectors in $\R^3$ with the cross product acts on $\R^3$ by $v \mapsto (w \mapsto v \times w)$.
This works because $u \times (v \times w) - v \times (u \times w) = (u \times v) \times w$.
