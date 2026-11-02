---
tag: KGTA7KGP3C
kind: concept
name: Injective algebra
msc: [08B30, 18G05]
sources:
  - url: https://en.wikipedia.org/wiki/Injective_object
---

## Summary

An algebra in a class of algebras is injective when every homomorphism into it from a subalgebra extends to the whole algebra.
It is the universal-algebra form of an injective object, with embeddings in the role of monomorphisms.
In the variety of abelian groups the injective algebras are the divisible groups, and in modules they are the [[injective modules|85H7PRHDPZ]].
Injective algebras and injective hulls are tools for embedding algebras into well-behaved ones.

## Explanations

### L1 human

An injective algebra is a target that never blocks an extension.
If a map is defined on part of a bigger algebra, it can always be extended to all of it.
For example, any homomorphism from the subgroup $\Z$ of the rational numbers into $\Q$ extends to a homomorphism from $\Q$ to $\Q$: $n \mapsto nq$ extends to $x \mapsto xq$.
The group $\Z$ itself is not injective: the identity map $\Z \to \Z$ has no extension to $\Q$.
