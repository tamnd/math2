---
tag: 36KSZ7GA5S
kind: concept
name: Matrix Lie group
msc: ["22E15", "22E60"]
specializes: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group
---

## Summary

A matrix Lie group is a closed subgroup of the [[general linear group|0FCHE902D7]] $GL_n(\C)$.
By the [[closed subgroup theorem|3NJGY8QSTE]], every matrix Lie group is a [[Lie group|7JBRGCVJRB]], and its Lie algebra can be computed with the [[matrix exponential|020M04FN1H]].
Most Lie groups met in practice, such as the orthogonal, unitary and symplectic groups, are matrix Lie groups.
So they are a common entry point to Lie theory.

## Explanations

### L1 human

A matrix Lie group is a set of invertible matrices that is closed under products and inverses.
It must also contain the limit of each convergent sequence of its elements, when that limit is invertible.
The rotation matrices of the plane form an example: products and inverses of rotations are rotations, and a limit of rotations is a rotation.
Working with matrices lets one do Lie theory with concrete calculations, using $e^A = I + A + A^2/2! + \cdots$ in place of abstract constructions.
Not every Lie group is of this kind, but the most important ones are.
