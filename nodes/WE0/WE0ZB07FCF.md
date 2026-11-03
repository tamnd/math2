---
tag: WE0ZB07FCF
kind: proof
name: Proof that a matrix and its transpose have the same trace
msc: [15A15]
proves: 09E1RCZ7YT
uses: [07PTPSZPME, 0W809K6AW0]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Basic properties
---

## Proof

1. Write $A = (a_{ij})$, with $1 \le i, j \le n$. Then $A^T$ is also an $n \times n$ matrix.
2. By the definition of the [[transpose|0W809K6AW0]], $(A^T)_{ij} = a_{ji}$. Taking $j = i$ gives $(A^T)_{ii} = a_{ii}$ for each $i$.
3. By the definition of the [[trace|07PTPSZPME]] and step 2, $\tr(A^T) = \sum_{i=1}^{n} (A^T)_{ii} = \sum_{i=1}^{n} a_{ii} = \tr A$.

## Idea

The transpose reflects a matrix in its main diagonal. The diagonal entries stay where they are, so their sum does not change.
