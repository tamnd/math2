---
tag: R35CBH1NPB
kind: definition
name: Lie ideal
msc: [17B05]
defines: JWMTXQ8A3A
uses: [5JJYBJ6A8K, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra
---

## Definition

Let $\mathfrak g$ be a [[Lie algebra|5JJYBJ6A8K]] over a field $k$.
An *ideal* of $\mathfrak g$ is a [[linear subspace|00YC1D652K]] $\mathfrak a \subseteq \mathfrak g$ such that $[x, a] \in \mathfrak a$ for all $x \in \mathfrak g$ and $a \in \mathfrak a$.

## Remarks

Since $[a, x] = -[x, a]$, there is no difference between left and right ideals.
Every ideal is a [[Lie subalgebra|WKSSTQ69AK]].
If $\mathfrak a$ is an ideal, the quotient space $\mathfrak g / \mathfrak a$ is a Lie algebra with $[x + \mathfrak a, y + \mathfrak a] = [x, y] + \mathfrak a$.

Example: $\mathfrak{sl}_n(k)$, the trace-zero matrices, is an ideal of $\mathfrak{gl}_n(k)$.
For all $X, Y$ one has $\tr(XY) = \tr(YX)$, so $\tr [X, Y] = 0$, and $[X, Y] \in \mathfrak{sl}_n(k)$.

Non-example: in $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$, take $h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and $e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
The line $k h$ is a subalgebra but not an ideal, because $[e, h] = -2e$ is not a multiple of $h$.
