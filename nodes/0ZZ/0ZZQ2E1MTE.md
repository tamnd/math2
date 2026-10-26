---
tag: 0ZZQ2E1MTE
kind: statement
role: proposition
name: Determinant of a transpose
msc: [15A15]
uses: [0C3CFHDN6R, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Let $K$ be a commutative ring and let $A$ be an $n \times n$ matrix over $K$.
Then $\det A^T = \det A$, where $A^T$ is the [[transpose|09DXWYRD43]] of $A$ and $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

In the [[Leibniz formula|016PE4VZ8Q]], the term of $\sigma$ for $A^T$ equals the term of $\sigma^{-1}$ for $A$, and $\sgn(\sigma^{-1}) = \sgn(\sigma)$.
So each property of the determinant for rows also holds for columns.

## Explanations

### L1 human

Exchanging rows and columns does not change the determinant.
So we can expand, reduce or test a determinant by columns as well as by rows.
Every rule for rows has a twin rule for columns.
