---
tag: 7NTVTHC7CG
kind: concept
name: K1 of a C*-algebra
msc: [46L80, 19K99]
specializes: [DQZ8S67ZE6]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Summary

$K_1(A)$ is an abelian group attached to a [[C*-algebra|M2WFY1D3SZ]] $A$.
It is built from [[unitary elements|KK9S67F8CA]] of matrix algebras over the unitization of $A$, counted up to homotopy.
It measures how many essentially different ways a unitary can fail to be connected to the identity.
For $A = C(X)$ with $X$ compact Hausdorff, it is the topological K-group $K^1(X)$.

## Explanations

### L1 human

A unitary is the algebra version of a rotation, and two unitaries are counted as the same when one can be deformed into the other through unitaries.
Unitaries of different sizes are compared by padding them with the identity.
On the circle, the function $z \mapsto z$ is a unitary of $C(\mathbb{T})$ that winds once around $0$.
It cannot be deformed to the constant $1$, and its winding number gives $K_1(C(\mathbb{T})) \cong \Z$.
For a matrix algebra $M_n(\C)$, the unitary group is connected, so $K_1(M_n(\C)) = 0$.
