---
tag: 6VFADXR4MW
kind: definition
name: Pseudo-Riemannian manifold
msc: [53B30, 53C50]
defines: GH6CXWFNDJ
uses: [F45VQ47GPV, WY6K3P4YCG, WX302T93TW, 0AXZNE5XNH, 01NHFZF2SK, 07EZA80NEH]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-Riemannian_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] of dimension $n$, with [[tangent spaces|WY6K3P4YCG]] $T_pM$.
A *pseudo-Riemannian metric* on $M$ is a smooth symmetric $(0, 2)$-[[tensor field|WX302T93TW]] $g$ on $M$ such that:

1. for each $p \in M$, the map $g_p \colon T_pM \times T_pM \to \R$ is a [[symmetric bilinear form|0AXZNE5XNH]];
2. for each $p \in M$, the form $g_p$ is [[nondegenerate|01NHFZF2SK]]: if $g_p(v, w) = 0$ for all $w \in T_pM$, then $v = 0$;
3. the [[signature|07EZA80NEH]] of $g_p$ is the same for all $p \in M$.

A *pseudo-Riemannian manifold* is a pair $(M, g)$ of a smooth manifold $M$ and a pseudo-Riemannian metric $g$ on $M$.

## Remarks

Example: on $\R^2$ with coordinates $(t, x)$, let $g = -dt^2 + dx^2$.
At each point its matrix is $\operatorname{diag}(-1, 1)$, which is symmetric with nonzero determinant, so $g$ is nondegenerate with constant signature: $(\R^2, g)$ is pseudo-Riemannian.

Non-example: on $\R^2$, let $g = dt^2 + t \, dx^2$.
Its matrix $\operatorname{diag}(1, t)$ is degenerate where $t = 0$, so clause 2 fails on the line $t = 0$.

On a connected manifold, clause 3 follows from clause 2 and continuity, since the signature can only change where the determinant of $g$ vanishes.
A Riemannian metric is the case where $g_p$ is positive definite at every point.
In local coordinates $(x^1, \ldots, x^n)$ one writes $g = \sum_{i,j} g_{ij} \, dx^i \, dx^j$ with a symmetric invertible matrix $(g_{ij})$.
