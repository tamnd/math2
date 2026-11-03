---
tag: EBNX02VRSD
kind: definition
name: Lie subalgebra
msc: [17B05]
defines: WKSSTQ69AK
uses: [5JJYBJ6A8K, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
A *Lie subalgebra* of $\mathfrak g$ is a [[linear subspace|00YC1D652K]] $\mathfrak h \subseteq \mathfrak g$ such that $[x, y] \in \mathfrak h$ for all $x, y \in \mathfrak h$.

## Remarks

Example: in $\mathfrak{gl}_n(k)$, the space $\mathfrak b_n$ of upper triangular matrices is a subalgebra.
If $A$ and $B$ are upper triangular, so are $AB$ and $BA$, hence so is $[A, B] = AB - BA$.

Non-example: the symmetric matrices in $\mathfrak{gl}_2(\R)$ form a subspace but not a subalgebra.
For $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, the bracket is $[A, B] = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which is not symmetric.

A subalgebra $\mathfrak h$ with the restricted bracket is itself a Lie algebra.
The intersection of subalgebras is a subalgebra, so each subset generates a smallest subalgebra containing it.
