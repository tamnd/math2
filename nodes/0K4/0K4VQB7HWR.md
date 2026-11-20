---
tag: 0K4VQB7HWR
kind: statement
role: proposition
name: Determinant with equal rows or a zero row
aliases: [determinant-of-a-matrix-with-two-equal-rows]
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
about: [00KDZRW4C0]
uses: [0C3CFHDN6R, 0PPG793642, 0V8F3E48E6, 0CRMGPAH83, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$ with rows $r_1, \dots, r_n$.
Let $\det$ be the [[determinant|0C3CFHDN6R]].

1. If two different rows of $A$ are equal, then $\det A = 0$.
2. If a row of $A$ is zero, then $\det A = 0$.
3. If some row $r_i$ is a [[linear combination|0V8F3E48E6]] of the other rows, then $\det A = 0$.
4. If $\sum_k c_k r_k = 0$ with $c_k \in K$, then $c_i \det A = 0$ for every $i$.
5. If $K$ is a [[field|0QA8CHH8MG]] and the rows of $A$ are [[linearly dependent|0CRMGPAH83]], then $\det A = 0$.

## Remarks

### Why each hypothesis is needed

In part 1 the two rows must be in different places; a matrix has each row equal to itself.
In part 4 one only gets $c_i \det A = 0$, not $\det A = 0$.
For example, over $\mathbb{Z}/4\mathbb{Z}$ the $1 \times 1$ matrix $(2)$ has the dependent row $2 \cdot 2 = 0$, but $\det (2) = 2 \neq 0$.
Part 5 needs a field, or at least an integral domain, so that $c_i \det A = 0$ with $c_i \neq 0$ forces $\det A = 0$.

### Consequences

- The same five rules hold for columns, by the [[determinant of the transpose|0ZZQ2E1MTE]].
- Adding a multiple of one row to another row does not change $\det$; see the [[effect of row operations|09YB3WQG38]].
- A matrix with $\det A \neq 0$ over a field has independent rows; this is one half of the [[invertibility criterion|FBSAPTP1PR]].

### Converse

Over a field the converse of part 5 is also true: $\det A = 0$ implies that the rows are dependent.
The proof needs row reduction or the adjugate; see the [[invertibility criterion|FBSAPTP1PR]].
For a $2 \times 2$ example, $\det \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 0$, and row $2$ is twice row $1$.

### Generalizations

Every [[alternating multilinear map|0MSWYWHYF5]] has the same five properties, by the same proof.
Over an integral domain $R$, part 5 holds in the form: dependent rows over the field of fractions of $R$ give $\det A = 0$.

## Explanations

### L1 human

If two rows of a square table are the same, its determinant is $0$.
The same is true if a row has only zeros.
More generally, the determinant is $0$ if one row can be built from the other rows by scaling and adding.
In the picture of volume, the rows then lie in a flat plane, so the box they span has no volume.

### L2 human

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$.

1. Row $3$ is $2 r_2 - r_1$, since $2(4, 5, 6) - (1, 2, 3) = (7, 8, 9)$.
2. By part 3, $\det A = 0$.
3. Check by the rule of Sarrus: $45 + 84 + 96 - 105 - 48 - 72 = 225 - 225 = 0$.

The typical use is to see at once that a determinant is zero.
A trap: "no two rows are equal" does not mean $\det A \neq 0$, as this example shows.

### L3 human

Parts 1 to 4 hold for any alternating multilinear map $D$ on a module.
Part 4 says that $\det A$ is killed by every coefficient of a relation among the rows; so over a ring, $\det A$ is a zero divisor or zero when the rows are dependent.
This is the key step of McCoy's theorem: a system $Ax = 0$ over a commutative ring has a nonzero solution if and only if the annihilator of the ideal of maximal minors is nonzero.
