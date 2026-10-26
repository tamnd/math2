---
tag: 09E1RCZ7YT
kind: statement
role: proposition
name: Trace of a transpose
msc: [15A15]
uses: [07PTPSZPME, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Basic properties
---

## Statement

Let $R$ be a commutative ring and let $A$ be an $n \times n$ matrix over $R$.
Then $\tr(A^T) = \tr A$, where $A^T$ is the [[transpose|09DXWYRD43]] of $A$ and $\tr$ is the [[trace|0XC1RDBY7A]].

## Remarks

The transpose does not move the entries on the main diagonal, so the sum of the diagonal entries stays the same.
For a complex matrix, $\tr(A^*) = \overline{\tr A}$.

## Explanations

### L1 human

Transposing flips a matrix over its diagonal.
The diagonal itself does not move.
So the trace, which only sees the diagonal, does not change.
