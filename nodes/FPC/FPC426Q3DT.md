---
tag: FPC426Q3DT
kind: definition
name: Quasi-Newton method
msc: [90C53, 65K05, 90C30]
defines: JEEEH7757R
uses: [0ABK9V9Y64, 0VR671PHE5, TNQZVR6TFN]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-Newton_method
---

## Definition

Let $f \colon \R^n \to \R$ be continuously differentiable, with [[gradient|0ABK9V9Y64]] $\nabla f$.
A *quasi-Newton method* for minimizing $f$ starts from $x_0 \in \R^n$ and an invertible [[symmetric|0VR671PHE5]] $n \times n$ matrix $B_0$, and for $k \ge 0$:

1. computes the direction $p_k = -B_k^{-1} \nabla f(x_k)$;
2. sets $x_{k+1} = x_k + \alpha_k p_k$ for a step length $\alpha_k > 0$;
3. puts $s_k = x_{k+1} - x_k$ and $y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$;
4. chooses a symmetric matrix $B_{k+1}$ that satisfies the *secant equation* $B_{k+1} s_k = y_k$ and differs from $B_k$ by a matrix of rank $1$ or $2$.

The rule that gives $B_{k+1}$ from $B_k$, $s_k$ and $y_k$ is the *update formula* of the method.

## Remarks

The secant equation holds for the true Hessian of a quadratic function: if $f(x) = \tfrac12 x^T A x - b^T x$, then $y_k = A s_k$.
If $f$ is twice continuously differentiable, then $y_k = \left(\int_0^1 \nabla^2 f(x_k + t s_k)\, dt\right) s_k$, so $B_{k+1}$ mimics an average Hessian along the step.

Example: the symmetric rank-one (SR1) update
$$B_{k+1} = B_k + \frac{(y_k - B_k s_k)(y_k - B_k s_k)^T}{(y_k - B_k s_k)^T s_k},$$
defined when the denominator is nonzero.
Check: $B_{k+1} s_k = B_k s_k + (y_k - B_k s_k) = y_k$, and the correction is symmetric of rank $1$.
The BFGS and DFP updates are rank-two updates that also satisfy clause 4.

Non-example: [[gradient descent|12317R8RTJ]] with $B_k = I$ for all $k$ fails clause 4, since in general $s_k \ne y_k$.

Many methods keep $H_k = B_k^{-1}$ instead of $B_k$ and update it directly, so that $p_k = -H_k \nabla f(x_k)$ costs only a matrix-vector product.
