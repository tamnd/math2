---
tag: QP92G4ZGJE
kind: concept
name: Deformation of algebras
msc: [16S80, "16E40"]
specializes: [SWFR1GD6QT]
sources:
  - url: https://en.wikipedia.org/wiki/Deformation_(mathematics)
---

## Summary

A deformation of an [[associative algebra|3CTW1P4HBP]] $A$ is a family of associative products on $A$ depending on a parameter $t$.
At $t = 0$ it gives back the original product.
In the formal theory of Murray Gerstenhaber, the parameter is a formal variable and the products are power series in $t$.
The first-order terms are classified by the second Hochschild cohomology of $A$, and the obstructions to extending them lie in the third.
Deformations of algebras are the algebraic core of [[deformation quantization|3MKSJ1J04K]].

## Explanations

### L1 human

Imagine changing the multiplication of an algebra a little bit, in a way controlled by a small parameter $t$.
At $t = 0$ one has the old algebra, and for small $t$ a nearby algebra.
For example, the commutative polynomial ring in $x$ and $y$ can be bent into an algebra where $yx = xy - t$, which is a Weyl algebra.
Some algebras cannot be bent at all except in trivial ways; they are called rigid.
The theory asks which bendings exist and when two of them are really the same after a change of coordinates.
