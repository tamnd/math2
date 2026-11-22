---
tag: KFJ7M9FRXV
kind: example
name: A family that is independent over R and dependent over F_2
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0CRMGPAH83]
uses: [0EVHJFTG9Z, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
---

## Example

Let $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$ and $v_3 = (1, 1, 0)$.
All entries are $0$ or $1$, so these are vectors of $\mathbb{R}^3$ and also of $\mathbb{F}_2^3$, where $\mathbb{F}_2 = \{0, 1\}$ is the field with $1 + 1 = 0$.
The same three vectors are [[linearly independent|0EVHJFTG9Z]] over $\mathbb{R}$ and linearly dependent over $\mathbb{F}_2$.

We check independence over $\mathbb{R}$.

1. Suppose $a v_1 + b v_2 + c v_3 = 0$ with $a, b, c \in \mathbb{R}$. Adding entry by entry gives
$$(a + c, \ b + c, \ a + b) = (0, 0, 0).$$
2. The first two entries give $a = -c$ and $b = -c$.
3. The third entry then gives $a + b = -2c = 0$. Since $2 \ne 0$ in $\mathbb{R}$, we may divide by $-2$, so $c = 0$.
4. Steps 2 and 3 give $a = b = c = 0$, so only the trivial combination is zero.

We check dependence over $\mathbb{F}_2$.

5. Add the three vectors entry by entry:
$$v_1 + v_2 + v_3 = (1 + 0 + 1, \ 0 + 1 + 1, \ 1 + 1 + 0) = (2, 2, 2).$$
6. In $\mathbb{F}_2$ we have $2 = 1 + 1 = 0$, so $v_1 + v_2 + v_3 = (0, 0, 0)$.
7. The coefficients $1, 1, 1$ are not all zero, so this is a nontrivial relation, and the family is dependent.

## Remarks

The whole difference sits in step 3, where we divide by $2$.
Over $\mathbb{F}_2$ that division is impossible, and $c = 1$ solves $-2c = 0$, which leads to the relation of step 6.

The [[determinant|0C3CFHDN6R]] shows the same thing at once.
Expanding along the first row of the matrix with columns $v_1, v_2, v_3$ gives
$$\det \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} = 1 \cdot (1 \cdot 0 - 1 \cdot 1) - 0 + 1 \cdot (0 \cdot 1 - 1 \cdot 1) = -2.$$
The determinant is an integer, and its image in a field $F$ is nonzero exactly when $2 \ne 0$ in $F$.
So the family is independent over every field of characteristic other than $2$, for example over $\mathbb{Q}$, $\mathbb{C}$ and $\mathbb{F}_3$, and dependent over every field of characteristic $2$.

If you change one entry, the picture changes.
For $v_3 = (1, 1, 1)$ the determinant becomes $1 \cdot (1 - 1) - 0 + 1 \cdot (0 - 1) = -1$, which is nonzero in every field, so that family is independent over all fields.
The lesson is that independence is a property of the vectors together with the field of scalars, not of the vectors alone.

## Explanations

### L1 human

The same three lists of numbers can be independent or dependent, depending on which numbers you may use as coefficients and how they add.
In ordinary arithmetic, no recipe with these three lists gives zero except the empty recipe.
In the arithmetic of $\mathbb{F}_2$, where $1 + 1 = 0$, adding all three lists gives zero in every entry.

### L2 human

The determinant test turns the question into one number.
For a square matrix with integer entries, compute the determinant once over $\mathbb{Z}$, here $-2$.
Over a field $F$, the columns are independent exactly when this integer is nonzero in $F$.
Since $-2$ is divisible only by the prime $2$, only fields of characteristic $2$ see a dependence.
Watch out: checking independence over $\mathbb{R}$ does not settle independence over a finite field, as this example shows.
