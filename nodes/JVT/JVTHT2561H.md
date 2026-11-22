---
tag: JVTHT2561H
kind: proof
name: Proof that the nonzero rows of an echelon form are a basis of the row space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 1JGMW9DM4Z
uses: [E4GKK727ZM, 0EP73HK4C4, 0F27PBRWD7, 0HR573CHNM, 0VTQTPQGAV, 05G2G0P224]
methods: [0NTF6DMVAP, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Proof

We use the theorem on row equivalence for the row space, and then we read a vanishing combination of the nonzero rows at the pivot columns, from the top down.
Let $u_1, \dots, u_r$ be the nonzero rows of $U$, from top to bottom, and let the pivot of $u_k$ be in column $p_k$.

1. By part 3 of the [[theorem on row equivalence|E4GKK727ZM]], $\operatorname{Row}(A) = \operatorname{Row}(U)$, which proves part 1.
2. By the [[definition of the row space|0EP73HK4C4]], $\operatorname{Row}(U)$ is the [[span|0HR573CHNM]] of all rows of $U$, and a zero row adds nothing to a span, so $u_1, \dots, u_r$ span $\operatorname{Row}(U)$.
3. By the definition of [[row echelon form|0F27PBRWD7]], $p_1 < p_2 < \dots < p_r$, and every entry of $u_k$ to the left of column $p_k$ is $0$.
4. So for $k > j$, entry $p_j$ of $u_k$ is $0$, because $p_j < p_k$.
5. Let $c_1 u_1 + \dots + c_r u_r = 0$ with $c_k \in F$; we show $c_j = 0$ for each $j$ by induction on $j$.
6. Let $j \ge 1$ and assume $c_1 = \dots = c_{j-1} = 0$, so that $c_j u_j + \dots + c_r u_r = 0$.
7. Entry $p_j$ of this sum is $c_j (u_j)_{p_j}$, because by step 4 the rows $u_k$ with $k > j$ contribute $0$ there.
8. So $c_j (u_j)_{p_j} = 0$, and the pivot $(u_j)_{p_j}$ is nonzero, so $c_j = 0$, since a field has no zero divisors.
9. By induction all $c_j$ are $0$, so $u_1, \dots, u_r$ are linearly independent.
10. By steps 2 and 9, $u_1, \dots, u_r$ form a [[basis|0VTQTPQGAV]] of $\operatorname{Row}(U) = \operatorname{Row}(A)$, which proves part 2.
11. Each nonzero row of $U$ holds exactly one pivot, so the number of pivots is $r$, and the definition of [[dimension|05G2G0P224]] gives $\dim \operatorname{Row}(A) = r$, which proves part 3.

## Idea

Row operations can be undone, so they keep the row space.
In echelon form the nonzero rows have a staircase shape: each pivot sits in a column where all lower rows are zero.
In a combination that is zero, look at the first pivot column: only the first row is nonzero there, so its coefficient must vanish.
Then repeat with the next pivot column, and the coefficients die one by one.

## Variants

The induction can be replaced by a triangular submatrix.
The $r \times r$ submatrix of $U$ in rows $1, \dots, r$ and columns $p_1, \dots, p_r$ is upper triangular with the pivots on its diagonal, so it is invertible.
A vanishing combination of $u_1, \dots, u_r$ gives a vanishing combination of the rows of this invertible submatrix, so all coefficients are $0$.

For the reduced row echelon form the check is shorter.
The pivots are $1$, and the other entries of each pivot column are $0$, so entry $p_j$ of $\sum_k c_k u_k$ is exactly $c_j$.
