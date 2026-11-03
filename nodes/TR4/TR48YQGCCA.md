---
tag: TR48YQGCCA
kind: statement
role: theorem
name: Rank–nullity theorem for matrices
msc: [15A03, 15A04]
uses: [0ZC9YTXZRY, 0PHDYNR24D, 0APCFW7639]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4974
    locator: ap-linear-algebra.tex:4974
---

## Statement

Let $A$ be a matrix with $n$ columns.
Let $r$ be the [[rank|0ZC9YTXZRY]] of $A$.
Let $k$ be the [[nullity|0APCFW7639]] of $A$, that is, the dimension of the [[kernel|0PHDYNR24D]] of $A$.
Then the number of columns is the sum of the rank and the nullity:
$$n = r + k.$$

## Remarks

The kernel of $A$ is the set of vectors $x$ with $Ax = 0$.
It is a subspace of the space of column vectors with $n$ entries.
So the claim says that the dimension of that space splits into the part that $A$ keeps, the rank, and the part that $A$ sends to zero, the nullity.
