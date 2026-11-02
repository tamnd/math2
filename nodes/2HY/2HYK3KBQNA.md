---
tag: 2HYK3KBQNA
kind: concept
name: Sheafification
msc: [18F20, 18F10]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_(mathematics)
---

## Summary

Sheafification turns a [[presheaf|AND2WHZC8P]] $P$ on a [[site|NYE0Z94MME]] into the closest [[sheaf|RT8A8FJ566]] $aP$.
It comes with a map $P \to aP$ through which every map from $P$ to a sheaf factors uniquely.
It is a functor that is [[left adjoint|TZHF6ZM92S]] to the inclusion of sheaves into presheaves, and it preserves finite limits.
It is how one builds sheaves such as cokernels, quotients and constant sheaves, which are not sheaves when computed objectwise.
On a small site it can be computed by applying the plus construction twice.

## Explanations

### L1 human

Some natural constructions give data that is defined locally but does not glue, so it is only a presheaf.
Sheafification repairs this: it forces local data that agree on overlaps to glue, and it identifies data that agree locally.
For example, on a space with two connected components, the constant presheaf with value $\Z$ has only constant functions, while its sheafification allows a different integer on each component.
