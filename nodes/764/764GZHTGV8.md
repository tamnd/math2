---
tag: 764GZHTGV8
kind: concept
name: Finitely presented algebra
msc: ["13E15", 13B02]
specializes: [AC5TFFQT9M]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_ring_theory
---

## Summary

An algebra $B$ over a commutative ring $A$ is finitely presented if it can be described by finitely many generators and finitely many relations.
That is, $B \cong A[x_1, \ldots, x_n]/I$ with $I$ a finitely generated ideal.
Over a Noetherian ring every [[finite type algebra|AC5TFFQT9M]] is finitely presented, so the distinction matters only over non-Noetherian bases.
Finite presentation is the right finiteness condition for limit arguments and for étale and smooth morphisms in algebraic geometry.

## Explanations

### L1 human

To describe a ring by a finite amount of data, one lists some generators and some polynomial equations between them.
For example, $\Z[i]$ is $\Z[x]/(x^2 + 1)$: one generator and one relation.
Finite type asks only for finitely many generators, while finite presentation also asks that finitely many equations imply all the others.
Over a ring like $\Z$ or a field, the second demand is automatic.
