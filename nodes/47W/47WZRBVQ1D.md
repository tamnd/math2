---
tag: 47WZRBVQ1D
kind: definition
name: Wolfe conditions
msc: [90C30, 65K05]
defines: E1F970GGRC
uses: [B6T5HA74QW, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Wolfe_conditions
---

## Definition

Let $f \colon \R^n \to \R$ be continuously differentiable, with [[gradient|0ABK9V9Y64]] $\nabla f$.
Let $x \in \R^n$ and let $p$ be a descent direction at $x$, that is, $\nabla f(x)^T p < 0$.
Fix constants $0 < c_1 < c_2 < 1$.
A step length $\alpha > 0$ satisfies the *Wolfe conditions* if:

1. (sufficient decrease, or Armijo condition) $f(x + \alpha p) \le f(x) + c_1 \alpha \nabla f(x)^T p$;
2. (curvature condition) $\nabla f(x + \alpha p)^T p \ge c_2 \nabla f(x)^T p$.

It satisfies the *strong Wolfe conditions* if it satisfies clause 1 and $\abs{\nabla f(x + \alpha p)^T p} \le c_2 \abs{\nabla f(x)^T p}$.

## Remarks

In terms of $\varphi(\alpha) = f(x + \alpha p)$, the conditions read $\varphi(\alpha) \le \varphi(0) + c_1 \alpha \varphi'(0)$ and $\varphi'(\alpha) \ge c_2 \varphi'(0)$.
Typical values in quasi-Newton methods are $c_1 = 10^{-4}$ and $c_2 = 0.9$.

Example: $f(x) = x^2$ on $\R$, $x = 1$, $p = -1$, $c_1 = 10^{-4}$, $c_2 = 0.9$.
Then $\varphi(\alpha) = (1 - \alpha)^2$ and $\varphi'(\alpha) = -2(1 - \alpha)$, so $\varphi'(0) = -2$.
For $\alpha = 1$: $\varphi(1) = 0 \le 1 - 2 \cdot 10^{-4}$, and $\varphi'(1) = 0 \ge -1.8$, so both conditions hold.

Non-example: in the same setting, $\alpha = 0.01$ satisfies clause 1, but $\varphi'(0.01) = -1.98 < -1.8$, so it fails clause 2.
The step $\alpha = 2$ fails clause 1, since $\varphi(2) = 1 > 1 - 4 \cdot 10^{-4}$.

If $f$ is bounded below along the ray $\set{x + \alpha p : \alpha > 0}$, then there is an interval of step lengths that satisfy the strong Wolfe conditions.
In a quasi-Newton method, clause 2 gives $y^T s \ge (c_2 - 1) \alpha \nabla f(x)^T p > 0$, which keeps the BFGS update positive definite.
