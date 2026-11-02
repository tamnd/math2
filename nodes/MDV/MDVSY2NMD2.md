---
tag: MDVSY2NMD2
kind: concept
name: Gelfand–Kirillov dimension
msc: [16P90]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand–Kirillov_dimension
same_as:
  wikidata: Q5530427
  wikipedia: Gelfand–Kirillov dimension
---

## Summary

The Gelfand–Kirillov dimension of an algebra over a field is the exponent of the polynomial rate at which the algebra grows.
It is defined through the [[growth|EHY4PYSMGZ]] of finite-dimensional subspaces under multiplication, so it makes sense for noncommutative algebras.
For a finitely generated commutative algebra it equals the [[Krull dimension|MVGBS3J1P7]], and the $n$-th [[Weyl algebra|98QE7KY55W]] has Gelfand–Kirillov dimension $2n$.
It is a basic invariant in noncommutative ring theory and in the theory of $D$-modules.

## Explanations

### L1 human

Take a finite set of generators and look at all products of at most $n$ of them.
If the dimension of their span grows roughly like $n^d$, the algebra has Gelfand–Kirillov dimension $d$.
The polynomial ring in $d$ variables has dimension $d$, just like the space it describes.
An algebra whose span grows exponentially, like the free algebra on two letters, has infinite Gelfand–Kirillov dimension.
