---
tag: DK2GB9VGT4
kind: definition
name: Line search
msc: [90C30, 65K05]
defines: B6T5HA74QW
uses: [0ABK9V9Y64, 06KWGHDN2J]
sources:
  - url: https://en.wikipedia.org/wiki/Line_search
---

## Definition

Let $f \colon \R^n \to \R$ be continuously differentiable, with [[gradient|0ABK9V9Y64]] $\nabla f$.
A vector $p \in \R^n$ is a *descent direction* at $x \in \R^n$ if $\nabla f(x)^T p < 0$.
A *line search method* builds a sequence $(x_k)$ by
$$x_{k+1} = x_k + \alpha_k p_k,$$
where $p_k$ is a descent direction at $x_k$ and $\alpha_k > 0$ is the *step length*.
The step length is chosen by examining the function $\varphi_k(\alpha) = f(x_k + \alpha p_k)$ of one variable $\alpha > 0$.
The line search is *exact* if $\alpha_k$ minimizes $\varphi_k$ over $\alpha > 0$; otherwise it is *inexact*.

## Remarks

Since $\varphi_k'(0) = \nabla f(x_k)^T p_k < 0$ is the [[directional derivative|06KWGHDN2J]] of $f$ along $p_k$, the function decreases for all small enough $\alpha > 0$.

Example: let $f(x) = \tfrac12 x^T A x - b^T x$ with $A$ symmetric positive definite, and let $g = \nabla f(x_k) = A x_k - b$.
Then $\varphi_k'(\alpha) = (g + \alpha A p_k)^T p_k$, so the exact step is $\alpha_k = -\dfrac{g^T p_k}{p_k^T A p_k}$, which is positive when $p_k$ is a descent direction.

Non-example: if $\nabla f(x_k)^T p_k > 0$, then $p_k$ is not a descent direction and $\varphi_k(\alpha) > f(x_k)$ for all small $\alpha > 0$.
Then no small step decreases $f$.

Common inexact rules are the Armijo condition, the [[Wolfe conditions|E1F970GGRC]] and [[backtracking line search|J99056ZFE6]].
