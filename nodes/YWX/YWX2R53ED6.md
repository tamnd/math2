---
tag: YWX2R53ED6
kind: concept
name: Trace form
msc: [12F10, "11E04", 11R29]
sources:
  - url: https://en.wikipedia.org/wiki/Field_trace
---

## Summary

The trace form of a finite extension $L/K$ is the [[symmetric bilinear form|0AXZNE5XNH]] $(x, y) \mapsto \mathrm{Tr}_{L/K}(xy)$ on $L$, built from the [[field trace|WPE5Z53QYJ]].
It is [[nondegenerate|01NHFZF2SK]] exactly when $L/K$ is separable.
Its Gram determinant in a basis is the [[discriminant|3BCYVS9E17]] of that basis.
Over $\Q$ the trace form is a quadratic form whose signature counts the real embeddings of a number field.

## Explanations

### L1 human

The trace turns each element of $L$ into an element of $K$.
Applying it to products $xy$ gives a way to pair two elements of $L$ and get a number in $K$, like a dot product.
For $\Q(i)$ over $\Q$, the pairing of $a + bi$ with $c + di$ is $2(ac - bd)$.
In characteristic $p$ this pairing can vanish completely, and that happens exactly for inseparable extensions.
