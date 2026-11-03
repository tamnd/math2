---
tag: 79JGXK5DZG
kind: definition
name: BFGS method
msc: [90C53, 65K05]
defines: 2C7B0CXBMW
uses: [JEEEH7757R, 0KX66CZMBB, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm
---

## Definition

Let $f \colon \R^n \to \R$ be continuously differentiable, with [[gradient|0ABK9V9Y64]] $\nabla f$.
The *BFGS method* is the [[quasi-Newton method|JEEEH7757R]] that starts from $x_0 \in \R^n$ and a symmetric [[positive definite matrix|0KX66CZMBB]] $B_0$, and for $k \ge 0$:

1. sets $p_k = -B_k^{-1} \nabla f(x_k)$ and $x_{k+1} = x_k + \alpha_k p_k$, with a step length $\alpha_k > 0$ such that $y_k^T s_k > 0$, where $s_k = x_{k+1} - x_k$ and $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$;
2. updates
$$B_{k+1} = B_k - \frac{B_k s_k s_k^T B_k}{s_k^T B_k s_k} + \frac{y_k y_k^T}{y_k^T s_k}.$$

## Remarks

Check of the secant equation: $B_{k+1} s_k = B_k s_k - B_k s_k \frac{s_k^T B_k s_k}{s_k^T B_k s_k} + y_k \frac{y_k^T s_k}{y_k^T s_k} = y_k$.

Equivalent form: with $H_k = B_k^{-1}$ and $\rho_k = 1 / (y_k^T s_k)$, the inverse is updated by
$$H_{k+1} = (I - \rho_k s_k y_k^T) H_k (I - \rho_k y_k s_k^T) + \rho_k s_k s_k^T.$$
This form gives $p_k = -H_k \nabla f(x_k)$ in $O(n^2)$ operations.

Example: $n = 1$, $f(x) = x^2$, $B_0 = 1$, $x_0 = 1$, $\alpha_0 = 1/2$.
Then $p_0 = -2$, $x_1 = 0$, $s_0 = -1$, $y_0 = 0 - 2 = -2$ and $y_0 s_0 = 2 > 0$.
The update gives $B_1 = 1 - 1 + 4/2 = 2 = f''$, the exact curvature.

Non-example: if $y_k^T s_k \le 0$, clause 1 fails; the last term of the update is undefined when $y_k^T s_k = 0$, and when $y_k^T s_k < 0$ the matrix $B_{k+1}$ is not positive definite, because $s_k^T B_{k+1} s_k = y_k^T s_k < 0$.
A step length that satisfies the Wolfe conditions always gives $y_k^T s_k > 0$.
