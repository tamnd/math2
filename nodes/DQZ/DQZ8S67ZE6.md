---
tag: DQZ8S67ZE6
kind: concept
name: Operator K-theory
msc: [46L80, 19K99]
specializes: [ZT11JGCWX0]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
same_as:
  wikidata: Q7097836
  wikipedia: Operator K-theory
---

## Summary

Operator K-theory assigns to a [[C*-algebra|M2WFY1D3SZ]] $A$ two abelian groups $K_0(A)$ and $K_1(A)$.
The group $K_0(A)$ is built from projections in matrix algebras over $A$, and $K_1(A)$ from unitaries up to homotopy.
For the algebra $C(X)$ of continuous functions on a compact Hausdorff space $X$, it gives back the [[topological K-theory|6XCFW7YGX8]] of $X$.
It is a basic invariant in the classification of C*-algebras and in index theory.

## Explanations

### L1 human

A C*-algebra is an algebra of operators, like the algebra of $n \times n$ complex matrices.
Projections in it play the role of subspaces, and two projections count as the same when one can be moved onto the other by a partial isometry.
Adding projections side by side gives a sum, and formal differences turn this into the group $K_0$.
For the matrix algebra $M_n(\C)$, a projection is determined up to this equivalence by its rank, so $K_0(M_n(\C)) \cong \Z$.
The group $K_1$ records the ways a unitary cannot be connected to the identity.
