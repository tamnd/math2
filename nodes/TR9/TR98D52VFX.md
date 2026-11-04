---
kind: statement
msc:
- 15A18
- 15B57
name: Orthogonal diagonalizability of real matrices
role: theorem
sources:
- locator: src/section7-1.xml:988
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-1.xml#L988
tag: TR98D52VFX
uses:
- 0W02QESPJQ
- 0VR671PHE5
- 07SQCNV233
- 0DGZBQWZWN
---

## Statement

Let $A$ be a real square matrix.
Then $A$ is orthogonally diagonalizable if and only if $A$ is a [[symmetric matrix|0VR671PHE5]].

Here, orthogonally diagonalizable means that there are an [[orthogonal matrix|0W02QESPJQ]] $Q$ and a diagonal matrix $D$ with $A = Q D Q^T$.
This is a special case of a [[diagonalisable matrix|07SQCNV233]].

## Remarks

If $A = Q D Q^T$, then $A^T = Q D^T Q^T = Q D Q^T = A$, so $A$ is symmetric.
The other direction is the real case of the [[spectral theorem for Hermitian matrices|0DGZBQWZWN]].
