---
tag: DTBK11SR77
kind: topic
name: Determinants
msc: ["15A15"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]], and it studies one number attached to a square matrix: the determinant.
That number answers two questions at once.
It says whether the matrix is invertible, and it says by what factor the matrix changes areas and volumes, with a sign for orientation.
The topic starts with the formula $ad - bc$ for a $2 \times 2$ matrix and with the rule of Sarrus for size $3$, which fails for size $4$.
To go further, it takes the axiomatic view: the determinant is the only function of the columns that is linear in each column, vanishes when two columns are equal, and gives $1$ on the identity.
From these three rules come the Leibniz formula over permutations, the effect of row operations, the product rule $\det(AB) = \det A \det B$ and the invertibility test.
Minors and cofactors lead to the Laplace expansion, the adjugate, the explicit inverse and Cramer's rule.
Block matrices, the Vandermonde determinant, the Cauchy-Binet formula and the identities of Sylvester type extend the toolbox.
The topic ends with the meaning of the determinant: an invariant of a linear map, a measure of volume, the sign of an orientation, its derivative and its square root for alternating matrices.
Later topics use the determinant to define the characteristic polynomial of a matrix and to study eigenvalues.

## Remarks

### Reading order

1. [[Determinant of a 2 × 2 matrix|0ZN2J42SK7]]: you compute $ad - bc$, read it as a signed area, and use it to test invertibility.
2. [[Rule of Sarrus|7H2P40X0MV]]: you compute $3 \times 3$ determinants with the six diagonals and see why the scheme fails for $4 \times 4$.
3. [[Alternating multilinear map|0K6CH0MT0F]]: you meet the kind of function that the determinant is, and learn that such functions of $n$ vectors in $F^n$ form a space of dimension $1$.
4. [[Determinant|00KDZRW4C0]]: you see the general definition by three rules and why the three standard definitions agree.
5. [[Leibniz formula|016PE4VZ8Q]]: you expand the determinant as a signed sum of $n!$ products, one for each permutation.
6. [[Multilinearity of the determinant in rows|0PPG793642]]: you use linearity in each row, and you see that the determinant of a sum is not the sum of the determinants.
7. [[Determinant with equal rows or a zero row|0K4VQB7HWR]]: you recognize at a glance three kinds of matrix whose determinant is $0$.
8. [[Effect of row operations on the determinant|09YB3WQG38]]: you track how a swap, a scaling and a row addition change the determinant.
9. [[Determinant of a triangular matrix|0K1KKMFHYH]]: you multiply the diagonal entries, and you compute any determinant by row reduction.
10. [[Determinant of the transpose|0ZZQ2E1MTE]]: you learn that columns and rows play the same role.
11. [[Multiplicativity of the determinant|04CPJ6AF00]]: you prove $\det(AB) = \det A \det B$ in two ways.
12. [[Determinant of the inverse|0783S9D0ZH]]: you get $\det(A^{-1}) = 1 / \det A$ and see that similar matrices have equal determinants.
13. [[Invertible iff the determinant is nonzero|FBSAPTP1PR]]: you get the main test for invertibility over a field.
14. [[Determinants over commutative rings|03Q7RE2HXR]]: you see that invertibility over a ring needs a unit determinant, as for integer matrices with determinant $\pm 1$.
15. [[Minor|0BT9BYWVRY]]: you take determinants of square submatrices, such as the leading principal minors.
16. [[Cofactor|0XPKR18APA]]: you attach a sign from the checkerboard pattern to each minor.
17. [[Laplace expansion|0C08BQ3M05]]: you expand a determinant along any row or column, and by complementary minors.
18. [[Adjugate matrix|07W9H8QF38]]: you build the transposed matrix of cofactors and learn its rank.
19. [[The identity A adj A = det A · I|0528HKWZ1Z]]: you prove the identity behind the explicit inverse, over any commutative ring.
20. [[Inverse via the adjugate|0ENVM493VK]]: you write $A^{-1}$ as $\operatorname{adj} A / \det A$ and see why unimodular integer matrices have integer inverses.
21. [[Cramer's rule|0977KZ6PQB]]: you solve $Ax = b$ by quotients of determinants and compare its cost with elimination.
22. [[Determinant of a block triangular matrix|0J9TVTNB4K]]: you multiply the determinants of the diagonal blocks, and you see that the $2 \times 2$ formula fails for general blocks.
23. [[Determinant via the Schur complement|0KA7A4ENVJ]]: you reduce a block determinant to smaller ones through an invertible block.
24. [[Vandermonde determinant|0P84B554AS]]: you prove that the determinant of powers is the product of the differences, the fact behind polynomial interpolation.
25. [[Cauchy-Binet formula|08WE2W7DYS]]: you expand the determinant of a product of rectangular matrices as a sum over minors.
26. [[Weinstein-Aronszajn identity|0G24VQ1088]]: you trade $\det(I_m + AB)$ for $\det(I_n + BA)$, which can be much smaller.
27. [[Matrix determinant lemma|0BC3Q6K92H]]: you update a determinant after a rank one change in one step.
28. [[Sylvester's determinant identity|7SSKBQYFW1]]: you relate the determinants of bordered minors, with the Desnanot-Jacobi identity as the smallest case.
29. [[Dodgson condensation|RQ44FKS5QM]]: you compute a determinant by repeated $2 \times 2$ minors and learn when the method breaks down.
30. [[Rank by minors|HVHQ50TJB1]]: you find the rank of a matrix as the size of its largest nonzero minor.
31. [[Determinant of a linear map|0X0HQYSZ0K]]: you see that every matrix of an endomorphism has the same determinant.
32. [[Determinant of a family of vectors in a basis|05CJSSXPR3]]: you measure a family of vectors against a basis and test whether it is a basis.
33. [[Determinant as volume scaling factor|RC5BTSG8T2]]: you read $\lvert \det A \rvert$ as the volume of the image of the unit cube.
34. [[Orientation of a real vector space|0QJJAQ6ZYZ]]: you learn what the sign of the determinant means, through right-handed and left-handed bases.
35. [[Jacobi's formula|357FEAZ0Q4]]: you differentiate the determinant and find that its derivative at the identity is the trace.
36. [[Pfaffian|NH5HWBPWS9]]: you meet a polynomial whose square is the determinant of an alternating matrix.

### Prerequisites

- [[Sign of a permutation|02DKV69ZH0]]: the sign that appears in the Leibniz formula.
- [[Invertible matrices and matrix factorizations|P8J6QR66TJ]]: elementary matrices and inverses, used in the proofs by row reduction.
- [[Matrices of linear maps, rank and change of basis|S6559D61BP]]: the matrix of a linear map, similarity and rank.

### Where the determinant returns

The next topic, [[eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]], defines the characteristic polynomial as $\det(xI - A)$.
In [[isometries and the orthogonal and unitary groups|AZS5BPF5H3]], the sign of the determinant separates rotations from reflections.
