---
tag: 4JVKH43WYP
kind: statement
role: proposition
name: Matrix with orthonormal columns has Q transpose Q equal to the identity
msc: [15A63, 15B10]
uses: [0RW9TNNT87, 09DXWYRD43]
about: [0W02QESPJQ]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-3.xml#L600
    locator: src/section6-3.xml:600
---

## Statement

Let $Q$ be a real $m \times n$ matrix.
Suppose that the columns of $Q$ form an [[orthonormal family|0RW9TNNT87]].
Then the product of the [[transpose|09DXWYRD43]] of $Q$ with $Q$ is the $n \times n$ identity matrix:
$$Q^T Q = I_n.$$

## Remarks

The entry in row $i$ and column $j$ of $Q^T Q$ is the dot product of the $i$-th and $j$-th columns of $Q$.
This dot product is $1$ when $i = j$ and $0$ otherwise, because the columns are unit vectors that are pairwise orthogonal.
The matrix $Q$ need not be square. When it is square, it is an [[orthogonal matrix|0W02QESPJQ]].
