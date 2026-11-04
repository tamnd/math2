---
kind: statement
name: QR factorization of a matrix with independent columns
msc:
- 15A23
role: proposition
sources:
- url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-4.xml#L1118
  locator: src/section6-4.xml:1118
tag: P5S1MTTDP8
uses:
- 0EVHJFTG9Z
- 0F0RPPJ2TT
- 0N4XY7Z3NN
- 0VT6P0GNQR
---

## Statement

Let $A$ be an $m \times n$ matrix whose columns are [[linearly independent|0EVHJFTG9Z]].
Then $A$ factors as $A = QR$.
Here $Q$ is an $m \times n$ matrix whose columns form an orthonormal basis of the [[column space|0F0RPPJ2TT]] of $A$.
The factor $R$ is an $n \times n$ [[upper triangular matrix|0N4XY7Z3NN]].

## Remarks

The columns of $Q$ come from applying the [[Gram–Schmidt process|0VT6P0GNQR]] to the columns of $A$.
The matrix $R$ records how each column of $A$ is built from the columns of $Q$.
