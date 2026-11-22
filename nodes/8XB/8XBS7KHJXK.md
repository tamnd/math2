---
tag: 8XBS7KHJXK
kind: example
name: Rule of Sarrus for a 3 × 3 integer matrix
msc: ["15A15"]
topics: [DTBK11SR77]
audience: school
instance_of: [7H2P40X0MV]
uses: [7H2P40X0MV, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_Sarrus
    locator: lead section
---

## Example

Let $A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & -1 & 4 \\ 5 & 2 & 1 \end{pmatrix}$ over $\mathbb{Z}$.
We compute $\det A$ by the [[rule of Sarrus|7H2P40X0MV]], and we check the value by a [[Laplace expansion|0C08BQ3M05]].

1. Copy the first two columns to the right of $A$:
$$\begin{matrix} 2 & 1 & 3 & 2 & 1 \\ 0 & -1 & 4 & 0 & -1 \\ 5 & 2 & 1 & 5 & 2 \end{matrix}$$
2. Multiply along the three diagonals that go down to the right, and add:
$$2 \cdot (-1) \cdot 1 + 1 \cdot 4 \cdot 5 + 3 \cdot 0 \cdot 2 = -2 + 20 + 0 = 18.$$
3. Multiply along the three diagonals that go up to the right, starting in the bottom row, and add:
$$5 \cdot (-1) \cdot 3 + 2 \cdot 4 \cdot 2 + 1 \cdot 0 \cdot 1 = -15 + 16 + 0 = 1.$$
4. Subtract the second sum from the first: $\det A = 18 - 1 = 17$.
5. For the check, expand along column $1$, whose entries are $2$, $0$ and $5$, with the signs $+, -, +$:
$$\det A = 2 \det \begin{pmatrix} -1 & 4 \\ 2 & 1 \end{pmatrix} - 0 + 5 \det \begin{pmatrix} 1 & 3 \\ -1 & 4 \end{pmatrix}.$$
6. The two $2 \times 2$ determinants are $(-1) \cdot 1 - 4 \cdot 2 = -9$ and $1 \cdot 4 - 3 \cdot (-1) = 7$.
7. So $\det A = 2 \cdot (-9) + 5 \cdot 7 = -18 + 35 = 17$, the same value.

## Remarks

The example shows how negative entries enter the rule.
The up diagonal through $5$, $-1$ and $3$ has the product $-15$, and subtracting it adds $15$ to the total.
If you drop that sign and subtract $15 + 16 = 31$, you get $18 - 31 = -13$, which is wrong.

The value also depends on each entry in a simple way.
Replace $a_{22} = -1$ by a variable $t$.
Only the main down diagonal and the up diagonal through $a_{22}$ change, and
$$\det A = (2t + 20 + 0) - (15t + 16 + 0) = 4 - 13t.$$
So the determinant is a linear function of $t$, as the multilinearity of the determinant predicts, and $t = -1$ gives $4 + 13 = 17$ again.
The matrix is not invertible exactly when $t = 4/13$, which is not an integer.

## Explanations

### L1 human

We add three products going down and subtract three products going up.
The down products are $-2$, $20$ and $0$, with sum $18$.
The up products are $-15$, $16$ and $0$, with sum $1$.
So the determinant is $18 - 1 = 17$.

### L2 human

The check uses a column with a zero in it, so it needs only two $2 \times 2$ determinants instead of three.
That is a good habit for every hand computation: expand along the row or column with the most zeros.
Two methods that agree give much more confidence than one method done twice, because a slip in a sign rarely repeats in the same way.
