---
tag: AMFJCC9M7G
kind: statement
role: proposition
name: An orthogonal set of nonzero vectors is linearly independent
msc: [15A63, 46C05]
uses: [0Y2X7P2WB7, 0CRMGPAH83]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L314
    locator: src/section6-3.xml:314
---

## Statement

Let $w_1, \ldots, w_n$ be vectors of $\R^m$. Assume that they are nonzero and that any two of them are [[orthogonal|0Y2X7P2WB7]] under the dot product. Then $w_1, \ldots, w_n$ are [[linearly independent|0CRMGPAH83]].

## Remarks

An orthogonal set here means a set of nonzero vectors that are pairwise orthogonal. The zero vector must be excluded, since a set that contains it is dependent.

Suppose $c_1 w_1 + \cdots + c_n w_n = 0$. Take the dot product with $w_j$. Every term except the $j$-th vanishes, so $c_j \, w_j \cdot w_j = 0$. As $w_j \ne 0$, we get $c_j = 0$.
