---
tag: 6R1D6QPY3S
kind: topic
name: Eigenvalues, the characteristic polynomial and the minimal polynomial
msc: ["15A18", "15A24"]
topics: [GN8GYSDZFX]
---

## Summary

A linear map usually turns vectors to new directions, but some vectors only get stretched, and the stretch factors are the eigenvalues.
This part of [[linear algebra|GN8GYSDZFX]] finds those special directions and the numbers that go with them.
It starts from the equation $Tv = \lambda v$ and turns it into a question about determinants: $\lambda$ is an eigenvalue exactly when $\det(\lambda I - A) = 0$.
That makes the characteristic polynomial the main tool, and its coefficients carry the trace and the determinant as the sum and the product of the eigenvalues.
The field matters throughout: a rotation of the real plane has no eigenvalue, while over the complex numbers every operator has one.
The second half puts the map itself into polynomials, which leads to the minimal polynomial and to the Cayley-Hamilton theorem, which says that every square matrix is a root of its own characteristic polynomial.
All of this prepares [[diagonalization and invariant subspaces|Z6S6PWMJPH]] and the [[canonical forms under similarity|GEBYZKYV3D]].

## Remarks

### Reading order

1. [[Eigenvalue|0BQAA2BK3Q]]: what it means for a map to act on a line as multiplication by one number, and why $0$ is an eigenvalue exactly for singular maps.
2. [[Eigenvector|0N6960W0BV]]: the invariant lines themselves, seen in rotations, projections, reflections and shears.
3. [[Eigenspace|0G0RFPG8HR]]: all eigenvectors for one eigenvalue at once, as the kernel of $T - \lambda I$, with a basis by row reduction.
4. [[Spectrum of a matrix|0XPX5NC67E]]: the set of eigenvalues, and how it changes when the field changes.
5. [[Characteristic polynomial|0VSSPAFM2C]]: the determinant $\det(tI - A)$ whose roots are the eigenvalues, and the other sign convention $\det(A - tI)$.
6. [[Characteristic polynomial of an endomorphism|C98TZ6ZAXC]]: why the polynomial does not depend on the basis, and how it splits for direct sums and block triangular matrices.
7. [[Eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]]: the link between the two definitions, and the bound of at most $n$ eigenvalues.
8. [[Computing eigenvalues and eigenvectors by hand|7JJE96MZQY]]: the full method on $2 \times 2$ and $3 \times 3$ matrices, with complex and triangular cases.
9. [[Coefficients of the characteristic polynomial|0FRYPZ6D0X]]: how to read the polynomial off principal minors, with the trace and the determinant at the two ends.
10. [[Trace is the sum of the eigenvalues|0NMXDCNNKR]]: a quick check on any eigenvalue computation, counted with multiplicity.
11. [[Determinant is the product of the eigenvalues|0C2F40MEBC]]: the companion check, and a second view of invertibility.
12. [[Eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]]: why different eigenvalues never share directions, so that the sum of eigenspaces is direct.
13. [[Algebraic multiplicity|0FY42N02DV]]: how often an eigenvalue appears as a root.
14. [[Geometric multiplicity|099TWVJ909]]: how many independent eigenvectors it has, and the defective eigenvalues where this is fewer.
15. [[Existence of an eigenvalue over an algebraically closed field|08CJB2NQ92]]: why every complex operator has an eigenvalue, with a proof that avoids determinants.
16. [[Invariant subspaces of dimension 1 or 2 for real operators|KAV44BRV77]]: what survives over the real numbers, including a real eigenvalue in odd dimension.
17. [[Eigenvalues of AB and BA|MCXV71BY74]]: why the two products share their nonzero eigenvalues even when they are different matrices.
18. [[Left eigenvector|32M8VY9A1M]]: eigenvectors that multiply from the left, their use in Markov chains, and their orthogonality to right eigenvectors.
19. [[Polynomial of an endomorphism|0E3MV6E6MG]]: how to put a map into a polynomial, and why $p(T)$ has the eigenvalues $p(\lambda)$.
20. [[Annihilating polynomial|0PBN8VEKY8]]: why some nonzero polynomial always kills a map in finite dimension.
21. [[Minimal polynomial|03NDVCSHSB]]: the smallest such polynomial, and how to compute it for projections, nilpotent and diagonal matrices.
22. [[Minimal polynomial divides every annihilating polynomial|0VTAD25A3G]]: the division argument that makes the minimal polynomial unique.
23. [[Eigenvalues are the roots of the minimal polynomial|0QF4ZEFG52]]: the same roots as the characteristic polynomial, proved without the Cayley-Hamilton theorem.
24. [[Cayley-Hamilton theorem|0F765KFC2J]]: every matrix satisfies its characteristic polynomial, with the adjugate proof and the reason the one-line proof is wrong.
25. [[Minimal polynomial divides the characteristic polynomial|093X6MN6Y6]]: the two polynomials have the same irreducible factors, which gives a finite search for the minimal one.
26. [[Inverse and powers by the Cayley-Hamilton theorem|R4CPYXFJEQ]]: how to write $A^{-1}$ and $A^k$ as short polynomials in $A$.

### Prerequisites

- [[Vector spaces, span, independence, bases and dimension|MVH97H8B2J]] and [[linear maps|9080WQTZ3M]]: subspaces, kernels and endomorphisms.
- [[Matrices and the operations on them|Y1ESNQ2V52]] and [[matrices of linear maps, rank and change of basis|S6559D61BP]]: matrix products, similar matrices and rank.
- [[Determinants|DTBK11SR77]]: the product rule, triangular matrices and the adjugate.
- [[Polynomial ring|0Q9EZS90GY]]: division with remainder and roots of polynomials.
