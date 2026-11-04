---
tag: ~d2ad52bf
kind: concept
name: Orthogonally diagonalisable matrix
aliases: [orthogonally-diagonalizable-matrix]
msc: [15A21, 15B10]
uses: [0S9GGTR0EX, 0N6960W0BV, 0W02QESPJQ, 07SQCNV233]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-1.xml#L758
    locator: src/section7-1.xml:758
---

## Summary

A real $n \times n$ matrix $A$ is orthogonally diagonalisable when $\mathbb{R}^n$ has an [[orthonormal basis|0S9GGTR0EX]] made of [[eigenvectors|0N6960W0BV]] of $A$.

Placing the vectors of such a basis as the columns of a matrix $Q$ gives an [[orthogonal matrix|0W02QESPJQ]]. Then $A = QDQ^T$, where $D$ is the diagonal matrix of the matching eigenvalues. So $A$ is a special case of a [[diagonalisable matrix|07SQCNV233]], where the change of basis can be chosen orthogonal.
