---
tag: 0KMN32XGPF
kind: statement
role: proposition
name: Determinant of a linear map is the determinant of its matrix
msc: [15A04, 15A15]
uses: [03F5KP94K0, 0YYMY95FWS]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Determinant of an endomorphism
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$ with a basis $B$, and let $T \colon V \to V$ be a linear map.
Then the [[determinant of $T$|0X0HQYSZ0K]] equals the determinant of the [[matrix of $T$|0YQSGNYE3K]] in $B$:
$$\det T = \det [T]_B.$$

## Remarks

The key fact is $\det(P^{-1} A P) = \det A$, which follows from the product rule.
Over a commutative ring, the same statement holds for free modules of finite rank.

## Explanations

### L1 human

We can compute the determinant of a linear map in any basis.
We write its matrix in that basis, and we take the determinant of the matrix.
Every basis gives the same answer.
