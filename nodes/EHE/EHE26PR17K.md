---
tag: EHE26PR17K
kind: statement
role: theorem
name: Hermite normal form
msc: [15B36, 15A21, 11C20]
uses: [R6RBQHW191, 0F27PBRWD7, 0EB9N0S33C]
about: [R6RBQHW191]
sources:
  - url: https://en.wikipedia.org/wiki/Hermite_normal_form
same_as:
  wikidata: Q13650324
  wikipedia: Hermite normal form
---

## Statement

Let $A$ be an $m \times n$ matrix with integer entries.
Say that an $m \times n$ integer matrix $H = (h_{ij})$ is in *Hermite normal form* if:

1. the nonzero rows of $H$ come before the zero rows;
2. the first nonzero entry of each nonzero row, its pivot, is positive and lies strictly to the right of the pivot of the row above;
3. the entries below each pivot are $0$;
4. each entry $h$ above a pivot $p$ in the same column satisfies $0 \le h < p$.

Then there is a [[unimodular|R6RBQHW191]] $m \times m$ integer matrix $U$, that is, one with $\det U = \pm 1$, such that $UA$ is in Hermite normal form.
The matrix $H = UA$ is unique.

## Remarks

The proof is integer Gaussian elimination.
The Euclidean algorithm on a column, by unimodular row operations, leaves the gcd of the entries in the pivot position and zeros below it.
Then the entries above each pivot are reduced modulo the pivot.
Uniqueness holds because the rows of $H$ are a special basis of the lattice spanned by the rows of $A$, and this basis is determined by the lattice.

Example: for $A = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix}$, subtract $3$ times row $1$ from row $2$ to get $\begin{pmatrix} 2 & 4 \\ 0 & -4 \end{pmatrix}$.
Negate row $2$ and subtract it from row $1$ to get $H = \begin{pmatrix} 2 & 0 \\ 0 & 4 \end{pmatrix}$, which satisfies all four conditions.

Without condition 4 the form is not unique: $\begin{pmatrix} 2 & 4 \\ 0 & 4 \end{pmatrix}$ is also a [[row echelon form|0F27PBRWD7]] of $A$ reachable by unimodular operations.
Some authors use the column version, $AU = H$ with $U$ unimodular of size $n \times n$ and $H$ lower triangular.

## Explanations

### L1 human

The Hermite normal form is the integer analogue of the reduced row echelon form.
Only operations that can be undone over the integers are allowed: swapping rows, negating a row, and adding an integer multiple of one row to another.
The result is a staircase-shaped matrix with a fixed choice of the entries above the pivots, and it is unique.

### L2 human

Two integer matrices have the same Hermite normal form exactly when their rows span the same lattice in $\Z^n$.
So the form solves the membership problem for lattices and gives a canonical basis.
It is used to solve linear Diophantine systems, to compute with ideals in number fields, and in integer programming.
Unlike the [[Smith normal form|MV28Z5N9XX]], it uses only row operations, and it keeps the row space.
