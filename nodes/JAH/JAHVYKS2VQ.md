---
kind: statement
msc:
- 65F20
- 15A23
name: Least-squares solution from a QR factorization
role: theorem
sources:
- locator: src/section6-5.xml:1325
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-5.xml#L1325
tag: JAHVYKS2VQ
uses:
- 0BYTQ4X1HC
- 0ERWG4NXQ9
about:
- 0BYTQ4X1HC
---

## Statement

Let $A$ be a real $m \times n$ matrix whose columns are linearly independent, and let $b \in \R^m$.
Suppose $A = QR$ is a [[QR factorization|0ERWG4NXQ9]] of $A$, where $Q$ has orthonormal columns and $R$ is an invertible upper triangular matrix.
Then the [[least squares|0BYTQ4X1HC]] solution $\hat x$ of $Ax = b$ is
$$\hat x = R^{-1} Q^T b.$$

## Remarks

The normal equations $A^T A \hat x = A^T b$ become $R^T R \hat x = R^T Q^T b$, because $Q^T Q$ is the identity.
Since $R^T$ is invertible, this reduces to $R \hat x = Q^T b$.
In practice one solves this triangular system by back substitution instead of forming $R^{-1}$.
