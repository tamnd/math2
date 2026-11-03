---
tag: Q14JS2MA1C
kind: concept
name: K0 of a ring
msc: [19A49, 13D15, "16E20"]
specializes: [5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

The group $K_0(R)$ of a ring $R$ is the [[Grothendieck group|5FDMY7PDYY]] of [[finitely generated projective modules|HQA9YHDSH5]] over $R$ under direct sum.
It is the first group of [[algebraic K-theory|5GVFZWMWC8]].
It measures how far finitely generated projective modules are from being free.
For a field or a local ring it is $\Z$, and for a [[Dedekind domain|7NPY2CN5KB]] it is $\Z$ plus the [[ideal class group|WQ46BD3ARY]].

## Explanations

### L1 human

Over a field, every finitely generated module is a vector space, and its dimension says everything about it.
Over other rings there are projective modules that are not free, and the dimension is no longer enough.
The group $K_0(R)$ collects all finitely generated projective modules, adds them by direct sum, and allows formal differences.
Two modules give the same element when they become isomorphic after adding the same module.
So $K_0(R)$ is a coarse but computable record of all projective modules over $R$.
