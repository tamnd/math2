---
tag: MTQ3SGX56W
kind: definition
name: Fully nonlinear PDE
msc: [35A99, 35J60]
defines: 2D3N1ZJWBW
uses: [GC5BDZ6QBC, 7X9N9H3RK6, E7JDFDPM1X]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_partial_differential_equation
---

## Definition

A [[partial differential equation|GC5BDZ6QBC]] $F\left(D^m u, \dots, D u, u, x\right) = 0$ of [[order|E7JDFDPM1X]] $m$ is *fully nonlinear* if it is not [[quasilinear|7X9N9H3RK6]].
That is, $F$ cannot be written as an affine function of the derivatives $D^m u$ of order $m$ whose coefficients depend only on $D^{m-1} u, \dots, D u, u, x$.

## Remarks

Example: the Monge–Ampère equation $\det D^2 u = f(x)$ in $\R^n$ with $n \ge 2$ is fully nonlinear of order $2$.
For $n = 2$ it reads $u_{xx} u_{yy} - u_{xy}^2 = f$, which contains the product $u_{xx} u_{yy}$ of two second derivatives.
Non-example: the minimal surface equation is not fully nonlinear, because it is affine in the second derivatives with coefficients depending on $\nabla u$ only.
For first-order equations, the eikonal equation $\abs{\nabla u}^2 = 1$ is fully nonlinear.

## Explanations

### L1 human

A PDE is fully nonlinear when its highest derivatives enter in a genuinely nonlinear way.
