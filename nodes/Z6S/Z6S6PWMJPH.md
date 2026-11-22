---
tag: Z6S6PWMJPH
kind: topic
name: Diagonalization, triangularization and invariant subspaces
msc: ["15A20", "15A18"]
topics: [GN8GYSDZFX]
---

## Summary

A linear map on a large space is easier to understand when we can cut the space into pieces that the map keeps in place, and then study the map on each piece.
These pieces are the invariant subspaces, and they are the thread of this part of [[linear algebra|GN8GYSDZFX]].
The best case is a diagonalizable map, where the space splits into eigenspaces and the map only stretches each one, so that powers, exponentials and long-term behavior become arithmetic with numbers.
Not every map is so kind: the shear and the nonzero nilpotent maps have too few eigenvectors, and a rotation of the plane has no real ones at all.
For these maps there are weaker but still useful forms: a triangular matrix whenever the characteristic polynomial splits, and a splitting into generalized eigenspaces through the kernels lemma and the primary decomposition.
The story ends with the Jordan-Chevalley decomposition, which writes every such map as a diagonalizable part plus a commuting nilpotent part, and with the Fitting decomposition into a nilpotent piece and an invertible piece.
The sub-area on canonical forms then classifies the nilpotent parts, which leads to the Jordan normal form.

## Remarks

### Reading order: diagonalization

1. [[Invariant subspace|0ACX5QT8TE]]: what it means for a map to keep a subspace in place, and why this makes its matrix block triangular.
2. [[Restriction and quotient operators|0KN7EPH7Z0]]: how a map breaks into a map on the invariant subspace and a map on the quotient, with characteristic polynomials that multiply.
3. [[Diagonalizable matrix|07SQCNV233]]: how to write $A = P D P^{-1}$ with eigenvectors in the columns of $P$, and the shear as the first failure.
4. [[Diagonalizable iff there is a basis of eigenvectors|056SW1E0AC]]: the basic criterion, and its form as a direct sum of eigenspaces.
5. [[n distinct eigenvalues imply diagonalizable|0Y95Z7MT02]]: a quick sufficient test, and why the identity matrix shows that it is not necessary.
6. [[Diagonalizability test by multiplicities|CDB8KCNNG9]]: the complete test by algebraic and geometric multiplicities, and the algorithm that follows.
7. [[Minimal polynomial criterion|0MPAJRB23T]]: the test by simple roots of the minimal polynomial, which shows at once that projections are diagonalizable, and so are involutions outside characteristic $2$.
8. [[Defective matrix|5F2AV5855Y]]: a catalog of matrices without a basis of eigenvectors, and what goes wrong in each.
9. [[Eigendecomposition|D0AP2R7272]]: the factorization $A = Q \Lambda Q^{-1}$ read as a sum of eigenvalues times projections.
10. [[Powers of a diagonalizable matrix|0TNR9BQ871]]: $A^k = P D^k P^{-1}$, with the Fibonacci numbers and the long-term behavior of a linear recurrence.
11. [[Simultaneous diagonalization|0FK17N4DKA]]: when several maps share one eigenbasis, namely exactly when they are diagonalizable and commute.

### Reading order: beyond diagonalization

12. [[Triangularization|0363JMQ42Y]]: the triangular form that exists exactly when the characteristic polynomial splits, built from a flag of invariant subspaces.
13. [[Simultaneous triangularization|42PG67Q5YN]]: one triangular basis for a whole family of commuting complex matrices.
14. [[Kernels lemma|ACBNK1VFVG]]: the splitting $\ker (p q)(T) = \ker p(T) \oplus \ker q(T)$ for coprime $p$ and $q$, with projections that are polynomials in $T$.
15. [[Primary decomposition theorem|49ZHBMYKVE]]: the splitting of the whole space along the irreducible factors of the minimal polynomial.
16. [[Generalized eigenvector|01H6QKWGDH]]: the vectors that a power of $T - \lambda$ sends to zero, and the chains they form.
17. [[Generalized eigenspace|0AJ035ZTZE]]: the space $\ker (T - \lambda)^n$, whose dimension is always the algebraic multiplicity.
18. [[Decomposition into generalized eigenspaces|0Z3GDY89T5]]: the direct sum of the generalized eigenspaces when the characteristic polynomial splits, a step toward the Jordan form.
19. [[Nilpotent endomorphism|063D5Z2C70]]: the maps with a zero power, which are strictly upper triangular in a suitable basis.
20. [[Semisimple endomorphism|08VRX3Q4PB]]: the replacement for "diagonalizable" over any field, tested by a squarefree minimal polynomial.
21. [[Jordan-Chevalley decomposition|011K11VPJN]]: the unique split $T = S + N$ into commuting diagonalizable and nilpotent parts that are polynomials in $T$.
22. [[Fitting decomposition|77SACA9CVQ]]: the split $V = \ker T^n \oplus \operatorname{im} T^n$ into a nilpotent piece and an invertible piece.

### Prerequisites

- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: eigenvalues, eigenspaces, multiplicities, the Cayley-Hamilton theorem and the minimal polynomial.
- [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]: direct sums of subspaces, projections and quotient spaces.
- [[Determinants|DTBK11SR77]]: the determinant of triangular and block triangular matrices.
