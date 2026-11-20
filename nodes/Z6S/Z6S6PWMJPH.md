---
tag: Z6S6PWMJPH
kind: topic
name: Diagonalization, triangularization and invariant subspaces
msc: ["15A20", "15A18"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]].
It covers invariant subspaces, the conditions for an endomorphism to be diagonalizable, triangularization, simultaneous diagonalization, generalized eigenspaces, the kernel lemma, and the Jordan-Chevalley decomposition.

## Remarks

### Reading order

1. [[Invariant subspace|0ACX5QT8TE]]: subspaces with $T(U) \subseteq U$, such as kernels and images of polynomials in $T$, and the block triangular matrix.
2. [[Restriction and quotient operators|0KN7EPH7Z0]]: $T|_U$ and the induced map on $V / U$, whose characteristic polynomials multiply to $p_T$.
3. [[Diagonalizable matrix|07SQCNV233]]: $A = P D P^{-1}$ with eigenvectors as the columns of $P$.
4. [[Diagonalizable iff there is a basis of eigenvectors|056SW1E0AC]]: equivalently, $V$ is the direct sum of the eigenspaces.
5. [[Distinct eigenvalues imply diagonalizable|0Y95Z7MT02]]: a sufficient condition that is not necessary.
6. [[Diagonalizability test by multiplicities|CDB8KCNNG9]]: $p_T$ splits and each geometric multiplicity equals the algebraic one.
7. [[Minimal polynomial criterion|0MPAJRB23T]]: $T$ is diagonalizable exactly when $m_T$ splits with simple roots.
8. [[Defective matrix|5F2AV5855Y]]: the shear, nonzero nilpotent matrices and real rotations.
9. [[Eigendecomposition|D0AP2R7272]]: $A = Q \Lambda Q^{-1}$ and the spectral sum of projections.
10. [[Powers of a diagonalizable matrix|0TNR9BQ871]]: $A^k = P D^k P^{-1}$, Fibonacci numbers and long-term behaviour.
11. [[Simultaneous diagonalization|0FK17N4DKA]]: commuting diagonalizable maps share an eigenbasis.
12. [[Triangularization|0363JMQ42Y]]: $T$ is triangularizable exactly when $p_T$ splits, through flags of invariant subspaces.
13. [[Simultaneous triangularization|42PG67Q5YN]]: commuting matrices over $\C$ share a triangular basis.
14. [[Kernels lemma|ACBNK1VFVG]]: $\ker (p q)(T) = \ker p(T) \oplus \ker q(T)$ for coprime $p$ and $q$.
15. [[Primary decomposition theorem|49ZHBMYKVE]]: the splitting of $V$ along the factorization of $m_T$.
16. [[Generalized eigenvector|01H6QKWGDH]]: vectors killed by a power of $T - \lambda$, and Jordan chains.
17. [[Generalized eigenspace|0AJ035ZTZE]]: $\ker (T - \lambda)^n$, whose dimension is the algebraic multiplicity.
18. [[Decomposition into generalized eigenspaces|0Z3GDY89T5]]: $V = \bigoplus_\lambda V_\lambda$ when $p_T$ splits, and $T = D + N$.
19. [[Nilpotent endomorphism|063D5Z2C70]]: $T^n = 0$, a strictly upper triangular form, and $p_T = t^n$.
20. [[Semisimple endomorphism|08VRX3Q4PB]]: every invariant subspace has an invariant complement, and $m_T$ is squarefree.
21. [[Jordan-Chevalley decomposition|011K11VPJN]]: $T = S + N$ with commuting semisimple and nilpotent parts that are polynomials in $T$.
22. [[Fitting decomposition|77SACA9CVQ]]: $V = \ker T^n \oplus \operatorname{im} T^n$, with a nilpotent part and an invertible part.

### Prerequisites

- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: eigenvalues, eigenspaces, multiplicities, the Cayley-Hamilton theorem and the minimal polynomial.
- [[Direct sums, complements and quotient spaces|QHKTJ89V6S]]: direct sums of subspaces, projections and quotient spaces.
- [[Determinants|DTBK11SR77]]: this topic uses the determinant of triangular and block triangular matrices.
