---
tag: FD7H5AM1R7
kind: definition
name: Differential-algebraic system of equations
msc: [34A09, 65L80]
defines: EY362KR0KB
uses: [0P97V20RW7, 047NDTEPCV, 0BXBADR94C]
sources:
  - url: https://en.wikipedia.org/wiki/Differential-algebraic_system_of_equations
---

## Definition

Let $I \subseteq \R$ be an open interval, let $\Omega \subseteq \R^n \times \R^n$ be an open set, and let $F : I \times \Omega \to \R^n$ be continuously differentiable.
Write $F = F(t, x, p)$ with $t \in I$ and $x, p \in \R^n$.
The system
$$F(t, x(t), x'(t)) = 0$$
is a *differential-algebraic system of equations* if the [[Jacobian matrix|047NDTEPCV]] $\partial F / \partial p$ of size $n \times n$ is singular at every point of $I \times \Omega$.
A solution is a differentiable map $x$ on a subinterval of $I$ with $(x(t), x'(t)) \in \Omega$ and $F(t, x(t), x'(t)) = 0$ for each $t$.

## Remarks

Example: for $x = (u, w)$, take the system $u' = -u + w$ and $0 = u - w + \sin t$.
Here $F(t, x, p) = (p_1 + u - w,\ u - w + \sin t)$ and $\partial F / \partial p$ has rows $(1, 0)$ and $(0, 0)$, so it is singular everywhere.
The constraint gives $w = u + \sin t$, hence $u' = \sin t$, so $u = C - \cos t$ and $w = C - \cos t + \sin t$.
Initial values must satisfy the constraint: $w(0) = u(0)$.
Non-example: if $\partial F / \partial p$ is invertible at a point, the [[implicit function theorem|0BXBADR94C]] solves for $x'$ near that point, and the system is locally an [[ordinary differential equation|0P97V20RW7]] $x' = f(t, x)$.
The form $u' = f(t, u, w)$, $0 = g(t, u, w)$ is called semi-explicit.
The differentiation index is the least number of differentiations of the system needed to determine $x'$ as a continuous function of $(t, x)$; the example above has index $1$.
