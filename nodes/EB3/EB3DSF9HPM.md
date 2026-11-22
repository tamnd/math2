---
tag: EB3DSF9HPM
kind: proof
name: Proof of the invertibility criterion by row reduction
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: FBSAPTP1PR
methods: [0WCP0PVET6]
uses: [FCM29NQ6DN, F7F6AA3XQ7, 1ZK55FS2BF, 09YB3WQG38, 0K4VQB7HWR, 0WF5AQYTW6, 0ZZQ2E1MTE, 0Z4BWARC38]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Invertibility
---

## Proof

We row reduce $A$, follow the determinant through each operation, and look at the two possible end results.
Let $A$ be an $n \times n$ matrix over a field $F$, as in the [[theorem|FBSAPTP1PR]].

*Conditions 1 and 2.*

1. By the [[existence of the reduced row echelon form|FCM29NQ6DN]], a finite sequence of row operations turns $A$ into a matrix $R$ in [[reduced row echelon form|0WF5AQYTW6]].
2. Each operation is a swap of two rows, a scaling of a row by some $c \neq 0$, or the addition of a multiple of one row to another.
3. By the [[effect of row operations|09YB3WQG38]], these operations multiply the determinant by $-1$, by $c$, and by $1$.
4. So $\det R = \kappa \det A$, where $\kappa$ is a product of nonzero factors.
   Since $F$ is a field, $\kappa \neq 0$, and $\det A \neq 0$ if and only if $\det R \neq 0$.
5. If $R = I_n$, then $\det R = 1$ by the [[determinant of the identity|0Z4BWARC38]].
6. If $R \neq I_n$, then $R$ has fewer than $n$ pivots.
   The reason is that $n$ pivots in an $n \times n$ reduced matrix sit in different rows and columns, so they lie on the diagonal and $R = I_n$.
7. With fewer than $n$ pivots, some row of $R$ has no pivot.
   In reduced row echelon form such a row is zero, so $\det R = 0$ by the rule for a [[zero row|0K4VQB7HWR]].
8. By steps 4 to 7, $\det A \neq 0$ if and only if $R = I_n$.
9. By the [[criterion for invertibility by the reduced form|1ZK55FS2BF]], $R = I_n$ if and only if $A$ is invertible.
   So conditions 1 and 2 are equivalent.

*Conditions 1 and 3.*

10. By the same criterion, $A$ is invertible if and only if $Ax = 0$ has only the solution $x = 0$.
11. Write $c_1, \dots, c_n$ for the columns of $A$, so that
$$Ax = x_1 c_1 + x_2 c_2 + \dots + x_n c_n.$$
   So $Ax = 0$ has only the solution $x = 0$ exactly when the columns are linearly independent, and conditions 1 and 3 are equivalent.

*Conditions 2 and 4.*

12. The rows of $A$ are the columns of $A^{\mathsf{T}}$, and $\det A^{\mathsf{T}} = \det A$ by the [[transpose rule|0ZZQ2E1MTE]].
13. Steps 1 to 11 applied to $A^{\mathsf{T}}$ show that its columns are independent if and only if $\det A^{\mathsf{T}} \neq 0$.
   So the rows of $A$ are independent if and only if $\det A \neq 0$, and conditions 2 and 4 are equivalent.

Steps 9, 11 and 13 together prove that the four conditions are equivalent.

## Idea

Row operations multiply the determinant by nonzero numbers, so they never change whether it is zero.
At the end of row reduction there are only two outcomes.
Either we reach $I_n$, whose determinant is $1$, or we reach a matrix with a zero row, whose determinant is $0$.
The first outcome happens exactly for invertible matrices, and that settles the question.
Independence of columns is the same as a trivial kernel, and the transpose moves the argument from columns to rows.

## Variants

A second proof uses the [[adjugate|8A6WRWSGQZ]], and its main part works over every commutative ring.
The row reduction proof needs a field, since it divides by pivots, but it is also the practical test.
It decides invertibility and computes $\det A$ with about $n^3$ arithmetic operations, while the Leibniz sum has $n!$ terms.
