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

Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$$
over $\R$.
Its [[reduced row echelon form|0NNR68BFRY]], found in the [[column space example|AGHYPF25CY]], has the nonzero rows $u_1 = (1, 2, 0, 1)$ and $u_2 = (0, 0, 1, 2)$.

1. By the [[theorem on the row space|1JGMW9DM4Z]], $\{u_1, u_2\}$ is a basis of the [[row space|0EP73HK4C4]] of $A$, and $\dim \operatorname{Row}(A) = 2$.
2. Check that the rows of $A$ are in the span: row 1 is $u_1$.
3. Row 2 is $2u_1 + u_2 = (2, 4, 0, 2) + (0, 0, 1, 2) = (2, 4, 1, 4)$.
4. Row 3 is $3u_1 + u_2 = (3, 6, 0, 3) + (0, 0, 1, 2) = (3, 6, 1, 5)$.
5. Independence: $a u_1 + b u_2 = (a,\ 2a,\ b,\ a + 2b)$. If this is $0$, then $a = 0$ from entry 1 and $b = 0$ from entry 3.
6. Membership test for $v = (1, 2, 1, 3)$: entries 1 and 3 force $a = 1$ and $b = 1$. Then $u_1 + u_2 = (1, 2, 1, 3) = v$, so $v \in \operatorname{Row}(A)$.
7. Membership test for $w = (0, 1, 0, 0)$: entries 1 and 3 force $a = b = 0$, which gives $0 \ne w$. So $w \notin \operatorname{Row}(A)$.

## Remarks

- The rows of $A$ satisfy row 3 = row 1 + row 2. So rows 1 and 2 of $A$ are another basis of $\operatorname{Row}(A)$.
- The row space and the column space both have dimension $2$, as the theorem that [[row rank equals column rank|0TZAG60ZYT]] says. But they lie in different spaces, $\R^4$ and $\R^3$.

## Explanations

### L1 human

Row reduction keeps the row space, so the nonzero rows at the end span the same space as the rows at the start.
Here two rows survive, so the row space is a plane in $\R^4$.

### L2 human

The pivot entries make the membership test easy: the coefficients of a combination of $u_1$ and $u_2$ are read off at the pivot columns 1 and 3.
Then one checks the other entries.
This is why the reduced form gives the most convenient basis of the row space.
