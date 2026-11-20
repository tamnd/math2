---
tag: "D3PN42EP4X"
kind: statement
role: proposition
name: Vectors span F^m iff the matrix of columns has a pivot in every row
msc: ["15A03", "15A06"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0DTY8B9HMS, 0BCMGDHZGR, 0XM8BZD76G, 0BJKVF90Z6]
about: [088RYKAWK9]
proofs: [~7399a93b]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-3.xml#L1347
    locator: src/section2-3.xml:1347
  - book: isbn:9780321982384
    locator: Section 1.4
---

## Statement

Let $F$ be a field, and let $v_1, \dots, v_n$ be vectors in the [[coordinate space|~9949dfd5]] $F^m$.
Let $A$ be the $m \times n$ matrix whose columns are $v_1, \dots, v_n$.

1. The vectors $v_1, \dots, v_n$ [[span|0BJKVF90Z6]] $F^m$ if and only if every row of $A$ contains a [[pivot|0BCMGDHZGR]] position.
2. In particular, a spanning set of $F^m$ has at least $m$ vectors.

## Remarks

### Why each hypothesis is needed

The statement is about the whole space $F^m$.
For a subspace $W \subsetneq F^m$, a spanning set of $W$ gives a matrix with zero rows in its echelon form.
The pivot positions must be read from an echelon form of $A$, not from $A$ itself.
The matrix with columns $(0, 1)$ and $(1, 0)$ spans $F^2$ but has a zero entry at position $(1, 1)$.

### Consequences

If $n < m$, then the vectors cannot span $F^m$, because $A$ has at most $n$ pivot positions, one in each pivot column.
A row without a pivot gives a vector $b$ for which the system $Ax = b$ has no solution.
Together with the [[column test for independence|76GG9B25A1]], it shows that a basis of $F^m$ has exactly $m$ vectors.

### Converse

Part 1 is an equivalence.
The converse of part 2 fails, because $(1, 1)$ and $(2, 2)$ are two vectors that do not span $F^2$.

### Generalizations

For a general space $V$ of dimension $m$, choose a basis and use coordinates.
Then $n$ vectors span $V$ exactly when their coordinate matrix has a pivot in every row.
Over a ring, the pivot test fails: $2 \in \Z$ alone does not span $\Z$, although the $1 \times 1$ matrix $(2)$ has a nonzero entry.

## Explanations

### L1 human

Put the vectors side by side as columns and row reduce.
If each row gets a pivot, every right side $b$ can be reached, so the vectors span.
If one row has no pivot, some $b$ cannot be reached.

### L2 human

Example in $\R^3$: $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$, $v_3 = (1, 1, 0)$.
Row reduction of the matrix with these columns subtracts row 1 from row 3, then row 2 from row 3.
The new row 3 is $(0, 0, -2)$, so each of the three rows has a pivot, and the vectors span $\R^3$.
With $v_3 = (1, 1, 2)$ instead, row 3 becomes $(0, 0, 0)$, and the vectors span only the plane $z = x + y$.
