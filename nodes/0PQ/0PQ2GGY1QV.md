---
tag: 0PQ2GGY1QV
kind: definition
name: Null space
msc: [15A03, 15A06]
defines: 0PHDYNR24D
uses: [02YFME3RGW, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
---

## Definition

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
The *null space* of $A$ is
$$\operatorname{Null}(A) = \{x \in F^n : Ax = 0\}.$$
It is the [[kernel|0S23E6YE83]] of the linear map $x \mapsto Ax$.

## Remarks

The null space is a subspace of $F^n$, of dimension $n - \rank A$, the [[nullity|0APCFW7639]] of $A$.
Row equivalent matrices have the same null space.
The null space of $\begin{pmatrix} 1 & 1 \end{pmatrix}$ is the line spanned by $(1, -1)^T$.
Each vector of the null space is orthogonal to each row of $A$, for the dot product.

## Explanations

### L1 human

The null space of a matrix is the set of solutions of $Ax = 0$.
We find a basis of it by row reduction: each free variable gives one basis vector.
It is the kernel of the matrix, viewed as a linear map.
