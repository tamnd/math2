---
tag: TSZFS6VP5M
kind: example
name: Checking the echelon conditions on a 4 by 5 matrix
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
instance_of: [0VYCDGMJJJ, 0J0BBCMJ5W]
uses: [0F27PBRWD7, 0BCMGDHZGR]
sources:
  - url: https://en.wikipedia.org/wiki/Row_echelon_form
    locator: lead section
---

## Example

We check the two echelon conditions on a larger matrix and then read it in two ways.
Let
$$M = \begin{bmatrix} 2 & 1 & 0 & 3 & 1 \\ 0 & 0 & 5 & 1 & 2 \\ 0 & 0 & 0 & 0 & 4 \\ 0 & 0 & 0 & 0 & 0 \end{bmatrix}$$
over $\mathbb{R}$.

1. The leading entry of row $1$ is $2$, in column $1$.
2. The leading entry of row $2$ is $5$, in column $3$.
3. The leading entry of row $3$ is $4$, in column $5$.
4. Row $4$ is zero, and it is the bottom row. So the zero-row condition holds.
5. The columns $1 < 3 < 5$ increase, so the staircase condition holds.
6. So $M$ is in [[row echelon form|0F27PBRWD7]], with [[pivot|0BCMGDHZGR]] columns $1$, $3$ and $5$, and $3$ pivots.
7. Now read $M$ as the augmented matrix of a system in $x_1, \dots, x_4$. Row $3$ says $0 = 4$.
8. So that system is inconsistent, because the last column is a pivot column.
9. Read $M$ instead as the coefficient matrix of $Mx = 0$ in $x_1, \dots, x_5$. The columns $2$ and $4$ have no pivot, so $x_2$ and $x_4$ are free.

## Remarks

The same matrix gives different answers depending on whether its last column is a right side.
As an augmented matrix, the pivot in column $5$ signals an impossible equation.
As a coefficient matrix, it only says that $x_5$ is a basic variable, and indeed row 3 forces $x_5 = 0$.

If the entry $4$ were $0$, row $3$ would be zero.
The system of step 7 would then be consistent, with the free variables $x_2$ and $x_4$.

## Explanations

### L1 human

Read each row from the left until you hit a number that is not zero.
These first numbers must move to the right as you go down, like steps.
Here they sit in columns $1$, $3$ and $5$, so the steps are correct.

### L2 human

1. Mark the leading entry of each row.
2. Check that the marks move strictly right going down.
3. Check that the zero rows are at the bottom.

Watch out: a leading entry in the last column of an augmented matrix means "no solution", not "the last unknown is $4$".
