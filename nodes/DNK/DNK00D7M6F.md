---
tag: DNK00D7M6F
kind: concept
name: Evolution algebra
msc: [17D92, 17D99]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_algebra
---

## Summary

An evolution algebra is an algebra with a special basis.
Distinct basis vectors multiply to zero, and each basis vector squares to a linear combination of basis vectors.
Such algebras model non-Mendelian, asexual inheritance: each basis vector is a type, and its square lists the types of its offspring.
They are always commutative, but in general neither associative nor power-associative.
They belong to the family of algebras of mathematical genetics, next to [[baric|A6HRHW6CBY]] and [[genetic algebras|S9Z7YX9D9K]].

## Explanations

### L1 human

Imagine organisms of a few types that reproduce on their own, with no mating between different types.
Put one basis vector for each type, and declare that two different types have product zero, because they never meet.
The square of a type is the mix of types among its offspring, with nonnegative coefficients in a probabilistic model.
For example, with types $e_1, e_2$ and $e_1^2 = e_2$, $e_2^2 = e_1$, each type produces only offspring of the other type.
The structure is then a graph or a Markov chain written as an algebra.
