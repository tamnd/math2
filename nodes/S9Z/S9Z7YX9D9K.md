---
tag: S9Z7YX9D9K
kind: concept
name: Genetic algebra
msc: [17D92, 92D10]
specializes: [A6HRHW6CBY]
sources:
  - url: https://en.wikipedia.org/wiki/Genetic_algebra
same_as:
  wikidata: Q5532873
  wikipedia: Genetic algebra
---

## Summary

A genetic algebra is a commutative, usually nonassociative, algebra with a special triangular basis, used to model the inheritance of genes.
Every genetic algebra is a [[baric algebra|A6HRHW6CBY]], and the triangular form of its multiplication makes the long-run behaviour of the population under random mating computable.
The study of algebras of this kind was started by Ivor Etherington around 1939.
The term is also used more loosely for the whole family of algebras of mathematical genetics, such as train, [[Bernstein|S8GFADSZ7M]] and [[evolution algebras|DNK00D7M6F]].

## Explanations

### L1 human

Take one gene with two variants $A$ and $a$.
A population is a vector $pA + qa$ of frequencies, and the product of two populations gives the frequencies of the offspring of random mating between them.
Mendel's rules give $A \cdot A = A$, $a \cdot a = a$ and $A \cdot a = \tfrac12(A + a)$.
This product is commutative but not associative, and in the basis $A, A - a$ it has a triangular form.
That triangular form is what makes the algebra genetic.
