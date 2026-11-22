---
tag: 6X9G57XHMF
kind: example
name: The rank of the matrix with entries 1 to 9 over the reals and over F3
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 0F27PBRWD7, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Computing the rank of a matrix
---

## Example

The same table of integers can have one rank over the real numbers and a smaller rank over a finite field.
Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix},$$
with columns $a_1, a_2, a_3$.
We find its [[rank|0EWQEYRVA8]] over $\mathbb{R}$ and over $\mathbb{F}_3$.

1. Over $\mathbb{R}$, subtract $4$ times row 1 from row 2 and $7$ times row 1 from row 3.
The rows become $(1, 2, 3)$, $(0, -3, -6)$ and $(0, -6, -12)$.
2. Subtract $2$ times row 2 from row 3.
The [[echelon form|0F27PBRWD7]] has rows $(1, 2, 3)$, $(0, -3, -6)$ and $(0, 0, 0)$, with two pivots, so the rank over $\mathbb{R}$ is $2$.
3. Check with a relation between the columns:
$$a_1 - 2a_2 + a_3 = (1 - 4 + 3,\ 4 - 10 + 6,\ 7 - 16 + 9) = (0, 0, 0).$$
4. Check with the [[determinant|0C3CFHDN6R]], expanded along the first row:
$$\det A = 1(45 - 48) - 2(36 - 42) + 3(32 - 35) = -3 + 12 - 9 = 0.$$
The $2 \times 2$ minor in the top left corner is $1 \cdot 5 - 2 \cdot 4 = -3 \ne 0$, so the largest nonzero minor has size $2$.
5. Over $\mathbb{F}_3$, reduce each entry modulo $3$: $4 \equiv 1$, $5 \equiv 2$, $6 \equiv 0$, $7 \equiv 1$, $8 \equiv 2$ and $9 \equiv 0$.
All three rows become $(1, 2, 0)$.
6. The three rows are equal and nonzero, so the row space is the line spanned by $(1, 2, 0)$, and the rank over $\mathbb{F}_3$ is $1$.

## Remarks

The example shows that the rank depends on the field.
The reason is visible in the minors.
The nine $2 \times 2$ minors of $A$ are $-3$, $-6$, $-3$, $-6$, $-12$, $-6$, $-3$, $-6$ and $6$, and all of them are multiples of $3$.
So over $\mathbb{F}_3$ every $2 \times 2$ minor is $0$, and the rank falls to $1$.

What happens over other fields?
Over $\mathbb{F}_p$ with $p \ne 3$, the minor $-3$ is nonzero, and $\det A = 0$ in every field, so the rank stays $2$.
For example, over $\mathbb{F}_2$ the rows are $(1, 0, 1)$, $(0, 1, 0)$ and $(1, 0, 1)$, and the rank is $2$.
In general, for an integer matrix, the rank over $\mathbb{F}_p$ is at most the rank over $\mathbb{Q}$, because a minor that is nonzero modulo $p$ is a nonzero integer.

## Explanations

### L1 human

The rows of this matrix go up in equal steps: each row is the one before it plus $(3, 3, 3)$.
So the third row is twice the second row minus the first row, and only two rows are really new.
That makes the rank $2$.
If we count modulo $3$, the step $(3, 3, 3)$ becomes zero, all rows become equal, and the rank becomes $1$.

### L2 human

To compute a rank over $\mathbb{F}_p$, first reduce all entries modulo $p$, and then row reduce with arithmetic modulo $p$.
Here the reduction modulo $3$ already gives three equal rows, so no more work is needed.
Watch out: you cannot reduce over $\mathbb{R}$ first and then read the result modulo $p$ in general, because a row operation over $\mathbb{R}$ may divide by a multiple of $p$.
Here the pivot $-3$ of step 2 is $0$ modulo $3$, which is exactly where the two computations part ways.
