---
tag: DV92N2YWZJ
kind: definition
name: Quasilinear PDE
msc: [35A99, 35J62, 35K59]
defines: 7X9N9H3RK6
uses: [GC5BDZ6QBC, E7JDFDPM1X, 0PJXBR6QA3]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_partial_differential_equation
---

## Definition

Let $\Omega$ be an open set in $\R^n$ and let $m \ge 1$.
A [[partial differential equation|GC5BDZ6QBC]] of [[order|E7JDFDPM1X]] $m$ in $\Omega$ is *quasilinear* if it has the following form.
$$\sum_{\abs{\alpha} = m} a_\alpha\left(D^{m-1} u, \dots, D u, u, x\right) \partial^\alpha u + a_0\left(D^{m-1} u, \dots, D u, u, x\right) = 0.$$
Here the functions $a_\alpha$ and $a_0$ are given.
Here $\alpha$ runs over [[multi-indices|0PJXBR6QA3]], and $D^j u$ denotes the collection of all partial derivatives of order $j$.
So the equation is affine in the derivatives of order $m$, and its coefficients depend at most on the derivatives of order less than $m$.

## Remarks

Example: the minimal surface equation $\operatorname{div}\left(\nabla u / \sqrt{1 + \abs{\nabla u}^2}\right) = 0$ in two variables expands to $(1 + u_y^2) u_{xx} - 2 u_x u_y u_{xy} + (1 + u_x^2) u_{yy} = 0$.
The coefficients of $u_{xx}$, $u_{xy}$, $u_{yy}$ depend only on first derivatives, so it is quasilinear of order $2$.
Non-example: the Monge–Ampère equation $u_{xx} u_{yy} - u_{xy}^2 = f(x, y)$ is not quasilinear, because it contains products of second derivatives; it is [[fully nonlinear|2D3N1ZJWBW]].
Every [[semilinear PDE|RCNY89A4NY]] is quasilinear.
For first-order equations, quasilinear means $\sum_{i} a_i(u, x) \partial_i u + a_0(u, x) = 0$.

## Explanations

### L1 human

Quasilinear means linear in the highest derivatives, once the solution and its lower derivatives are frozen.
