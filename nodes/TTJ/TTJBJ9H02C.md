---
tag: TTJBJ9H02C
kind: statement
role: proposition
name: Transpose of a singular value decomposition
msc: [15A18, 15A23]
uses: [000NPTMX6J, 09VMDSRXWJ]
about: [000NPTMX6J]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L1240
    locator: src/section7-4.xml:1240
---

## Statement

Let $A$ be a real matrix with a [[singular value decomposition|000NPTMX6J]] $A = U \Sigma V^T$, where $U$ and $V$ are orthogonal and $\Sigma$ has the [[singular values|09VMDSRXWJ]] of $A$ on its diagonal.

Then $A^T = V \Sigma^T U^T$, and this is a singular value decomposition of $A^T$.

Hence $A$ and $A^T$ have the same singular values.

The left singular vectors of $A$ (the columns of $U$) are the right singular vectors of $A^T$.

The right singular vectors of $A$ (the columns of $V$) are the left singular vectors of $A^T$.

## Remarks

The proof is one line: transpose both sides and reverse the order of the factors. The matrix $\Sigma^T$ is again diagonal with the same nonnegative entries, but it has the shape $n \times m$.
