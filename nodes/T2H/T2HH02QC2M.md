---
tag: T2HH02QC2M
kind: concept
name: Commutator of a ring
msc: [17A01, 17B60]
sources:
  - url: https://en.wikipedia.org/wiki/Commutator
    locator: Ring theory
---

## Summary

The commutator of two elements $x, y$ of a ring or algebra is $[x, y] = xy - yx$.
It is zero exactly when $x$ and $y$ commute, so it measures the failure of [[commutativity|099E72KTF8]].
In an [[associative algebra|3CTW1P4HBP]] the commutator is a Lie bracket, and this turns every associative algebra into a [[Lie algebra|WCJYA7CJ83]].
It is the ring analogue of the [[commutator of two group elements|0PXW0BN7DW]].

## Explanations

### L1 human

The commutator compares the two orders of a product: first $x$ then $y$, and first $y$ then $x$.
For numbers the two orders agree and the commutator is $0$.
For matrices they often differ.
With $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, one gets $[E, F] = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$.
