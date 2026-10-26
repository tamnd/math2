---
tag: 0TZAG60ZYT
kind: statement
role: theorem
name: Row rank equals column rank
msc: [15A03]
uses: [0EWQEYRVA8, 0EP73HK4C4, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proofs that column rank = row rank
---

## Statement

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Then the dimension of the [[row space|069MCGX635]] of $A$ equals the dimension of the [[column space|03AJKXH1AV]] of $A$.
Equivalently, $\rank A^T = \rank A$, where $A^T$ is the [[transpose|09DXWYRD43]].

## Remarks

One proof uses row reduction: row operations keep the row space and the dimension of the column space.
In reduced row echelon form, both dimensions equal the number of pivots.
Another proof uses the [[annihilator|0ASHNYF7AG]]: the dual map has the transposed matrix and the same rank.
Over $\C$, also $\rank A^* = \rank A$.

## Explanations

### L1 human

The number of independent rows of a matrix always equals the number of independent columns.
This is surprising, because rows and columns live in different spaces.
For a $3 \times 5$ matrix, it shows at once that the rank is at most $3$.
