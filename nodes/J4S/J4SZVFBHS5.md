---
tag: J4SZVFBHS5
kind: statement
role: proposition
name: Orthogonal complement of the column space is the null space of the transpose
msc: [15A03, 15A18]
uses: [03AJKXH1AV, 0PQ2GGY1QV, 0W809K6AW0, 0XJXTBCB2T]
about: [03AJKXH1AV, 0PQ2GGY1QV]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L878
    locator: src/section6-2.xml:878
---

## Statement

Let $A$ be an $m \times n$ real matrix, with [[transpose|0W809K6AW0]] $A^T$.
Use the standard dot product on $\R^m$.
Then the [[orthogonal complement|0XJXTBCB2T]] of the [[column space|03AJKXH1AV]] of $A$ is the [[null space|0PQ2GGY1QV]] of $A^T$:
$$\operatorname{Col}(A)^\perp = \operatorname{Nul}(A^T).$$

## Remarks

A vector $y \in \R^m$ is orthogonal to the column space exactly when it is orthogonal to each column of $A$.
The dot product of $y$ with the $j$-th column of $A$ is the $j$-th entry of $A^T y$.
So $y$ is orthogonal to all columns exactly when $A^T y = 0$.
