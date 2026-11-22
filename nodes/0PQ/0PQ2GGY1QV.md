---
tag: 0PQ2GGY1QV
kind: definition
name: Null space
msc: ["15A03", "15A06"]
topics: [S6559D61BP]
audience: ug1
defines: 0PHDYNR24D
uses: [02YFME3RGW, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: lead section
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section3-5.xml#L894
    locator: src/section3-5.xml:894
---

## Definition

The null space of a matrix is the set of solutions of the homogeneous system with that matrix.
Let $F$ be a field and let $A$ be an $m \times n$ [[matrix|0N1MY1T0W9]] over $F$.
The *null space* of $A$ is
$$\operatorname{Null}(A) = \{x \in F^n : Ax = 0\},$$
the [[kernel|02YFME3RGW]] of the linear map $F^n \to F^m$, $x \mapsto Ax$.

## Remarks

The vector $x$ ranges over $F^n$, because $Ax$ is defined only when $x$ has one entry for each column.
The right side is the zero vector of $F^m$, and this is what makes the solution set a subspace: sums and multiples of solutions of $Ax = 0$ are again solutions.
With a nonzero right side the solution set is not a subspace, since it does not contain $0$.

For example, the null space of $\begin{pmatrix} 1 & 1 \end{pmatrix}$ is the line in $F^2$ spanned by $(1, -1)$, since $x_1 + x_2 = 0$ means $x_2 = -x_1$.
Its dimension is $n - \operatorname{rank} A$, the [[nullity|0APCFW7639]] of $A$, by the [[free variable theorem|5NKND0CPKP]].
Row equivalent matrices have the same null space, and over $\mathbb{R}$ each vector of the null space is orthogonal to each row of $A$ for the dot product.
The [[concept page|0PHDYNR24D]] works examples, including the left null space $\operatorname{Null}(A^{\mathsf{T}})$.

## Explanations

### L1 human

The null space of a matrix is the set of solutions of $Ax = 0$.
A basis comes from row reduction: each free variable gives one basis vector.
For the equation $x_1 + x_2 = 0$, the solutions are the multiples of $(1, -1)$.
