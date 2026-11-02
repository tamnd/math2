---
tag: RPSYWTKB4V
kind: definition
name: Singularity of a smooth map
msc: [58K05, 57R45, 58K15]
defines: 1JG3HFWX3T
uses: [F45VQ47GPV, 6P9PXQDSEN, 0ZZXSBTR4J]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Definition

Let $M$ and $N$ be [[smooth manifolds|F45VQ47GPV]] of dimensions $m$ and $n$, and let $f \colon M \to N$ be a smooth map.
For $p \in M$, let $df_p \colon T_p M \to T_{f(p)} N$ be the [[differential|6P9PXQDSEN]] of $f$ at $p$.
The point $p$ is a *singular point*, or *singularity*, of $f$ if the [[rank|0ZZXSBTR4J]] of $df_p$ is less than $\min(m, n)$.
Otherwise $p$ is a *regular point* of $f$.
The set of singular points of $f$ is denoted $\Sigma(f)$.

## Remarks

Example: $f \colon \R^2 \to \R^2$, $f(x, y) = (x, y^2)$, has $df_{(x,y)} = \begin{pmatrix} 1 & 0 \\ 0 & 2y \end{pmatrix}$, of rank $1 < 2$ exactly when $y = 0$.
So $\Sigma(f)$ is the line $y = 0$, along which $f$ folds the plane.
Non-example: for $f \colon \R \to \R^2$, $f(t) = (t, t^2)$, the differential $df_t$ has matrix $(1, 2t)^T$ of rank $1 = \min(1, 2)$ at every $t$, so $f$ has no singular points.
A point is regular if and only if $f$ is an [[immersion|6RW68JGBHC]] near it (when $m \le n$) or a [[submersion|BMY55EW3RF]] near it (when $m \ge n$).
For $N = \R$ the singular points are the [[critical points|0YTCMFB4HC]] of $f$, where $df_p = 0$.
Some authors call every point with $df_p$ not surjective a critical point; this agrees with the definition above when $m \ge n$.
