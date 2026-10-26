---
tag: 009CY8JXFX
kind: statement
role: proposition
name: Scaling a row scales the determinant
msc: [15A15]
uses: [0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Basic rules
---

## Statement

Let $K$ be a commutative ring, let $A$ be an $n \times n$ matrix over $K$, and let $c \in K$.
Let $B$ be the matrix that results when one row of $A$ is multiplied by $c$.
Then $\det B = c \det A$, where $\det$ is the [[determinant|00KDZRW4C0]].

## Remarks

This is a special case of [[linearity in each row|0PPG793642]].
It describes the effect of the scaling [[row operation|04XWH28452]] on the determinant.
Scaling all $n$ rows gives $\det(cA) = c^n \det A$, see [[the determinant of a scalar multiple|01EXSMK864]].

## Explanations

### L1 human

If we stretch one edge of a box by the factor $c$, then its volume is multiplied by $c$.
The determinant behaves in the same way.
For example, doubling one row doubles the determinant.
