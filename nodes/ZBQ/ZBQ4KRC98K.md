---
tag: ZBQ4KRC98K
kind: concept
name: Cartan matrix of an algebra
msc: [16G10, 20C20]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_matrix
---

## Summary

The Cartan matrix of a finite-dimensional algebra records how the simple modules occur as composition factors of the indecomposable [[projective modules|BFFA03GE3V]].
Its rows are indexed by the indecomposable projectives and its columns by the [[simple modules|G00C22AEDH]].
In the modular representation theory of finite groups it is a basic invariant of the group algebra.
It is a different notion from the Cartan matrix of a semisimple Lie algebra, which shares the name.

## Explanations

### L1 human

Over a finite-dimensional algebra, every module is built in layers from simple modules, like a number is built from primes.
The projective modules are the most important building blocks, and each one has a top simple module.
The Cartan matrix is the table that counts how often each simple module appears in the layers of each indecomposable projective module.
For the algebra $K[x]/(x^2)$ there is one simple module and the only indecomposable projective has two layers, so the Cartan matrix is $(2)$.
For a semisimple algebra the projectives are simple and the Cartan matrix is the identity matrix.
