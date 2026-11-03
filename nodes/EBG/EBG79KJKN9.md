---
tag: EBG79KJKN9
kind: definition
name: Sequential quadratic programming
msc: [90C55, 90C30, 65K05]
defines: CPX8Q2GFGD
uses: [0ABK9V9Y64, 0693Y2METT, 0VKKP8X6Q6, 0VR671PHE5]
sources:
  - url: https://en.wikipedia.org/wiki/Sequential_quadratic_programming
---

## Definition

Let $f, g_1, \dots, g_m, h_1, \dots, h_l \colon \R^n \to \R$ be twice continuously differentiable.
Consider the problem of minimizing $f(x)$ subject to $g_i(x) \le 0$ for all $i$ and $h_j(x) = 0$ for all $j$.
Its Lagrangian is $\mathcal{L}(x, \lambda, \nu) = f(x) + \sum_i \lambda_i g_i(x) + \sum_j \nu_j h_j(x)$.
A *sequential quadratic programming method* starts from $(x_0, \lambda_0, \nu_0)$, and for $k \ge 0$:

1. chooses a [[symmetric|0VR671PHE5]] matrix $B_k$, equal to or approximating the [[Hessian|0693Y2METT]] $\nabla_{xx}^2 \mathcal{L}(x_k, \lambda_k, \nu_k)$;
2. computes a solution $p_k$, with multipliers $(\lambda_{k+1}, \nu_{k+1})$, of the quadratic program: minimize $\nabla f(x_k)^T p + \tfrac12 p^T B_k p$ subject to $g_i(x_k) + \nabla g_i(x_k)^T p \le 0$ for all $i$ and $h_j(x_k) + \nabla h_j(x_k)^T p = 0$ for all $j$;
3. sets $x_{k+1} = x_k + p_k$.

## Remarks

Practical versions damp the step in clause 3 by a line search on a merit function, or restrict it by a trust region.

Example: with no constraints, clause 2 asks to minimize $\nabla f(x_k)^T p + \frac12 p^T B_k p$.
If $B_k = \nabla^2 f(x_k)$ is positive definite, the solution is $p_k = -\nabla^2 f(x_k)^{-1} \nabla f(x_k)$.
So SQP reduces to [[Newton's method in optimization|TNQZVR6TFN]].

With only equality constraints and $B_k$ the exact Hessian of the Lagrangian, the step solves the Newton equations for the system $\nabla_x \mathcal{L} = 0$, $h = 0$.

Non-example: keeping the constraints $g_i(x_k + p) \le 0$ and $h_j(x_k + p) = 0$ unlinearized fails clause 2.
The subproblem is then a general nonlinear program, not a quadratic program.
