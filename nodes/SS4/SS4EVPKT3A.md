---
tag: SS4EVPKT3A
kind: topic
name: Positive definite matrices and the singular value decomposition
msc: ["15A18", "15A23", "15B48"]
topics: [GN8GYSDZFX]
---

## Summary

A symmetric matrix $A$ gives a quadratic form $x^{\mathsf{T}} A x$, and the first question about a form is whether it is positive at every nonzero vector.
This part of [[linear algebra|GN8GYSDZFX]] starts from that question.
Matrices that pass are the positive definite ones, and matrices whose form is only at least $0$ are the positive semidefinite ones.
Three tests decide the question: the signs of the eigenvalues, the signs of determinants of corners by Sylvester's criterion, and a factorization $A = B^* B$.
Each test gives a tool.
Elimination gives the Cholesky factor, the spectral theorem gives a unique positive square root, and the square root of $A^* A$ splits any square matrix into a rotation times a stretch, the polar decomposition.
The stretch factors are the singular values, and they lead to the singular value decomposition $A = U \Sigma V^*$, which holds for every rectangular matrix.
The decomposition shows that a matrix maps the unit sphere onto an ellipsoid.
It also gives the Moore-Penrose inverse, which solves least squares for any matrix, and the best approximation by matrices of low rank.
Throughout, matrices are finite and real or complex.

## Remarks

### Reading order

1. [[Positive definite matrix|0KX66CZMBB]] and its [[definition|0QQCG3JWJ4]]: what it means for a form to be positive, and where such matrices come from.
2. [[Positive semidefinite matrix|01MMVW8CKC]] and its [[definition|0880F9EQCP]]: the weaker condition that covariance matrices and Gram matrices satisfy.
3. [[Eigenvalue test for definiteness|0HYC2RHD3M]]: how to read definiteness from the signs of the eigenvalues.
4. [[Gram matrices are positive semidefinite|0AM050KCAW]]: why every $B^* B$ is positive semidefinite, and why every positive semidefinite matrix has this form.
5. [[Sylvester's criterion|0WKEF78PMV]]: a test by determinants, and why semidefiniteness needs all principal minors.
6. [[Cholesky decomposition|0WKG8CYY6A]]: how to factor a positive definite matrix as $L L^*$ by elimination.
7. [[Square root of a positive semidefinite matrix|EQ98KW1ZN4]]: how to compute the unique positive semidefinite square root from the eigenvalues.
8. [[Polar decomposition|0J2C7BDJQA]]: how to write a square matrix as a unitary matrix times a positive semidefinite one, and when the factors are unique.
9. [[Singular value|09VMDSRXWJ]], its [[definition|0K2TX12X58]], and [[singular values, rank and the operator norm|6VXM1T8PG7]]: what the stretch factors of a matrix are, and how they give the rank and the norm.
10. [[Singular value decomposition|000NPTMX6J]]: the factorization $A = U \Sigma V^*$ of every matrix, and how to compute it.
11. [[Geometry of the singular value decomposition|JAEKA59DNZ]]: the picture of the unit circle going to an ellipse.
12. [[Moore-Penrose inverse|0YY8VX28JR]], its [[definition|0PSRCMCM5X]], and [[the pseudoinverse from the SVD|Q9YN0F60ZW]]: the four conditions, and the shortest least-squares solution of any system.
13. [[Eckart-Young-Mirsky theorem|JJT6GC055J]]: why cutting the SVD after $k$ terms gives the best rank $k$ approximation, in the operator norm and in the Frobenius norm.
14. [[Simultaneous diagonalization with a positive definite matrix|K559AQ9H67]]: how to diagonalize two forms at once when one of them is positive definite.

### Prerequisites

- [[Inner product spaces|1D4JTZ9VS3]]: inner products, norms, orthonormal bases and the Gram-Schmidt process.
- [[Determinants|DTBK11SR77]]: determinants, minors and their product rule, used in Sylvester's criterion.
- [[Orthogonal complements, projections and least squares|8GQVME4SZZ]]: projections and the least-squares problem that the pseudoinverse solves.
- [[Adjoints, normal operators and the spectral theorems|3YM9EK6VMB]]: the spectral theorem for Hermitian matrices, which the eigenvalue test, the square root and the SVD use.
- [[Isometries and the orthogonal and unitary groups|AZS5BPF5H3]]: unitary and orthogonal matrices, the rotation factors in the polar decomposition and the SVD.
