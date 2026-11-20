---
tag: 1D4JTZ9VS3
kind: topic
name: Inner product spaces
msc: ["15A63"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]].
It covers real and complex inner products on finite-dimensional spaces, the norm that they induce and its identities, orthonormal bases, and the Gram-Schmidt process.
It ends with the Gram matrix and with the Riesz representation of linear forms.
In this topic a complex inner product is linear in the first slot, as in most mathematics books.
Physics books and Mathlib use the second slot.

## Remarks

### Reading order

1. [[Inner product|0NB0AWGJBW]]: the axioms, the dot product, and the complex inner product with conjugates.
2. [[Inner product space|0QVNCJXRY3]]: a vector space with a chosen inner product, and the main examples.
3. [[Norm induced by an inner product|0MFJJV97RJ]]: the length $\sqrt{\ip{x}{x}}$ and the distance it defines.
4. [[Cauchy-Schwarz inequality|0RFWW56Y22]]: $|\ip{x}{y}| \leq \norm{x}\norm{y}$, with equality exactly for dependent vectors.
5. [[Triangle inequality for the induced norm|SRN4T2G6AM]]: the induced norm is a norm.
6. [[Parallelogram law|026HPGYGS4]]: the identity that singles out the norms that come from inner products.
7. [[Polarization identity|05FKHRT0B4]]: the norm determines the inner product.
8. [[Orthogonal vectors|0Y2X7P2WB7]]: $\ip{x}{y} = 0$, and the trap of the symmetric condition over $\mathbb{C}$.
9. [[Pythagorean theorem|0BVTDM872V]]: the converse holds over $\mathbb{R}$ and fails over $\mathbb{C}$.
10. [[Orthonormal family|0RW9TNNT87]]: unit vectors at right angles, which are always independent.
11. [[Orthonormal basis|0S9GGTR0EX]]: the standard basis and matrices with orthonormal columns.
12. [[Coordinates in an orthonormal basis|09DZ8CD1AK]]: $v = \sum_i \ip{v}{e_i} e_i$, the model of Fourier coefficients.
13. [[Bessel's inequality|0RBT5PB74K]]: the squared coordinates are at most $\norm{v}^2$.
14. [[Parseval's identity|047RFCNVSK]]: equality for an orthonormal basis.
15. [[Gram-Schmidt process|0VT6P0GNQR]]: from any independent family to an orthonormal one with the same spans.
16. [[Existence of an orthonormal basis|0Y85GYEGSF]]: every orthonormal family extends to an orthonormal basis.
17. [[Gram matrix|00SPJSDT3Z]]: invertible exactly for independent families, with the squared volume as determinant.
18. [[Riesz representation theorem in finite dimensions|04GYPXDXNH]]: each linear form is $\ip{\cdot}{u}$, and $u$ depends antilinearly on the form over $\mathbb{C}$.

### Prerequisites

- [[Overview and vectors in the plane and in space|VKVAJ94SKZ]]: the dot product, lengths and angles in $\mathbb{R}^2$ and $\mathbb{R}^3$.
- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]: bases, dimension and the extension of an independent set to a basis.
- [[Dual spaces and duality|9K7FFF26QR]]: linear forms and the dual space, used in row 18.
- Complex numbers, their conjugates and moduli. Row 17 also uses determinants.
