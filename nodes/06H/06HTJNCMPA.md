---
tag: 06HTJNCMPA
kind: statement
role: theorem
name: "Grassmann's formula"
aliases: [dimension-formula]
msc: [15A03]
uses: [0RMKABS2S5, 0V33SPH7RR, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Properties
---

## Statement

Let $F$ be a field, let $V$ be a vector space over $F$, and let $U$ and $W$ be finite-dimensional [[linear subspaces|00YC1D652K]] of $V$.
Then
$$\dim(U + W) + \dim(U \cap W) = \dim U + \dim W,$$
where $U + W$ is the [[sum of the subspaces|0JMTY8MF54]] and $\dim$ is the [[dimension|03GSZ8RTZJ]].

## Remarks

The proof extends a basis of $U \cap W$ to a basis of $U$ and to a basis of $W$.
Together, these vectors form a basis of $U + W$.
Another proof applies the [[rank–nullity theorem|0W4FSW1TVB]] to the map $U \times W \to V$, $(u, w) \mapsto u - w$.
Two planes through the origin in $\R^3$ with $U \ne W$ have $\dim(U + W) = 3$, so $\dim(U \cap W) = 1$.

## Explanations

### L1 human

The formula counts dimensions like a count of elements in a union of two sets.
We add the two dimensions, but then the common part is counted twice, so we subtract it once.
Two different planes through the origin in space always share at least a line.
