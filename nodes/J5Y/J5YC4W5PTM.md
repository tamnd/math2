---
tag: J5YC4W5PTM
kind: proof
name: Proof of the column test for linear independence
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 76GG9B25A1
methods: [TFQ1845T84, 0NTF6DMVAP]
uses: [0EVHJFTG9Z, E7SAHXQEVC, JPW6KVS70A, H75GS7QVPB]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Evaluating linear independence
  - book: isbn:9780321982384
    locator: Section 1.7
---

## Proof

We link each condition to the next: condition 2 through the dependence lemma, condition 3 through the matrix-vector product, and condition 4 through free variables.

1. By part 3 of the [[linear dependence lemma|H75GS7QVPB]], the columns are dependent if and only if some column $v_j$ lies in the span of the other columns. Negating both sides shows that conditions 1 and 2 are equivalent.
2. By [[linear systems as vector equations|E7SAHXQEVC]], for every $x = (x_1, \dots, x_n)$ in $F^n$,
$$Ax = x_1 v_1 + \dots + x_n v_n.$$
3. So a solution $x \ne 0$ of $Ax = 0$ is the same thing as a list of coefficients, not all $0$, with $x_1 v_1 + \dots + x_n v_n = 0$.
4. By the [[definition of independence|0EVHJFTG9Z]], such coefficients exist exactly when the columns are dependent. So conditions 1 and 3 are equivalent.
5. By the [[theorem on homogeneous systems|JPW6KVS70A]], $Ax = 0$ has a solution $x \ne 0$ if and only if some column of an echelon form of $A$ has no pivot. Negating both sides shows that conditions 3 and 4 are equivalent.
6. For part 2, each pivot is the leading entry of its own row, so an echelon form of $A$ has at most $m$ pivots.
7. If $n > m$, then at most $m$ of the $n$ columns hold a pivot, so some column has none.
8. Then condition 4 fails, and by part 1 the columns are linearly dependent.

## Idea

The matrix-vector product turns the question about vectors into a question about one homogeneous system.
A dependence relation among the columns is exactly a nonzero solution of $Ax = 0$.
Row reduction produces such a solution exactly when there is a free variable, that is, a column without a pivot.
Counting pivots by rows then gives part 2, since a matrix cannot have more pivots than rows.

## Variants

Part 2 has a proof by induction on $m$ that avoids echelon forms.
For $m = 1$, two or more scalars $a_1, a_2, \dots$ are dependent: if $a_1 = 0$ then $1 \cdot a_1 = 0$, and otherwise $a_2 a_1 - a_1 a_2 = 0$ with the coefficient $a_2$ on $a_1$ and $-a_1 \ne 0$ on $a_2$.
For larger $m$, if every column has first entry $0$, drop the first row and use the induction hypothesis.
Otherwise, say $v_1$ has first entry $c \ne 0$, and replace each other column $v_j$ by $w_j = v_j - c^{-1} (v_j)_1 v_1$, whose first entry is $0$.
The $n - 1$ vectors $w_j$ live in a copy of $F^{m-1}$ and $n - 1 > m - 1$, so they satisfy a nontrivial relation by induction.
Expanding each $w_j$ turns that relation into a relation among $v_1, \dots, v_n$ in which some $v_j$ with $j \ge 2$ has a nonzero coefficient.
The equivalence of conditions 1 and 3 can also be stated as: $x \mapsto Ax$ is injective exactly when its kernel is zero.
