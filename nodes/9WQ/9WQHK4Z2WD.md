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

Let $r_1, \dots, r_n$ be the rows of $A$, and write $\det(x_1, \dots, x_n)$ for the determinant of the matrix with rows $x_1, \dots, x_n$.

1. Part 1. By property 2 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ vanishes on every matrix with two equal rows.
2. Part 2. Let $r_i = 0$. Then $r_i = 0 \cdot r_i$, so [[multilinearity|0PPG793642]] in row $i$ gives $\det A = 0 \cdot \det A = 0$.
3. Part 3. Let $r_i = \sum_{k \neq i} c_k r_k$, a [[linear combination|0V8F3E48E6]] of the other rows.
4. Multilinearity in row $i$ gives $\det A = \sum_{k \neq i} c_k \det(r_1, \dots, r_k, \dots, r_n)$, with $r_k$ in place $i$.
5. Each matrix in the sum of step 4 has $r_k$ in place $k$ and in place $i \neq k$. By step 1, each term is $0$.
6. So $\det A = 0$.
7. Part 4. Fix $i$ and let $A'$ be $A$ with row $i$ replaced by $\sum_k c_k r_k = 0$. By step 2, $\det A' = 0$.
8. Multilinearity in row $i$ gives $\det A' = \sum_k c_k \det(r_1, \dots, r_k, \dots, r_n)$, with $r_k$ in place $i$.
9. In step 8 the term $k = i$ is $c_i \det A$. Each term $k \neq i$ is $0$ by step 1.
10. So $c_i \det A = \det A' = 0$.
11. Part 5. Over a field, a [[linearly dependent|0CRMGPAH83]] family has a relation $\sum_k c_k r_k = 0$ with some $c_i \neq 0$.
12. By step 10, $c_i \det A = 0$. Multiplying by $c_i^{-1}$ gives $\det A = 0$.

## Idea

Two equal rows give zero by definition.
For a row built from the other rows, multilinearity splits the determinant into pieces with two equal rows.
A relation among the rows works the same way, but leaves the factor $c_i$ in front of $\det A$.

## Variants

With the Leibniz sum as the definition, part 1 is proved by pairing $\sigma$ with $\sigma \tau$, where $\tau$ exchanges the two equal rows: the two terms are equal with opposite signs.
This is step 4 of the proof of the [[existence and uniqueness theorem|1C8RRWHD45]], and it also works in characteristic $2$.
