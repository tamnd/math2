---
tag: 9T2XVJNBBY
kind: concept
name: Entropic algebra
msc: [08A62, 20N02]
specializes: [QJGPT2W0FT]
sources:
  - url: https://en.wikipedia.org/wiki/Medial_magma
---

## Summary

An entropic algebra is an [[algebra|QJGPT2W0FT]] in which any two operations commute with each other.
Equivalently, every operation $A^n \to A$ is a [[homomorphism|KBXSZC6BV1]] of algebras from the power $A^n$ to $A$.
For an algebra with one binary operation this is the [[medial law|VZHN6GA3TA]].
Modules over a commutative ring, semilattices and affine spaces are entropic.
In an entropic variety, the homomorphisms from one algebra $A$ to another algebra $B$ form a subalgebra of the power $B^A$.

## Explanations

### L1 human

Fill a rectangle with elements, $n$ rows and $m$ columns.
Take two operations, one with $n$ arguments and one with $m$ arguments.
You can apply the second operation along each row and then the first to the results.
Or you can apply the first down each column and then the second to the results.
An algebra is entropic when these two ways always agree.
For a vector space this says, for instance, that $r(a + b) = ra + rb$ and $r(sa) = s(ra)$.
