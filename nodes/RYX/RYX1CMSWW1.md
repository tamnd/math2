---
tag: RYX1CMSWW1
kind: proof
name: Proof that the trace is linear
msc: [15A15]
proves: 0GJWQZCPZM
uses: [07PTPSZPME, 0BVXADM10P, 0K28YXMS7Q]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Basic properties
---

## Proof

We compute both traces from the diagonal entries.

1. Write $A = (a_{ij})$ and $B = (b_{ij})$, with $1 \le i, j \le n$.
2. By the definition of [[matrix addition|0BVXADM10P]], the diagonal entries of $A + B$ are $(A + B)_{ii} = a_{ii} + b_{ii}$.
3. By the definition of the [[trace|07PTPSZPME]], $\tr(A + B) = \sum_{i=1}^{n} (a_{ii} + b_{ii})$.
4. Addition in $R$ is associative and commutative, so this finite sum splits as $\sum_{i} a_{ii} + \sum_{i} b_{ii} = \tr A + \tr B$.
5. By the definition of the [[scalar multiple|0K28YXMS7Q]], the diagonal entries of $cA$ are $(cA)_{ii} = c\, a_{ii}$.
6. So $\tr(cA) = \sum_{i=1}^{n} c\, a_{ii}$. By the distributive law in $R$, this equals $c \sum_{i=1}^{n} a_{ii} = c \tr A$.

## Idea

The trace only sees the diagonal. Adding matrices or scaling a matrix acts on each diagonal entry separately, so the sum of the diagonal behaves in the same way.
