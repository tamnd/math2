---
tag: JWMTXQ8A3A
kind: concept
name: Lie ideal
msc: [17B05]
specializes: [WKSSTQ69AK]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Summary

An ideal of a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak g$ is a linear subspace $\mathfrak a$ with $[x, a] \in \mathfrak a$ for all $x \in \mathfrak g$ and $a \in \mathfrak a$.
Ideals are exactly the kernels of [[Lie algebra homomorphisms|H5D71JE8TA]], and they are the subspaces by which one can form quotient Lie algebras.
They play the role of normal subgroups in group theory.
A Lie algebra with no ideals other than $0$ and itself, and not abelian, is called simple.

## Explanations

### L1 human

An ideal is a subspace that absorbs brackets with anything.
Bracket an element of the ideal with any element of the whole algebra, and you land back in the ideal.
For example, in the Lie algebra of all $n \times n$ matrices, the matrices of trace zero form an ideal.
The reason is that every commutator $AB - BA$ has trace zero.
Because of this property, the quotient by an ideal is again a Lie algebra.
