---
tag: GG03BSSZ43
kind: example
name: A basis of the null space of a 3 × 4 matrix from its free variables
msc: ["15A03", "15A06"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0PHDYNR24D]
illustrates: [5NKND0CPKP]
uses: [0PQ2GGY1QV, 0NNR68BFRY, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Computation by Gaussian elimination
  - book: isbn:9780321982384
    locator: Section 4.2
---

## Example

Each free variable of the reduced form gives one basis vector of the null space.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}, \qquad R = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{pmatrix},$$
where $R$ is the [[reduced row echelon form|0NNR68BFRY]] of $A$, found in the [[column space example|AGHYPF25CY]].

1. The [[pivot columns|0BCMGDHZGR]] are 1 and 3, and the free columns are 2 and 4, so we expect $n - r = 4 - 2 = 2$ basis vectors.
2. The system $Rx = 0$ reads $x_1 + 2x_2 + x_4 = 0$ and $x_3 + 2x_4 = 0$, so $x_1 = -2x_2 - x_4$ and $x_3 = -2x_4$.
3. Put $x_2 = 1$ and $x_4 = 0$; this gives $s_1 = (-2, 1, 0, 0)$.
4. Put $x_2 = 0$ and $x_4 = 1$; this gives $s_2 = (-1, 0, -2, 1)$.
5. Check with the original matrix, row by row:
$$A s_1 = (-2 + 2,\ -4 + 4,\ -6 + 6) = (0, 0, 0),$$
$$A s_2 = (-1 + 0 + 0 + 1,\ -2 + 0 - 2 + 4,\ -3 + 0 - 2 + 5) = (0, 0, 0).$$
6. The general solution of $Ax = 0$ is $t_1 s_1 + t_2 s_2 = (-2t_1 - t_2, t_1, -2t_2, t_2)$.
7. Its entries 2 and 4 are $t_1$ and $t_2$, so the combination is zero only for $t_1 = t_2 = 0$, and $s_1, s_2$ are independent.
8. So $s_1, s_2$ is a basis of the [[null space|0PQ2GGY1QV]], and $\dim \operatorname{Null}(A) = 2$.

## Remarks

The example shows that the null space and the column relations are the same information.
The vector $s_1$ says $-2a_1 + a_2 = 0$, that is, $a_2 = 2a_1$, and $s_2$ says $-a_1 - 2a_3 + a_4 = 0$, that is, $a_4 = a_1 + 2a_3$.
The pivot entries of each $s_l$ are the negatives of the entries of $R$ in the free column: column 4 of $R$ is $(1, 2, 0)$, and $s_2$ has $-1$ and $-2$ in positions 1 and 3.

Each $s_l$ is orthogonal to each row of $A$, for example $(2, 4, 1, 4) \cdot s_2 = -2 + 0 - 2 + 4 = 0$.
The rank $2$ and the nullity $2$ add up to the $4$ columns, as the [[rank-nullity theorem for matrices|TR48YQGCCA]] says.
If we change the corner entry $5$ to $6$, a third pivot appears in column 4, only $x_2$ stays free, and the null space shrinks to the line through $s_1$.

## Explanations

### L1 human

Two of the four unknowns can be chosen freely, and the other two then follow.
So the solutions of $Ax = 0$ form a flat plane inside four-dimensional space.
Choosing $1$ for one free unknown and $0$ for the other gives two solutions, and every solution is a mixture of these two.

### L2 human

The method has three moves: reduce, solve for the pivot variables, and set the free variables to the unit choices.
The typical use is to describe all solutions of $Ax = b$ as one solution plus the null space.
Watch out: a basis vector must have the $1$ in its own free position, and leaving it out gives a vector such as $(-2, 0, 0, 0)$, which is not a solution, since $A(-2, 0, 0, 0) = (-2, -4, -6)$.
