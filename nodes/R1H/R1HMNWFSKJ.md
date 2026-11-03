---
tag: R1HMNWFSKJ
kind: definition
name: Newton's method in optimization
msc: [90C30, 49M15, 65K05]
defines: TNQZVR6TFN
uses: [0ABK9V9Y64, 0693Y2METT, 07EXVNF9VP]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%27s_method_in_optimization
---

## Definition

Let $U \subseteq \R^n$ be open and let $f \colon U \to \R$ be twice differentiable, with [[gradient|0ABK9V9Y64]] $\nabla f$ and [[Hessian matrix|0693Y2METT]] $\nabla^2 f$.
*Newton's method* for minimizing $f$ starts from a point $x_0 \in U$ and defines
$$x_{k+1} = x_k - \left(\nabla^2 f(x_k)\right)^{-1} \nabla f(x_k), \qquad k = 0, 1, 2, \dots,$$
as long as $\nabla^2 f(x_k)$ is invertible and $x_{k+1} \in U$.
The vector $p_k = -\left(\nabla^2 f(x_k)\right)^{-1} \nabla f(x_k)$ is the *Newton step* at $x_k$.

## Remarks

The point $x_k + p_k$ is the stationary point of the quadratic model $m_k(p) = f(x_k) + \nabla f(x_k)^T p + \tfrac12 p^T \nabla^2 f(x_k) p$.
So the method is [[Newton's method|07EXVNF9VP]] for the system $\nabla f(x) = 0$.
A damped version sets $x_{k+1} = x_k + \alpha_k p_k$ with a step length $\alpha_k \in (0, 1]$ chosen by a line search.

Example: let $A$ be a symmetric positive definite $n \times n$ matrix, $b \in \R^n$, and $f(x) = \tfrac12 x^T A x - b^T x$.
Then $\nabla f(x) = Ax - b$ and $\nabla^2 f(x) = A$, so $x_1 = x_0 - A^{-1}(A x_0 - b) = A^{-1} b$ for every $x_0$.
This is the unique minimizer, reached in one step.

Non-example: for $f(x) = x^3$ on $\R$ and $x_0 = 0$, one has $f''(0) = 0$.
The Hessian is not invertible, so the Newton step is not defined.

If $\nabla^2 f$ is Lipschitz near a minimizer $x^*$ and $\nabla^2 f(x^*)$ is positive definite, the iterates converge quadratically to $x^*$ from every $x_0$ close enough to $x^*$.
