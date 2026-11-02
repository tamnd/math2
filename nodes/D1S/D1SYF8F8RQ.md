---
tag: D1SYF8F8RQ
kind: definition
name: Lorentzian manifold
msc: [53C50, 53B30]
defines: BY4QYYS788
uses: [GH6CXWFNDJ, 07EZA80NEH]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-Riemannian_manifold
    locator: Lorentzian manifold
---

## Definition

Let $(M, g)$ be a [[pseudo-Riemannian manifold|GH6CXWFNDJ]] of dimension $n \ge 2$.
It is a *Lorentzian manifold* if, at each point $p \in M$, the form $g_p$ has [[signature|07EZA80NEH]] $(n - 1, 1)$.
That is, in a suitable basis of $T_pM$ the matrix of $g_p$ is $\operatorname{diag}(-1, 1, \ldots, 1)$.

## Remarks

Example: Minkowski space is $\R^n$ with coordinates $(t, x_1, \ldots, x_{n-1})$ and $g = -dt^2 + dx_1^2 + \cdots + dx_{n-1}^2$.
Its matrix is $\operatorname{diag}(-1, 1, \ldots, 1)$ at every point, with one negative and $n - 1$ positive entries.

Non-example: $\R^4$ with $g = -dt^2 - dx^2 + dy^2 + dz^2$ is pseudo-Riemannian, but its signature has two negative entries, so it is not Lorentzian.

Many physics texts use the opposite convention, signature $(1, n - 1)$, that is $\operatorname{diag}(1, -1, \ldots, -1)$; the two conventions differ by replacing $g$ with $-g$.
A nonzero tangent vector $v$ is called timelike if $g(v, v) < 0$, null if $g(v, v) = 0$, and spacelike if $g(v, v) > 0$ (in the convention used here).
