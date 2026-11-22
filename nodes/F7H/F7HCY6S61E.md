---
tag: F7HCY6S61E
kind: proof
name: Proof that the pivot columns form a basis of the column space
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
proves: 11CSKXQNG3
uses: [0F0RPPJ2TT, 0HR573CHNM, FCM29NQ6DN, E4GKK727ZM, 0NNR68BFRY, 0BCMGDHZGR, 0PDVQEP0ZC, 0VTQTPQGAV, 05G2G0P224]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.3
---

## Proof

We show that the columns of $A$ and of its reduced form satisfy the same linear relations, and then we read the relations in the reduced form.
Write $a_1, \dots, a_n$ for the columns of $A$.

1. For $x \in F^n$, the definition of the [[matrix-vector product|0PDVQEP0ZC]] gives $Ax = x_1 a_1 + \dots + x_n a_n$.
2. So $\{Ax : x \in F^n\}$ is the set of linear combinations of the columns, which is their [[span|0HR573CHNM]] and hence $\operatorname{Col}(A)$ by the [[definition|0F0RPPJ2TT]].
3. A span is a subspace, and this proves part 1.
4. By the [[theorem on row reduction|FCM29NQ6DN]], $A$ is row equivalent to a matrix $R$ in [[reduced row echelon form|0NNR68BFRY]]; let $r_1, \dots, r_n$ be its columns and $p_1 < \dots < p_r$ its [[pivot columns|0BCMGDHZGR]].
5. Row equivalent matrices have the same null space, by part 4 of the [[theorem on row equivalence|E4GKK727ZM]], so $Ax = 0$ exactly when $Rx = 0$.
6. By step 1, this says that $\sum_j x_j a_j = 0$ exactly when $\sum_j x_j r_j = 0$, so the columns of $A$ and of $R$ satisfy the same linear relations.
7. In $R$ the pivot of row $k$ is $1$ and the rest of its column is $0$, so $r_{p_k} = e_k$, the $k$-th standard unit vector of $F^m$, for $1 \le k \le r$.
8. For independence, let $\sum_{k=1}^r x_{p_k} a_{p_k} = 0$ and put $x_j = 0$ for the other $j$.
9. By step 6, also $\sum_{k=1}^r x_{p_k} e_k = 0$, so every $x_{p_k}$ is $0$, and the pivot columns of $A$ are linearly independent.
10. For spanning, note that the rows of $R$ below row $r$ are zero, so step 7 gives, for each column of $R$,
$$r_j = \sum_{k=1}^r R_{kj}\, e_k = \sum_{k=1}^r R_{kj}\, r_{p_k}.$$
11. This is a linear relation among the columns of $R$, so by step 6 the same relation holds in $A$:
$$a_j = \sum_{k=1}^r R_{kj}\, a_{p_k} \quad \text{for each } j.$$
12. So every column of $A$ lies in the span of the pivot columns of $A$, and that span is $\operatorname{Col}(A)$.
13. By steps 9 and 12, the pivot columns of $A$ form a [[basis|0VTQTPQGAV]] of $\operatorname{Col}(A)$, which proves part 2.
14. This basis has $r$ vectors, so the definition of [[dimension|05G2G0P224]] gives $\dim \operatorname{Col}(A) = r$, the number of pivot positions, which proves part 3.

The pivot positions are the same in every row echelon form of $A$, since they are the positions of the pivots of the unique reduced form, so part 2 holds for any echelon form.

## Idea

Row operations keep the null space, and the null space is exactly the list of linear relations among the columns.
So row operations keep every relation among the columns, even though they move the columns themselves.
In the reduced form the relations can be read off: the pivot columns are unit vectors, and each other column is a combination of them with its own entries as coefficients.
We then read the same relations back in $A$.

## Variants

The [[pivot test for independence|55K7JBE13G]] gives step 9 at once, applied to the matrix of the pivot columns, and the [[pivot test for spanning|D3PN42EP4X]] is the related criterion for the whole space $F^m$.
A second proof uses maps.
The invertible matrix $E$ with $R = EA$ gives an isomorphism $y \mapsto Ey$ of $F^m$ that sends $\operatorname{Col}(A)$ onto $\operatorname{Col}(R)$ and $a_j$ to $r_j$.
An isomorphism sends a basis to a basis, and $e_1, \dots, e_r$ is a basis of $\operatorname{Col}(R)$, so $a_{p_1}, \dots, a_{p_r}$ is a basis of $\operatorname{Col}(A)$.
