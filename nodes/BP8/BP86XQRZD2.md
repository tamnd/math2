---
tag: BP86XQRZD2
kind: concept
name: K0 of a C*-algebra
msc: [46L80, 19K14]
specializes: [DQZ8S67ZE6]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Summary

$K_0(A)$ is an abelian group attached to a [[C*-algebra|M2WFY1D3SZ]] $A$.
It is built from projections in matrix algebras over $A$, counted up to [[Murray–von Neumann equivalence|GT9S7APKG1]].
The [[Grothendieck group|5FDMY7PDYY]] construction then makes them into a group.
For $A = C(X)$ with $X$ compact Hausdorff, it is the topological K-group $K^0(X)$ of vector bundles on $X$.
It is the first invariant of [[operator K-theory|DQZ8S67ZE6]] and a key tool in the classification of C*-algebras.

## Explanations

### L1 human

A projection in a matrix algebra is like a subspace, and its rank says how big the subspace is.
In a general C*-algebra, two projections count as equal when a partial isometry carries one onto the other.
Placing two projections side by side in a bigger matrix adds them, and formal differences of such classes form $K_0(A)$.
For the complex numbers, a projection matrix is determined up to equivalence by its rank, so $K_0(\C) \cong \Z$.
For the algebra of all bounded operators on an infinite-dimensional Hilbert space, every class cancels and $K_0$ is $0$.
