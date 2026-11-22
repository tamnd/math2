---
tag: 1D4JTZ9VS3
kind: topic
name: Inner product spaces
msc: ["15A63"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]], and it gives a vector space the geometry of lengths, angles and right angles.
It starts from the dot product of $\mathbb{R}^n$ and keeps only three of its properties: linearity, symmetry and positivity.
Over $\mathbb{C}$ symmetry becomes conjugate symmetry, and in math2 a complex inner product is linear in the first slot and conjugate-linear in the second, as in most mathematics books, while physics books and Mathlib use the other order.
From the three axioms come the induced norm, the Cauchy-Schwarz and triangle inequalities, and the parallelogram law, which tells exactly which norms come from an inner product.
The polarization identity shows that the norm alone determines the inner product.
Orthogonality then leads to orthonormal families and bases, in which coordinates are inner products and lengths are sums of squares, as Bessel's inequality and Parseval's identity make precise.
The Gram-Schmidt process builds an orthonormal basis from any basis, so every finite-dimensional inner product space looks like $\mathbb{R}^n$ or $\mathbb{C}^n$ with the standard inner product.
The topic ends with the Gram matrix, which tests independence and measures volume, and with the Riesz representation of linear forms.
The later topics on orthogonal projections, adjoints and the spectral theorems build on all of this.

## Remarks

### Reading order

1. [[Inner product|0NB0AWGJBW]]: you learn the three axioms, why complex vectors need a conjugate, and the inner products on matrices and polynomials.
2. [[Inner product space|0QVNCJXRY3]]: you see that the inner product is part of the data, so one vector space can carry two different geometries.
3. [[Norm induced by an inner product|0MFJJV97RJ]]: you measure lengths and distances by $\sqrt{\ip{x}{x}}$ and turn any nonzero vector into a unit vector.
4. [[Cauchy-Schwarz inequality|0RFWW56Y22]]: you bound $\abs{\ip{x}{y}}$ by $\norm{x}\norm{y}$, which makes angles possible, and you meet two proofs.
5. [[Triangle inequality for the induced norm|SRN4T2G6AM]]: you prove that the induced norm is a norm and find when the inequality is an equality.
6. [[Parallelogram law|026HPGYGS4]]: you learn the identity that decides which norms come from an inner product, and see the maximum norm fail it.
7. [[Polarization identity|05FKHRT0B4]]: you recover the inner product from the norm, and conclude that maps which keep lengths also keep inner products.
8. [[Orthogonal vectors|0Y2X7P2WB7]]: you test right angles by $\ip{x}{y} = 0$ and see that the answer depends on the inner product.
9. [[Pythagorean theorem in an inner product space|0BVTDM872V]]: you add squared lengths of orthogonal vectors and see why the converse fails over $\mathbb{C}$.
10. [[Orthonormal family|0RW9TNNT87]]: you work with unit vectors at right angles and prove that they are always independent.
11. [[Orthonormal basis|0S9GGTR0EX]]: you recognize orthonormal bases, including the columns of matrices with $Q^* Q = I$.
12. [[Coordinates in an orthonormal basis|09DZ8CD1AK]]: you find coordinates as inner products, $v = \sum_i \ip{v}{e_i} e_i$, the model of Fourier coefficients.
13. [[Bessel's inequality|0RBT5PB74K]]: you see that the squared coordinates along an orthonormal family never exceed $\norm{v}^2$.
14. [[Parseval's identity|047RFCNVSK]]: you compute inner products and norms from coordinates in an orthonormal basis.
15. [[Gram-Schmidt process|0VT6P0GNQR]]: you turn any independent family into an orthonormal one with the same spans, and meet the Legendre polynomials.
16. [[Existence of an orthonormal basis|0Y85GYEGSF]]: you learn that every finite-dimensional inner product space has an orthonormal basis, and that each orthonormal family extends to one.
17. [[Gram matrix|00SPJSDT3Z]]: you collect the inner products of a family in a matrix that tests independence and whose determinant is a squared volume.
18. [[Riesz representation theorem in finite dimensions|04GYPXDXNH]]: you write each linear form as $\ip{\cdot}{u}$ and see that $u$ depends conjugate-linearly on the form over $\mathbb{C}$.

### Prerequisites

- [[Overview and vectors in the plane and in space|VKVAJ94SKZ]]: the dot product, lengths and angles in $\mathbb{R}^2$ and $\mathbb{R}^3$.
- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]]: bases, dimension and the extension of an independent set to a basis.
- [[Dual spaces and duality|9K7FFF26QR]]: linear forms and the dual space, used for the Riesz representation.
- Complex numbers with their conjugates and moduli, and determinants for the Gram matrix.
