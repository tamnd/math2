---
tag: 0N4XY7Z3NN
kind: concept
name: Upper triangular matrix
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: school
specializes: [0JXZKX526R]
uses: [0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Properties
  - url: https://en.wikipedia.org/wiki/Triangular_matrix
    locator: Algebras of triangular matrices
inventory: [1W8C1QV0S3]
---

## Summary

An upper triangular matrix is a [[square matrix|0JXZKX526R]] whose entries below the main diagonal are $0$: $u_{ij} = 0$ for $i > j$.
The [[formal definition|0MKABWDRNC]] also defines the strictly upper triangular matrices, with $u_{ij} = 0$ for $i \ge j$.
A [[lower triangular matrix|00J3KZP8Y0]] has zeros above the diagonal, and its transpose is upper triangular; this page treats both through the upper case.
A [[product of upper triangular matrices|~16a77e22]] is upper triangular, and its diagonal is the product of the diagonals.
A [[strictly upper triangular matrix is nilpotent|~0f948644]].
Triangular matrices are the end point of elimination, and every complex matrix is [[similar to one|0363JMQ42Y]].

## Motivation

Gaussian elimination turns a system $Ax = b$ into $Ux = c$ with $U$ upper triangular.
The last equation of $Ux = c$ has one unknown, the one before has two, and so on.
So we solve it by [[back substitution|0ATFVE08MW]] from the bottom up.
Triangular matrices also keep the flag of subspaces $\langle e_1 \rangle \subset \langle e_1, e_2 \rangle \subset \cdots$, which is the reason products stay triangular.

## Notation

- Upper triangular matrices are often written $U$ or $R$, and lower triangular ones $L$, as in $A = LU$ and $A = QR$.
- A *unitriangular* matrix is triangular with all diagonal entries $1$.
- In Mathlib, `Matrix.BlockTriangular M id` expresses that `M` is upper triangular; it is bound to the general [[triangular matrix|GTG8MJGDKC]] page.

## Remarks

### Examples

- [[A product of two 3 × 3 upper triangular matrices|~1091bcac]], with the diagonal $2, 4, 18$.
- [[A strictly upper triangular 3 × 3 matrix of index 3|~9021d76b]].
- Diagonal matrices are upper and lower triangular.
- The Jordan block $\begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$ is upper triangular.

### Non-examples

- [[The product of an upper and a lower triangular matrix|~23722604]] need not be triangular.
- A rectangular $2 \times 3$ matrix is not triangular in this sense, although row echelon forms are sometimes called upper trapezoidal.

### Basic properties

- Sums, scalar multiples and products of upper triangular matrices of order $n$ are upper triangular, so they form a subring of $M_n(R)$.
- The diagonal of $UV$ is $(u_{11} v_{11}, \dots, u_{nn} v_{nn})$, by the [[product theorem|~16a77e22]].
- A strictly upper triangular $N$ of order $n$ satisfies $N^n = 0$, by the [[nilpotency theorem|~0f948644]].
- The transpose of an upper triangular matrix is lower triangular, so each fact has a lower triangular twin.
- The [[determinant|0K1KKMFHYH]] is the product of the diagonal entries, and $U$ is [[invertible|7X1B65CTG4]] over a field exactly when no diagonal entry is $0$; the inverse is again upper triangular.
- Over a field, the diagonal entries are the [[eigenvalues|0BQAA2BK3Q]], with multiplicity.

### History

- The factorisation $A = LU$ into triangular factors goes back to the elimination methods of Gauss; Turing analysed its rounding errors in 1948.

### Common errors

- Reading "triangular" as "zero diagonal"; the diagonal of an upper triangular matrix is arbitrary.
- Multiplying an upper and a lower triangular matrix and expecting a triangular result.
- Taking the diagonal entries of a non-triangular matrix as its eigenvalues.

## Explanations

### L1 human

An upper triangular matrix has zeros below the diagonal, so its nonzero entries form a triangle in the upper right corner.
Systems with such a matrix are easy to solve from the last equation upwards.
Multiplying two such matrices gives another one.

### L2 human

The matrix $U$ is upper triangular exactly when $Ue_j$ is a combination of $e_1, \dots, e_j$ for each $j$.
So $U$ maps each subspace $V_j = \langle e_1, \dots, e_j \rangle$ into itself, and a composite of such maps does the same.
On the quotient $V_j / V_{j-1}$, the map $U$ acts as multiplication by $u_{jj}$, which explains the diagonal rule.

### L3 human

The invertible upper triangular matrices form the Borel subgroup $B$ of $GL_n(F)$, the stabiliser of the standard flag.
The strictly upper triangular matrices form a nilpotent Lie algebra, and the unitriangular ones form a nilpotent group.
For $n \ge 2$, the ring of upper triangular matrices over a field is not semisimple; its strictly upper part is its Jacobson radical.
