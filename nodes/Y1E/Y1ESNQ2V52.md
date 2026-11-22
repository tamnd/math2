---
tag: Y1ESNQ2V52
kind: topic
name: Matrices and the operations on them
msc: ["15A99"]
topics: [GN8GYSDZFX]
---

## Summary

This topic is a part of [[linear algebra|GN8GYSDZFX]], and it turns the tables of numbers from elimination into objects that we can compute with.
A matrix is a rectangular array of entries from a field, or more generally from a commutative ring.
It starts as a way to store the coefficients of a system, and it ends as an algebra of its own, with sums, products and many named special shapes.

The first pages fix the language: rows, columns, the size $m \times n$, square matrices, and the two matrices that act like $0$ and $1$.
Matrices of one size add entry by entry and form a vector space.
The product is the heart of the topic.
We first multiply a matrix by a vector, which writes a whole system as one equation $Ax = b$.
Then we multiply two matrices, with the row-times-column rule that comes from composing linear maps.
This product is associative but not commutative, and a product of two nonzero matrices can be zero.
So the square matrices of one size form a ring, the matrix ring, whose center is the scalar matrices.

The second half is a gallery of shapes and operations that a first course uses all the time.
Diagonal and triangular matrices are the easy cases for products and powers.
The transpose turns rows into columns and reverses the order of a product, and it defines the symmetric and skew-symmetric matrices; the conjugate transpose does the same job over the complex numbers.
Block matrices let us multiply in pieces, and the trace is a number with the cyclic property $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.
The topic closes with matrices defined by an equation on their powers, nilpotent, idempotent and involutory, with commuting pairs, and with the matrix units $E_{ij}$ from which every matrix is built.
All of this returns in the next topics: [[invertible matrices and factorizations|P8J6QR66TJ]], [[determinants|DTBK11SR77]] and [[matrices of linear maps|S6559D61BP]].

## Remarks

### Reading order

1. [[Matrix|0VD9ZSWWJG]]: how to name the size, the rows, the columns and each entry, and when two matrices are equal.
2. [[Square matrix|0JXZKX526R]]: why equal numbers of rows and columns allow powers, and what the main diagonal is.
3. [[Zero matrix|0ZTKJJDGR7]]: the identity for addition, and why $AB = 0$ does not force $A = 0$ or $B = 0$.
4. [[Identity matrix|06DW9BAWB1]]: the identity for multiplication, whose columns are the standard basis vectors.
5. [[Matrix addition and scalar multiplication|0Y7H3SAVA1]]: why the matrices of one size form a vector space of dimension $mn$.
6. [[Matrix-vector product|0PDVQEP0ZC]]: how to compute $Ax$ by rows or as a combination of columns, and how a system becomes $Ax = b$.
7. [[Matrix multiplication|032Q9FB8MT]]: the row-times-column rule, its three other views, and why it matches composition.
8. [[Associativity of matrix multiplication|073E4XC016]]: why brackets in a product do not matter, proved by sums and by composition.
9. [[Noncommutativity of matrix multiplication|0P506SPZP2]]: a pair with $AB \neq BA$, and which school algebra rules this breaks.
10. [[Matrix ring|AB2MD5CD13]]: the ring $M_n(R)$, its center of scalar matrices, and its lack of two-sided ideals over a field.
11. [[Scalar matrix|067NKSBEWT]]: the matrices $\lambda I$, and why they are the only ones that commute with everything.

### Reading order, continued: special shapes and the transpose

12. [[Diagonal matrix|044JNC7ZAA]]: how products and powers work entry by entry, and how a diagonal factor scales rows or columns.
13. [[Upper and lower triangular matrices|0N4XY7Z3NN]]: why products stay triangular, and why strictly triangular matrices are nilpotent.
14. [[Transpose|09DXWYRD43]]: how rows become columns, the rules of the transpose, and the notations in books.
15. [[Transpose of a product|09GK5PS824]]: why $(AB)^{\mathsf{T}} = B^{\mathsf{T}} A^{\mathsf{T}}$ reverses the order, and how it gives the dot product as $x^{\mathsf{T}} y$.
16. [[Symmetric matrix|0VR671PHE5]]: the matrices with $A^{\mathsf{T}} = A$, and when a product of two of them is symmetric.
17. [[Skew-symmetric matrix|0PBY4E9GQF]]: the matrices with $A^{\mathsf{T}} = -A$, and how every square matrix splits into a symmetric and a skew-symmetric part.
18. [[Conjugate transpose|0DXKE10PHF]]: the complex version of the transpose, and why lengths of complex vectors need it.
19. [[Hermitian and skew-Hermitian matrices|0P17NGQQMQ]]: the complex analogues of symmetric matrices, and the decomposition $A = H + iK$.
20. [[Block matrix|0ASDFEQS6P]]: how to cut a matrix into blocks and multiply block by block.

### Reading order, continued: blocks, the trace and powers

21. [[Block diagonal matrix|001T5FJDC1]]: how a matrix made of separate square blocks computes powers and inverses one block at a time.
22. [[Trace of a matrix|0XC1RDBY7A]]: the sum of the diagonal entries, its linearity, and the inner product $\operatorname{tr}(A^{\mathsf{T}} B)$.
23. [[Cyclic property of the trace|0Y4NF1DRKD]]: why $\operatorname{tr}(AB) = \operatorname{tr}(BA)$, and why $AB - BA = I$ has no solution over the real numbers.
24. [[Nilpotent matrix|07BSPZPSMF]]: matrices with a zero power, and the finite geometric series for the inverse of $I - N$.
25. [[Idempotent matrix|0KCE8CG86P]]: matrices with $P^2 = P$, which are the projections, and why their trace is their rank.
26. [[Involutory matrix|NH2QE3671N]]: matrices with $A^2 = I$, which are the reflections, and their link with projections.
27. [[Commuting matrices|8G3X8MPG7E]]: pairs with $AB = BA$, and why the binomial theorem holds for them.
28. [[Matrix units|A4HTT7JFD1]]: the matrices $E_{ij}$, their product rule, and their use in proofs about the matrix ring.

### Prerequisites

1. [[Overview and vectors in the plane and in space|VKVAJ94SKZ]]: vectors, their sums and their dot products.
2. [[Systems of linear equations and row reduction|DXSXFVDMXQ]]: the coefficient matrix of a system and row operations.
3. [[Ring|0B1261B5ED]]: the axioms of a ring, for the matrix ring.
