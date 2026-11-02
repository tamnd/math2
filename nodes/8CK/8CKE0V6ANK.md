---
tag: 8CKE0V6ANK
kind: concept
name: Approximation property
msc: [46B28]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_property
same_as:
  wikidata: Q621744
  wikipedia: Approximation property
---

## Summary

A Banach space has the approximation property when the identity operator can be approximated, uniformly on each compact set, by bounded operators of finite rank.
Grothendieck showed that this is equivalent to a statement on operators.
For every Banach space $Y$, every compact operator from $Y$ into the space is a norm limit of finite-rank operators.
Spaces with a Schauder basis, such as $\ell^p$ for $1 \le p < \infty$ and $c_0$, have the property.
[[Enflo's counterexample|ZKP5KGFWCK]] shows that some separable Banach spaces do not.

## Explanations

### L1 human

Finite-rank operators are the simplest operators: their values lie in a finite-dimensional space, so they are matrices in disguise.
The approximation property says that the identity map can be imitated by such operators on any compact set, up to any small error.
In $\ell^2$, the map that keeps the first $n$ coordinates of a sequence and replaces the rest by $0$ does this for $n$ large.
