---
tag: SXVNJY4XFY
kind: concept
name: K1 of a ring
msc: [19B99, 19B14]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Summary

The group $K_1(R)$ of a ring $R$ is the abelianisation of the [[stable general linear group|G8R9561PXT]] $GL(R)$.
By Whitehead's lemma it is the quotient of $GL(R)$ by the [[elementary subgroup|E5JXB0E324]] $E(R)$.
It generalises the determinant: for a commutative ring the determinant induces a split surjection $K_1(R) \to R^\times$, and for a field this is an isomorphism.
It is the first of the [[algebraic K-groups|5GVFZWMWC8]] above $K_0$ and carries the Whitehead group used in topology.

## Explanations

### L1 human

Two invertible matrices count as the same in $K_1$ if row operations turn one into the other, after enlarging both with $1$s on the diagonal.
Only operations of the type "add a multiple of one row to another" are allowed.
For a field, what survives is exactly the determinant.
For more general rings, extra information can remain beyond the determinant.
For example, over the integers every invertible matrix reduces to $\mathrm{diag}(\pm 1, 1, \dots, 1)$, so $K_1(\Z)$ has two elements.
