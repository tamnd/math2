---
tag: 0EWQEYRVA8
kind: definition
name: Rank of a matrix
msc: [15A03]
defines: 0ZC9YTXZRY
uses: [0F0RPPJ2TT, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
---

## Definition

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
The *rank* of $A$ is
$$\rank A = \dim \operatorname{Col}(A),$$
the [[dimension|03GSZ8RTZJ]] of the [[column space|03AJKXH1AV]] of $A$.

## Remarks

The rank is the maximal number of linearly independent columns of $A$.
It also equals the dimension of the row space, by [[row rank equals column rank|0TZAG60ZYT]].
It equals the number of pivots in a row echelon form of $A$, and the largest order of a nonzero minor of $A$.
An $n \times n$ matrix is invertible if and only if its rank is $n$.

## Explanations

### L1 human

The rank of a matrix counts how many of its columns are really independent.
For $\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the second column is twice the first, so the rank is $1$.
We compute the rank by row reduction and count the pivots.
