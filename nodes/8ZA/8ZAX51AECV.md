---
tag: 8ZAX51AECV
kind: example
name: A basis of the row space of a 3 × 4 matrix from its echelon form
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [069MCGX635]
illustrates: [1JGMW9DM4Z]
uses: [0EP73HK4C4, 0NNR68BFRY]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Basis
  - book: isbn:9780321982384
    locator: Section 4.6
---

## Example

The nonzero rows of the reduced form are a basis of the row space, and the pivot columns make the membership test quick.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$$
over $\mathbb{R}$.
Its [[reduced row echelon form|0NNR68BFRY]], found in the [[column space example|AGHYPF25CY]], has the nonzero rows $u_1 = (1, 2, 0, 1)$ and $u_2 = (0, 0, 1, 2)$, with pivots in columns 1 and 3.

1. By the [[echelon basis theorem|1JGMW9DM4Z]], $u_1, u_2$ is a basis of the [[row space|0EP73HK4C4]] of $A$, so $\dim \operatorname{Row}(A) = 2$.
2. We check that the rows of $A$ lie in the span; row 1 is $u_1$ itself.
3. Row 2 is $2u_1 + u_2 = (2, 4, 0, 2) + (0, 0, 1, 2) = (2, 4, 1, 4)$.
4. Row 3 is $3u_1 + u_2 = (3, 6, 0, 3) + (0, 0, 1, 2) = (3, 6, 1, 5)$.
5. For independence, a combination is $a u_1 + b u_2 = (a, 2a, b, a + 2b)$, and if it is $0$, entry 1 gives $a = 0$ and entry 3 gives $b = 0$.
6. For $v = (1, 2, 1, 3)$, entries 1 and 3 force $a = 1$ and $b = 1$, and $u_1 + u_2 = (1, 2, 1, 3) = v$, so $v \in \operatorname{Row}(A)$.
7. For $w = (0, 1, 0, 0)$, entries 1 and 3 force $a = b = 0$, which gives the zero vector and not $w$, so $w \notin \operatorname{Row}(A)$.

## Remarks

The example shows why the reduced form gives the most convenient basis.
At a pivot column, exactly one basis vector has a nonzero entry, and that entry is $1$, so the coefficients of a combination can be read at the pivot columns.
After that, the other entries only need to be checked.

The basis is not unique.
The rows of $A$ satisfy row 3 = row 1 + row 2, since $(1, 2, 0, 1) + (2, 4, 1, 4) = (3, 6, 1, 5)$, so rows 1 and 2 of $A$ are another basis.
The column space of $A$ also has dimension $2$, as the theorem that [[row rank equals column rank|0TZAG60ZYT]] says, but it is a plane in $\mathbb{R}^3$, while the row space is a plane in $\mathbb{R}^4$.
If we change the entry $5$ in the corner to $6$, row reduction leaves three nonzero rows, and the row space becomes a subspace of dimension $3$ in $\mathbb{R}^4$.

## Explanations

### L1 human

Row reduction keeps the row space, so the nonzero rows at the end span the same space as the rows at the start.
Here two rows survive, so the row space is a flat plane inside four-dimensional space.
Every row of $A$ is built from the two surviving rows, for example row 2 is twice the first plus the second.

### L2 human

To decide whether a vector lies in the row space, first read its entries at the pivot columns 1 and 3.
These entries are the only possible coefficients $a$ and $b$.
Then form $a u_1 + b u_2$ and compare the remaining entries with the vector.
Watch out: a vector can agree with the combination at the pivot columns and still fail elsewhere, as $w$ does at entry 2.
