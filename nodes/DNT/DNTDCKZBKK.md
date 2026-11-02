---
tag: DNTDCKZBKK
kind: concept
name: Monadic functor
msc: [18C15, 18C20]
sources:
  - url: https://en.wikipedia.org/wiki/Monad_(category_theory)
---

## Summary

A functor $U \colon \mathcal{D} \to \mathcal{C}$ is monadic when it has a left adjoint and $\mathcal{D}$ is, up to equivalence, the category of algebras of the resulting [[monad|FF6XXA6D1A]].
So the objects of $\mathcal{D}$ are exactly objects of $\mathcal{C}$ with algebraic structure described by the monad.
The forgetful functors from groups, rings, modules and compact Hausdorff spaces to sets are monadic.
Beck's monadicity theorem characterizes monadic functors.

## Explanations

### L1 human

A forgetful functor forgets structure, for example it sends a group to its underlying set.
It is monadic when the forgotten structure can be fully recovered as a way of evaluating formal expressions.
Groups are monadic over sets: a group is a set with a consistent way to evaluate words in its elements.
Topological spaces are not monadic over sets, since a topology is not an algebraic structure of this kind.
