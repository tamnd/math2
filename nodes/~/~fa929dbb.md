---
kind: statement
name: A spanning set of R^m has at least m vectors
role: proposition
tag: ~fa929dbb
msc:
  - 15A03
uses:
  - 088RYKAWK9
  - 0XPR1E85W0
about:
  - 088RYKAWK9
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-3.xml#L1387
    locator: src/section2-3.xml:1387
---

## Statement

Let $m$ be a positive integer. Suppose a set of vectors of $\mathbb{R}^m$ [[spans|088RYKAWK9]] the whole of [[the space|0XPR1E85W0]] $\mathbb{R}^m$. Then the set has at least $m$ vectors.

## Remarks

Equivalently, a set with fewer than $m$ vectors in $\mathbb{R}^m$ never spans $\mathbb{R}^m$.

In matrix terms, the matrix whose columns are the vectors has $m$ rows. To span, it needs a pivot position in every row. Each column holds at most one pivot, so there must be at least $m$ columns.
