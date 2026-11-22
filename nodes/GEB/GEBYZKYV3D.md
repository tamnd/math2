---
tag: GEBYZKYV3D
kind: topic
name: Canonical forms under similarity
msc: ["15A21", "15A20"]
topics: [GN8GYSDZFX]
---

## Summary

Two square matrices are similar when they describe the same linear map in two different bases, and this part of [[linear algebra|GN8GYSDZFX]] asks how to tell whether that happens.
The answer is a canonical form: one chosen matrix in each similarity class, so that two matrices are similar exactly when they have the same form.
The story starts with a single vector $v$ and the subspace spanned by $v, Tv, T^2 v, \dots$, on which $T$ acts by a companion matrix.
Treating $T$ as multiplication by $x$ turns the space into a module over the polynomial ring, and the structure of such modules splits the space into cyclic pieces.
The monic polynomials that label these pieces are the invariant factors, and the block diagonal matrix of their companion matrices is the rational canonical form, which exists over every field.
They can be computed by row and column operations on $xI - A$, without finding a single eigenvalue.
When the characteristic polynomial splits into linear factors, the cyclic pieces can be cut further into Jordan blocks, and the result is the Jordan normal form.
Over a field where it does not split, such as $\mathbb{Q}$ or $\mathbb{R}$, the Jordan form may not exist, and the rational form or the real Jordan form takes its place.
The last pages look at the Weyr form, the matrices that commute with a given one, the classification problem as a whole, and the count of conjugacy classes in a finite general linear group.

## Remarks

### Reading order

1. [[Cyclic subspace and cyclic vector|42MMQBTP0M]]: the smallest invariant subspace that contains a given vector, and how to test whether one vector generates the whole space.
2. [[Companion matrix|0ZCWPNZTQ3]]: the matrix of a map on a cyclic subspace, whose characteristic and minimal polynomials are both read off its last column.
3. [[An endomorphism as a module over the polynomial ring|KGVTFBZX59]]: why similar matrices are the same thing as isomorphic modules, which brings the theory of modules into play.
4. [[Cyclic decomposition theorem|R3Z20J19BR]]: how every space splits into cyclic subspaces whose annihilators divide one another.
5. [[Invariant factors and elementary divisors|F7GJPMVBXA]]: the two lists of polynomials that decide similarity, and how to pass from one list to the other.
6. [[Rational canonical form|042JWAR3Q0]]: one matrix of companion blocks in each similarity class, over any field.
7. [[Similarity via the characteristic matrix|92VZF0QRM8]]: a way to compute the invariant factors by the Smith normal form of $xI - A$, with no roots needed.
8. [[Similarity does not depend on the field|5PVFX89NM7]]: why two rational matrices that are similar over the complex numbers are already similar over the rationals.
9. [[A matrix is similar to its transpose|C708QKZPE6]]: a first application of the invariant factors, with an explicit symmetric matrix that does the job.
10. [[Jordan block|07PH4RX0X5]]: the building block of the Jordan form, its powers and its polynomials, and the convention with ones above the diagonal.
11. [[Normal form of nilpotent endomorphisms|Z2RTKWZZAZ]]: how a nilpotent map breaks into chains, and how the ranks of its powers fix the chain lengths.
12. [[Jordan normal form|085HQ5G5TE]]: the existence and uniqueness of the form when the characteristic polynomial splits, and what goes wrong when it does not.
13. [[Computing the Jordan form|7M1W0ZA49Q]]: the block sizes from kernel dimensions, a transition matrix from chains, and the check $AP = PJ$.
14. [[Real Jordan form|MPFT45RFGV]]: a real form for real matrices, with rotation-scaling blocks for each pair of complex eigenvalues.
15. [[Weyr canonical form|9XEA4VR8WP]]: a second form built from the same data, which suits questions about commuting matrices.
16. [[Matrices that commute with a given matrix|GXZGWZSJ2J]]: the dimension of the commuting algebra, and why for a cyclic matrix it consists of the polynomials in that matrix.
17. [[Classification of matrices up to similarity|H3E52HTEZ2]]: how the forms fit together, and why the same question for pairs of matrices has no comparable answer.
18. [[Conjugacy classes of the general linear group over a finite field|4FV9TDGWWH]]: the classes as rational canonical forms, and how to count them.

### Prerequisites

- [[Eigenvalues, the characteristic polynomial and the minimal polynomial|6R1D6QPY3S]]: the characteristic and minimal polynomials, and the Cayley-Hamilton theorem.
- [[Diagonalization, triangularization and invariant subspaces|Z6S6PWMJPH]]: invariant subspaces, generalized eigenspaces and the matrices that are not diagonalizable.
- [[Modules over a principal ideal domain|WKJXXX0DYG]]: needed for the module proofs, while the elementary proofs use only polynomial division and greatest common divisors.
