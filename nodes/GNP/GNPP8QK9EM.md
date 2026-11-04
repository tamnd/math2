---
tag: GNPP8QK9EM
kind: statement
role: proposition
name: Transpose times a vector gives the dot products with the columns
msc: [15A99]
uses: [09DXWYRD43, 0PDVQEP0ZC, 0S52TNNTH9]
about: [09DXWYRD43]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L798
    locator: src/section6-2.xml:798
---

## Statement

Let $A$ be an $m \times n$ real matrix with columns $v_1, \ldots, v_n$, each a vector in $\mathbb{R}^m$. Let $x$ be a vector in $\mathbb{R}^m$.

Then the [[matrix-vector product|0PDVQEP0ZC]] of the [[transpose|09DXWYRD43]] $A^T$ with $x$ is the column vector with $n$ entries whose $i$-th entry is the [[dot product|0S52TNNTH9]] $v_i \cdot x$.

## Remarks

The rows of $A^T$ are the columns of $A$. So entry $i$ of $A^T x$ is the dot product of row $i$ of $A^T$ with $x$, which is $v_i \cdot x$.
