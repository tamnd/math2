---
tag: DT45YNKWSQ
kind: definition
name: Direct collocation
msc: [49M37, 49M25, 65L60]
defines: T58W34D60G
uses: [58895A7T4H, SS1YMS2NPC, 7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Collocation_method
---

## Definition

Consider a [[trajectory optimization|58895A7T4H]] problem on a fixed interval $[t_0, t_f]$: minimise $\phi(x(t_f)) + \int_{t_0}^{t_f} L(x, u, t) \, dt$ subject to $x' = f(x, u, t)$, path constraints $c(x, u, t) \le 0$ and boundary conditions $b(x(t_0), x(t_f)) = 0$.
Choose a mesh $t_0 = \tau_0 < \tau_1 < \cdots < \tau_N = t_f$ and an integer $s \ge 1$.
On each interval $[\tau_k, \tau_{k+1}]$ choose $s$ collocation points $\tau_k \le \tau_{k,1} < \cdots < \tau_{k,s} \le \tau_{k+1}$.
The *direct collocation* method replaces the problem by the following finite nonlinear program.

1. The unknowns are the states $x_k$ at the mesh points and the controls at the collocation points. On each interval the state is a polynomial $p_k$ of degree at most $s$ with $p_k(\tau_k) = x_k$.
2. The dynamics are imposed only at the collocation points: $p_k'(\tau_{k,j}) = f(p_k(\tau_{k,j}), u(\tau_{k,j}), \tau_{k,j})$ for all $k$ and $j$, and the pieces join continuously, $p_k(\tau_{k+1}) = x_{k+1}$.
3. The path constraints hold at the collocation points and the boundary conditions at $x_0$ and $x_N$. The integral of $L$ becomes a quadrature sum.

The solution of this program is an approximate optimal trajectory.

## Remarks

Each choice of collocation points corresponds to an implicit [[Runge–Kutta method|7DBPJKYC6C]]; the state on each interval is a [[polynomial interpolant|SS1YMS2NPC]] of its values.
With $s = 2$ and the endpoints $\tau_k, \tau_{k+1}$ as collocation points, clause 2 becomes the trapezoidal rule $x_{k+1} - x_k = \frac{h_k}{2} \left( f(x_k, u_k, \tau_k) + f(x_{k+1}, u_{k+1}, \tau_{k+1}) \right)$ with $h_k = \tau_{k+1} - \tau_k$.
Hermite–Simpson collocation uses the endpoints and the midpoint with a cubic state.
The nonlinear program is large but sparse, and it is usually solved by sequential quadratic programming or by interior-point methods.

Example: minimise $\int_0^1 \frac{1}{2} u^2 \, dt$ with $x' = u$, $x(0) = 0$, $x(1) = 1$, using trapezoidal collocation on a uniform mesh of step $h = 1/N$.
The program is: minimise $\sum_{k=0}^{N-1} \frac{h}{4} (u_k^2 + u_{k+1}^2)$ subject to $x_{k+1} - x_k = \frac{h}{2} (u_k + u_{k+1})$, $x_0 = 0$, $x_N = 1$.
The choice $u_k = 1$, $x_k = k h$ satisfies all constraints.
It also satisfies the optimality conditions, with all multipliers of the dynamics constraints equal to one constant ($1$ or $-1$, by sign convention).
It reproduces the exact solution $u = 1$, $x(t) = t$ at the grid points.

Non-example: direct single shooting integrates the dynamics forward from a guessed control and optimises only over the control values.
It is not collocation, because the states are not unknowns of the program.

## Explanations

### L1 human

The trajectory is replaced by grid values, the equations of motion are checked only at a few points per step, and a large finite optimisation problem is solved.
