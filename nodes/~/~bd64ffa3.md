---
tag: ~bd64ffa3
kind: statement
role: proposition
name: Change of basis for a bilinear form
msc: [15A63, 15A21]
uses: [~f4279a01, ~fd97b3f3]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_congruence
    locator: lead section
---

## Statement

Let $F$ be a field and let $V$ be a finite-dimensional vector space over $F$, with two bases $\mathcal{B}$ and $\mathcal{B}'$.
Let $P$ be the [[change of basis matrix|~78c7aad5]] whose columns are the coordinate vectors of the vectors of $\mathcal{B}'$ in $\mathcal{B}$.
Let $B$ be a bilinear form on $V$, with [[matrix|~fed44dac]] $M$ in $\mathcal{B}$ and $M'$ in $\mathcal{B}'$.
Then
$$M' = P^T M P.$$

## Remarks

Two square matrices $M$ and $M'$ are *congruent* when $M' = P^T M P$ for an invertible matrix $P$.
So two matrices represent the same bilinear form in two bases if and only if they are congruent.
Congruence keeps the rank and the symmetry of a matrix, but in general not its eigenvalues.
Compare this with the rule $P^{-1} A P$ for the matrix of a linear map.

## Explanations

### L1 human

When we change the basis, the matrix of a bilinear form changes by $P^T M P$.
Both vectors change coordinates, so $P$ appears twice.
For a linear map, the rule is $P^{-1} A P$ instead.
