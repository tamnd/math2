---
tag: MDB2CHQDXJ
kind: example
name: The rank of a 3 × 4 matrix computed in four ways
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [0ZC9YTXZRY]
illustrates: [0TZAG60ZYT]
uses: [0EWQEYRVA8, 0NNR68BFRY, 0BCMGDHZGR, 0SD528P0EK]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Computing the rank of a matrix
---

## Example

Four different counts give the same [[rank|0EWQEYRVA8]], and one matrix shows all four at work.
Let
$$A = \begin{pmatrix} 1 & 2 & 0 & 1 \\ 2 & 4 & 1 & 4 \\ 3 & 6 & 1 & 5 \end{pmatrix}$$
over $\mathbb{R}$, with columns $a_1, a_2, a_3, a_4$ and rows $\rho_1, \rho_2, \rho_3$.

1. Pivots.
Subtract $2\rho_1$ from $\rho_2$ and $3\rho_1$ from $\rho_3$; both new rows are $(0, 0, 1, 2)$, so subtracting the new row 2 from the new row 3 leaves a zero row.
The [[reduced row echelon form|0NNR68BFRY]] has the rows $(1, 2, 0, 1)$, $(0, 0, 1, 2)$ and $(0, 0, 0, 0)$, with two [[pivots|0BCMGDHZGR]], so $\rank A = 2$.
2. Columns.
The second column is $a_2 = (2, 4, 6) = 2a_1$, and the fourth is
$$a_1 + 2a_3 = (1, 2, 3) + (0, 2, 2) = (1, 4, 5) = a_4.$$
The columns $a_1 = (1, 2, 3)$ and $a_3 = (0, 1, 1)$ are not multiples of each other, so they form a basis of the column space, and its dimension is $2$.
3. Rows.
The rows satisfy $\rho_1 + \rho_2 = (3, 6, 1, 5) = \rho_3$.
The rows $\rho_1$ and $\rho_2$ are not proportional: position 3 rules out $\rho_2 = c\rho_1$, since $1 \ne c \cdot 0$, and $\rho_1 = c\rho_2$ would force $c = 0$ there and so $\rho_1 = 0$.
So the row space has dimension $2$.
4. Minors.
The [[minor|0SD528P0EK]] on rows 1, 2 and columns 1, 3 is
$$\det \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix} = 1 \ne 0.$$
Each $3 \times 3$ minor uses three of the four columns, and any three columns are dependent: $a_2 = 2a_1$, $a_4 = a_1 + 2a_3$ and $a_4 = \tfrac{1}{2} a_2 + 2a_3$.
So all four $3 \times 3$ minors are $0$, the largest nonzero minor has size $2$, and the rank is $2$ once more.

## Remarks

Steps 2 and 3 count different things, independent columns in $\mathbb{R}^3$ and independent rows in $\mathbb{R}^4$, and they agree, as the theorem that [[row rank equals column rank|0TZAG60ZYT]] promises.
The pivots of step 1 sit in columns 1 and 3, and these are exactly the columns $a_1$ and $a_3$ chosen in step 2.

The rank $2$ is less than $\min(3, 4) = 3$, so $A$ does not have full rank.
If we change the entry in position $(3, 4)$ from $5$ to $6$, then $\rho_3 \ne \rho_1 + \rho_2$, the reduction leaves the third row $(0, 0, 0, 1)$, and the rank becomes $3$.
Then the minor on columns 1, 3, 4 is no longer zero.

## Explanations

### L1 human

The second column is twice the first, and the fourth column is the first plus twice the third.
So only two columns bring a new direction.
Looking at rows instead, the third row is the sum of the first two.
Both ways of looking give the number $2$.

### L2 human

Each method fits a different job.
Pivots are the fastest by hand and by computer, and they also tell you which columns to keep as a basis.
Column and row relations explain why the rank is what it is.
Minors give a test that needs no choices, but there are many of them: a $3 \times 4$ matrix has eighteen $2 \times 2$ minors and four $3 \times 3$ minors.
Watch out: one zero minor proves nothing, since only the vanishing of all minors of a size bounds the rank.
