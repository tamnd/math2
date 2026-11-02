---
tag: MYQN2FX9SB
kind: definition
name: Morse function
msc: [57R70, "58E05", 58K05]
defines: KPQ96640ZJ
uses: [F45VQ47GPV, 0V33BNKZ9S, 0YTCMFB4HC, 0693Y2METT]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_theory
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, and let $f \colon M \to \R$ be a [[smooth function|0V33BNKZ9S]].
A point $p \in M$ is a [[critical point|0YTCMFB4HC]] of $f$ if $df_p = 0$.
A critical point $p$ is *nondegenerate* if, in some chart $(x_1, \dots, x_n)$ around $p$, the [[Hessian matrix|0693Y2METT]] $\big(\partial^2 f / \partial x_i \partial x_j(p)\big)$ is invertible.
The function $f$ is a *Morse function* if every critical point of $f$ is nondegenerate.
The *index* of a nondegenerate critical point is the number of negative eigenvalues of its Hessian.

## Remarks

At a critical point the Hessian transforms under a change of chart by $H \mapsto A^T H A$ with $A$ invertible, so nondegeneracy and the index do not depend on the chart.
Example: $f \colon \R^2 \to \R$, $f(x, y) = x^2 - y^2$, is a Morse function.
Its only critical point is the origin, where the Hessian is $\begin{pmatrix} 2 & 0 \\ 0 & -2 \end{pmatrix}$, which is invertible; the index is $1$.
Non-example: $g \colon \R \to \R$, $g(x) = x^3$, is not a Morse function.
Its critical point $0$ has Hessian $g''(0) = 0$, which is not invertible.
Nondegenerate critical points are isolated, so on a compact manifold a Morse function has only finitely many critical points.
On a compact manifold the Morse functions form an open dense subset of $C^\infty(M, \R)$.
