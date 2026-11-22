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

A determinant is $0$ as soon as its rows carry less information than they should: two equal rows, a zero row, or a row built from the others.
Let $K$ be a commutative ring, let $n \ge 1$, and let $A$ be an $n \times n$ matrix over $K$ with rows $r_1, \dots, r_n$.
Let $\det$ be the [[determinant|0C3CFHDN6R]].

1. If $r_i = r_j$ for two indices $i \ne j$, then $\det A = 0$.
2. If some row $r_i$ is zero, then $\det A = 0$.
3. If some row $r_i$ is a [[linear combination|0V8F3E48E6]] of the other rows, then $\det A = 0$.
4. If $c_1 r_1 + \dots + c_n r_n = 0$ with $c_k \in K$, then $c_i \det A = 0$ for every $i$.
5. If $K$ is a [[field|0QA8CHH8MG]] and the rows of $A$ are [[linearly dependent|0CRMGPAH83]], then $\det A = 0$.

## Remarks

### Seeing a zero at once

Take
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}.$$
No two rows are equal and no row is zero, but the third row is built from the other two:
$$2 (4, 5, 6) - (1, 2, 3) = (7, 8, 9).$$
So part 3 gives $\det A = 0$ without any further work.
Check by the rule of Sarrus:
$$45 + 84 + 96 - 105 - 48 - 72 = 225 - 225 = 0.$$

### Why each hypothesis is needed

Part 1 asks for two rows in different places, $i \ne j$.
The condition $r_i = r_i$ says nothing, and $\det I_2 = 1$ although each row equals itself.

Part 4 gives only $c_i \det A = 0$, and over a general ring this does not force $\det A = 0$.
Over $\mathbb{Z}/4\mathbb{Z}$, the $1 \times 1$ matrix $(2)$ has the relation $2 \cdot 2 = 0$ with the nonzero coefficient $2$.
Its determinant is $2 \ne 0$, and part 4 only says $2 \cdot 2 = 0$, which is true.
That is why part 5 asks for a field: there a nonzero $c_i$ has an inverse, and $c_i \det A = 0$ gives $\det A = 0$.
The same argument works over any integral domain.

### What it gives you

Parts 1 to 3 are the fastest test for a zero determinant, and they hold for columns too by the [[determinant of the transpose|0ZZQ2E1MTE]].
Part 1 with multilinearity shows that adding a multiple of one row to another row keeps the determinant, which is one of the [[effects of row operations|09YB3WQG38]].
Part 5 is one half of the [[invertibility criterion|FBSAPTP1PR]]: over a field, $\det A \ne 0$ forces independent rows.

### The converse

Over a field the converse of part 5 is true: if $\det A = 0$, then the rows are dependent.
This needs more than multilinearity, namely row reduction or the adjugate, and the [[invertibility criterion|FBSAPTP1PR]] proves it.
For example, $\det \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} = 4 - 4 = 0$, and the second row is twice the first.
Over the ring $\mathbb{Z}/6\mathbb{Z}$ the converse of part 3 fails: $\det \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix} = 6 = 0$, but neither row is a multiple of the other.
The rows still satisfy the relation $3 (2, 0) + 2 (0, 3) = (6, 6) = 0$, so over a ring a relation is the right notion, not a combination.

### Watch out

"No two rows are equal" does not mean "the determinant is nonzero".
The matrix in the first example has three different rows and determinant $0$.
The correct test over a field is linear dependence, not equality.

### Try it

Is $\det \begin{pmatrix} 1 & 0 & 2 \\ 3 & 1 & 1 \\ 5 & 1 & 5 \end{pmatrix}$ zero?
Yes, because the third row is $2 (1, 0, 2) + (3, 1, 1) = (5, 1, 5)$, so part 3 applies.

## Explanations

### L1 human

If two rows of a square table are the same, its determinant is $0$.
The same is true if a row has only zeros.
More generally, the determinant is $0$ when one row can be built from the others by scaling and adding.
In the picture of volume, the rows then lie in one flat plane, so the box they span has no volume.
For example, the rows $(1, 2)$ and $(2, 4)$ lie on one line, and $1 \cdot 4 - 2 \cdot 2 = 0$.

### L2 human

Here is a typical use: for which $t$ is $\det \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 1 & t & 5 \end{pmatrix}$ zero?
Look for a combination $a (1, 1, 1) + b (1, 2, 3)$ that equals $(1, t, 5)$.
The first and last entries give $a + b = 1$ and $a + 3b = 5$, so $b = 2$ and $a = -1$.
The middle entry is then $t = a + 2b = 3$.
So for $t = 3$ the third row is a combination of the others, and part 3 gives determinant $0$.
Check by the rule of Sarrus at $t = 3$:
$$10 + 3 + 3 - 2 - 9 - 5 = 0.$$
The problem shows the typical use: a dependence among rows gives a zero determinant without expansion.
Watch out: to show that the determinant is nonzero for the other values of $t$, you need the converse of part 5, which the [[invertibility criterion|FBSAPTP1PR]] supplies.

### L3 human

Parts 1 to 4 hold for every [[alternating multilinear map|0MSWYWHYF5]], with the same proof.
Part 4 says that every coefficient of a relation among the rows kills $\det A$.
So over a commutative ring, dependent rows make $\det A$ zero or a zero divisor.
For square matrices the converse also holds, by McCoy's theorem: $Ax = 0$ has a nonzero solution exactly when $\det A$ is zero or a zero divisor.
The [[determinants over commutative rings|03Q7RE2HXR]] continue this line.
