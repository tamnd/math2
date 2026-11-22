---
tag: 9WQHK4Z2WD
kind: proof
name: Proof that a determinant with equal rows or a zero row vanishes
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0K4VQB7HWR
methods: [41JZ39GE3F, 0WCP0PVET6]
uses: [0C3CFHDN6R, 0PPG793642, 0V8F3E48E6, 0CRMGPAH83]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Proof

We take part 1 from the definition, and we reduce each later part to part 1 by linearity in one row.
Let $r_1, \dots, r_n$ be the rows of $A$.
Write $\det(x_1, \dots, x_n)$ for the determinant of the matrix with rows $x_1, \dots, x_n$, and write $A[i \leftarrow x]$ for $A$ with row $i$ replaced by $x$.

*Part 1.*

1. By property 2 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ vanishes on every matrix with two equal rows in different places.

*Part 2.*

2. Let $r_i = 0$.
   Then $r_i = 0 \cdot r_i$, so [[multilinearity in row i|0PPG793642]] gives $\det A = 0 \cdot \det A = 0$.

*Part 3.*

3. Let $r_i = \sum_{k \ne i} c_k r_k$, a [[linear combination|0V8F3E48E6]] of the other rows.
   Linearity in row $i$ gives
$$\det A = \sum_{k \ne i} c_k \det A[i \leftarrow r_k].$$
4. The matrix $A[i \leftarrow r_k]$ has the row $r_k$ in place $k$ and again in place $i \ne k$.
   By step 1, each term of step 3 is $0$, so $\det A = 0$.

*Part 4.*

5. Fix $i$, and let $A' = A[i \leftarrow \sum_k c_k r_k]$.
   The new row $i$ is $0$ by hypothesis, so $\det A' = 0$ by step 2.
6. Linearity in row $i$ gives
$$\det A' = \sum_{k=1}^{n} c_k \det A[i \leftarrow r_k].$$
7. The term with $k = i$ is $c_i \det A$, because $A[i \leftarrow r_i] = A$.
   Each term with $k \ne i$ is $0$ by step 4.
8. So $c_i \det A = \det A' = 0$.

*Part 5.*

9. Over a field, a [[linearly dependent|0CRMGPAH83]] family has a relation $\sum_k c_k r_k = 0$ with some $c_i \ne 0$.
10. By step 8, $c_i \det A = 0$.
    Multiplying by $c_i^{-1}$ gives $\det A = 0$.

## Idea

Two equal rows give zero by definition, and everything else is reduced to that case.
When one row is built from the others, linearity in that row splits the determinant into pieces.
Each piece repeats a row, so each piece is zero.
A relation among all the rows works in the same way, except that the piece with the row itself survives, with the factor $c_i$ in front.
Over a field that factor can be divided away.

## Variants

If the Leibniz sum is taken as the definition, part 1 needs its own proof.
Let rows $i$ and $j$ be equal, and let $\tau$ be the transposition of $i$ and $j$.
Pair each permutation $\sigma$ with $\sigma \tau$.
The two products $\prod_k a_{k \sigma(k)}$ and $\prod_k a_{k \sigma\tau(k)}$ are equal, since they differ only by taking entries from row $i$ or from the equal row $j$.
Their signs are opposite, so the terms cancel in pairs.
The cancellation is exact, so the argument works also when $2 = 0$ in $K$.
