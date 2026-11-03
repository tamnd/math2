---
tag: ARMX1P0X0S
kind: concept
name: Batalin–Vilkovisky algebra
msc: [17B63, 81T70, "16E45"]
specializes: [GJPPS5N213]
sources:
  - url: https://en.wikipedia.org/wiki/Batalin%E2%80%93Vilkovisky_formalism
---

## Summary

A Batalin–Vilkovisky algebra, or BV algebra, is a graded commutative algebra with an operator $\Delta$ of degree $-1$.
The operator squares to zero and is a differential operator of order at most two.
The failure of $\Delta$ to be a derivation defines a bracket, and this bracket makes the algebra a [[Gerstenhaber algebra|GJPPS5N213]].
BV algebras come from the Batalin–Vilkovisky formalism for gauge theories in physics.
They also appear in topology and algebra.
Examples are the homology of the free loop space of a closed oriented manifold and the Hochschild cohomology of some algebras.

## Explanations

### L1 human

On $\R^n$, the divergence is a natural operator on vector fields, and it extends to multivector fields, which can be multiplied by the wedge product.
It does not obey the product rule, and the amount by which it fails is the Schouten–Nijenhuis bracket, which extends the bracket of vector fields.
A BV algebra is an algebraic version of this picture, extended to multivector fields with a sign rule.
The operator $\Delta$ plays the role of the divergence, and applying it twice gives zero.
Its failure to respect products produces a Lie-type bracket that is compatible with the product.
