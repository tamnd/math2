---
tag: 01ZTQBK64Q
kind: statement
role: proposition
name: Adding a multiple of one row to another preserves the determinant
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

The most used step of elimination, adding a multiple of one row to another, leaves the determinant unchanged.
Let $K$ be a commutative ring, let $n \ge 2$, let $A$ be an $n \times n$ matrix over $K$, and let $c \in K$.
Let $i \ne j$, and let $B$ be the matrix that results when $c$ times row $j$ of $A$ is added to row $i$.
Then $\det B = \det A$, where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

### A small check

Add $-2$ times row $1$ to row $2$ in $\begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix}$:
$$\det \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix} = 7 - 6 = 1, \qquad \det \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix} = 1 - 0 = 1.$$
The value stays $1$, and the second matrix is triangular, so its determinant is the product of the diagonal.

### Why it holds

Split the new row $i$ into the old row and the added part.
By [[linearity in row i|0PPG793642]], $\det B = \det A + c \det A'$, where $A'$ is $A$ with row $i$ replaced by row $j$.
The matrix $A'$ has the same row in places $i$ and $j$, so $\det A' = 0$ by the rule for [[equal rows|0K4VQB7HWR]].
The [[proof|VCTVF3AZ1Q]] writes this out step by step.

### Why the rows must be different

With $i = j$, the operation adds $c$ times row $i$ to itself, which multiplies that row by $1 + c$.
Then the determinant is multiplied by $1 + c$, for example by $2$ when $c = 1$.
So the hypothesis $i \ne j$ cannot be dropped.

### What it gives you

Since this operation is free, [[Gaussian elimination|0JVJ2WCXZH]] can clear the entries below the diagonal without changing the determinant, and only exchanges and scalings need bookkeeping.
The same rule holds for columns, by the [[determinant of the transpose|0ZZQ2E1MTE]].
It is one of the [[effects of row operations|09YB3WQG38]].

## Explanations

### L1 human

In the plane, the two rows of a $2 \times 2$ matrix are two arrows, and the determinant is the signed area of the parallelogram they span.
Adding a multiple of one arrow to the other slides that side along the direction of the first arrow.
This is a shear: the base and the height of the parallelogram stay the same, so the area stays the same.
For the rows $(1, 3)$ and $(2, 7)$, sliding the second one to $(0, 1)$ keeps the area $1$.

### L2 human

Here is a typical use: compute
$$\det \begin{pmatrix} 1 & 2 & 3 \\ 2 & 5 & 8 \\ 3 & 8 & 14 \end{pmatrix}.$$
Subtract $2$ times row $1$ from row $2$ and $3$ times row $1$ from row $3$, which gives the rows $(0, 1, 2)$ and $(0, 2, 5)$.
Then subtract $2$ times the new row $2$ from row $3$, which gives $(0, 0, 1)$.
None of these steps changes the determinant, and the result is triangular with diagonal $1, 1, 1$, so the determinant is $1$.
Check by the rule of Sarrus: $70 + 48 + 48 - 45 - 64 - 56 = 166 - 165 = 1$.
Watch out: the rule is about adding a multiple of another row, so replacing row $2$ by $2$ times row $2$ minus row $1$ is not free; it doubles the determinant.
