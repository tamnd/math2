---
tag: 128WX7HXAT
kind: definition
name: Additive category
msc: ["18E05"]
defines: B2VP96NJSK
uses: [SC6FD5F4J0, AQET9YHH6F, BZEJKTQ76T, 0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Additive_category
---

## Definition

An *additive category* is a [[preadditive category|SC6FD5F4J0]] $\mathcal{C}$ such that:

1. $\mathcal{C}$ has a [[zero object|AQET9YHH6F]];
2. every two objects $X_1, X_2$ of $\mathcal{C}$ have a [[biproduct|BZEJKTQ76T]] $X_1 \oplus X_2$.

## Remarks

Then every finite family of objects has a biproduct, and a morphism $\bigoplus_{j} X_j \to \bigoplus_{i} Y_i$ is the same as a matrix $(f_{ij})$ with $f_{ij} \colon X_j \to Y_i$, composed by matrix multiplication.
Being additive is a property of the underlying category: the addition of morphisms is determined by the biproducts, through $f + g = \nabla \circ (f \oplus g) \circ \Delta$, where $\Delta$ is the diagonal and $\nabla$ the codiagonal.

Example: the category of left [[modules|0NZ8JA25WK]] over a ring $R$ is additive.
The zero module is a zero object, and the direct sum $M_1 \oplus M_2$ is a biproduct.

Non-example: the ring $\Z$, as a preadditive category with one object $\ast$, is not additive.
It has no zero object, since a zero object $Z$ has $\Hom(Z, Z) = \set{0}$, while $\Hom(\ast, \ast) = \Z$.
