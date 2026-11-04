---
kind: statement
msc:
- 15A04
- 15A09
name: Composition of matrix transformations is the matrix transformation of the product
role: proposition
sources:
- locator: src/section2-5.xml:1001
  url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-5.xml#L1001
tag: MH8YBQPZ7H
uses:
- 032Q9FB8MT
---

## Statement

Let $T \colon \mathbb{R}^n \to \mathbb{R}^m$ be a matrix transformation given by an $m \times n$ matrix $A$.
Let $S \colon \mathbb{R}^m \to \mathbb{R}^p$ be a matrix transformation given by a $p \times m$ matrix $B$.
Then the composition $S \circ T \colon \mathbb{R}^n \to \mathbb{R}^p$ is again a matrix transformation.
Its matrix is the [[matrix product|032Q9FB8MT]] $BA$.

## Remarks

In formulas, $S(T(\mathbf{x})) = B(A\mathbf{x}) = (BA)\mathbf{x}$ for every $\mathbf{x}$ in $\mathbb{R}^n$.
The matrix of the map that acts first stands on the right.
