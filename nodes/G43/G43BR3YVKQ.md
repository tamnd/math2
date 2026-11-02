---
tag: G43BR3YVKQ
kind: definition
name: Nondegenerate critical point
msc: [57R70, "58E05", 58K05]
defines: MGPPCDFQDG
uses: [F45VQ47GPV, 0V33BNKZ9S, 0YTCMFB4HC, 0693Y2METT, 0AXZNE5XNH, 01NHFZF2SK]
sources:
  - url: https://en.wikipedia.org/wiki/Morse_theory
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$ and let $f \colon M \to \R$ be a [[smooth function|0V33BNKZ9S]].
Let $p$ be a [[critical point|0YTCMFB4HC]] of $f$, so $df_p = 0$.
The *Hessian* of $f$ at $p$ is the [[symmetric bilinear form|0AXZNE5XNH]] on $T_p M$ given by
$$\operatorname{Hess}_p f(v, w) = v\big(W f\big),$$
where $W$ is any vector field with $W(p) = w$.
The critical point $p$ is *nondegenerate* if $\operatorname{Hess}_p f$ is a [[nondegenerate bilinear form|01NHFZF2SK]].
Otherwise $p$ is *degenerate*.

## Remarks

Because $df_p = 0$, the value $v(Wf)$ does not depend on the extension $W$ of $w$, and the form is symmetric.
In a chart $(x_1, \dots, x_n)$ around $p$, $\operatorname{Hess}_p f$ has the matrix $\big(\partial^2 f / \partial x_i \partial x_j (p)\big)$, the [[Hessian matrix|0693Y2METT]], and $p$ is nondegenerate if and only if this matrix is invertible.

Example: $f(x, y) = x^2 + xy + y^2$ on $\R^2$ has the critical point $(0, 0)$ with Hessian matrix $\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$.
Its determinant is $3 \ne 0$, so the origin is nondegenerate.

Non-example: $g(x, y) = x^2 + y^4$ has the critical point $(0, 0)$ with Hessian matrix $\begin{pmatrix} 2 & 0 \\ 0 & 0 \end{pmatrix}$, which is singular, so the origin is degenerate.

Nondegenerate critical points are isolated among critical points.
A function all of whose critical points are nondegenerate is a [[Morse function|KPQ96640ZJ]].
