---
tag: 447DVQAVA8
kind: definition
name: Irreducible Lie module
msc: [17B10]
defines: HFW8642GBK
uses: [5JJYBJ6A8K, TZAZ163QGK]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_representation
---

## Definition

Let $\mathfrak{g}$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $F$, and let $V$ be a $\mathfrak{g}$-[[module|TZAZ163QGK]].
A *submodule* of $V$ is a subspace $W$ with $x \cdot w \in W$ for all $x \in \mathfrak{g}$ and $w \in W$.
The module $V$ is *irreducible* if $V \ne 0$ and the only submodules of $V$ are $0$ and $V$.

## Remarks

Example: $\mathfrak{sl}_2(F)$ acting on $F^2$ by matrix multiplication.
A submodule $W$ with $W \ne 0, F^2$ would be a line preserved by $e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, hence $W = F e_1$, the only line that $e$ preserves.
But $f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ sends $e_1$ to $e_2 \notin W$, so no such $W$ exists.
Non-example: the Lie algebra $\mathfrak{b}$ of upper triangular $2 \times 2$ matrices acting on $F^2$; the line $F e_1$ is a submodule different from $0$ and $F^2$.
An irreducible representation is also called a simple module.
The zero module is not irreducible, by convention.
