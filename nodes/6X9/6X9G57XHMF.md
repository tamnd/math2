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

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}.$$

1. Over $\R$: subtract $4$ times row 1 from row 2, and $7$ times row 1 from row 3. The rows become $(1, 2, 3)$, $(0, -3, -6)$, $(0, -6, -12)$.
2. Subtract $2$ times row 2 from row 3. The [[echelon form|0F27PBRWD7]] has rows $(1, 2, 3)$, $(0, -3, -6)$, $(0, 0, 0)$, with two pivots. So the [[rank|0EWQEYRVA8]] over $\R$ is $2$.
3. Check by a column relation: $a_1 - 2a_2 + a_3 = (1 - 4 + 3,\ 4 - 10 + 6,\ 7 - 16 + 9) = (0, 0, 0)$.
4. Check by the [[determinant|0C3CFHDN6R]]: $\det A = 1(45 - 48) - 2(36 - 42) + 3(32 - 35) = -3 + 12 - 9 = 0$, while the minor $\det \begin{pmatrix} 1 & 2 \\ 4 & 5 \end{pmatrix} = -3 \ne 0$.
5. Over $\mathbb{F}_3$: reduce the entries modulo $3$. The rows become $(1, 2, 0)$, $(1, 2, 0)$, $(1, 2, 0)$.
6. All three rows are equal and nonzero. So the rank over $\mathbb{F}_3$ is $1$.

## Remarks

- The rank depends on the field of the entries. Here it drops from $2$ to $1$ when the entries are read modulo $3$.
- The minor $-3$ of step 4 is $0$ modulo $3$, which explains the drop. All $2 \times 2$ minors of $A$ are multiples of $3$.

## Explanations

### L1 human

The rows of this matrix are in arithmetic progression, so the third row is a combination of the first two.
So the rank is $2$ and not $3$.

### L2 human

Over $\mathbb{F}_3$, all three rows become equal, and the rank drops to $1$.
For a matrix with integer entries, the rank over $\mathbb{F}_p$ is at most the rank over $\Q$, because a minor that is nonzero modulo $p$ is also nonzero over $\Q$.
