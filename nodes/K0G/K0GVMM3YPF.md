---
tag: K0GVMM3YPF
kind: concept
name: Dirac bundle
msc: [53C27, 58J60, 15A66]
sources:
  - url: https://en.wikipedia.org/wiki/Dirac_operator
---

## Summary

A Dirac bundle over a Riemannian manifold is a bundle of [[Clifford modules|31Q0RDPZ00]] with a metric and a connection that are compatible with Clifford multiplication.
These data are exactly what is needed to define a [[Dirac operator|3DXGJTEQZH]] that is formally self-adjoint and satisfies a general Bochner–Weitzenböck formula.
Spinor bundles, the bundle of differential forms and the Clifford bundle itself are Dirac bundles.
The notion gives one framework for the de Rham, signature, Dolbeault and spin Dirac operators used in index theory.

## Explanations

### L1 human

A Dirac operator needs three ingredients.
They are a way to multiply sections by tangent vectors with the Clifford rule, a way to measure lengths of sections, and a way to differentiate them.
A Dirac bundle is a vector bundle carrying all three, fitted together so that the multiplication preserves lengths and the differentiation respects both.
For example, differential forms with multiplication $v \cdot \omega = v^\flat \wedge \omega - \iota_v \omega$ form a Dirac bundle.
Its Dirac operator is $d + d^*$, the square root of the Hodge Laplacian.
