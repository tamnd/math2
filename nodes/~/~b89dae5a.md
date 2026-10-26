---
tag: ~b89dae5a
kind: statement
role: proposition
name: One-sided inverse of a square matrix is two-sided
msc: [15A09]
uses: [~63729221]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Statement

Let $F$ be a field and let $A$ and $B$ be $n \times n$ matrices over $F$.
If $BA = I_n$, then $AB = I_n$, so $A$ is [[invertible|~1c77fde7]] and $A^{-1} = B$.
The same holds with the roles of $A$ and $B$ exchanged.

## Remarks

The statement also holds over each commutative ring, by the [[determinant|~362fc72a]]: $BA = I_n$ gives $\det B \det A = 1$.
For non-square matrices it fails: a $2 \times 1$ matrix can have a left inverse but never a right inverse.
A proof over a field uses [[rank–nullity|~dbabb598]]: $BA = I_n$ makes $x \mapsto Ax$ injective, hence surjective.

## Explanations

### L1 human

For square matrices, we only need to check one of $AB = I$ and $BA = I$.
The other one then holds automatically.
This saves half of the work when we check an inverse.
