---
tag: X3P4TQZ9X2
kind: definition
name: Semilinear PDE
msc: [35A99, 35J61, 35K58]
defines: RCNY89A4NY
uses: [GC5BDZ6QBC, E7JDFDPM1X, 0PJXBR6QA3]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_partial_differential_equation
---

## Definition

Let $\Omega$ be an open set in $\R^n$ and let $m \ge 1$.
A [[partial differential equation|GC5BDZ6QBC]] of [[order|E7JDFDPM1X]] $m$ in $\Omega$ is *semilinear* if it has the following form.
$$\sum_{\abs{\alpha} = m} a_\alpha(x) \, \partial^\alpha u + a_0\left(D^{m-1} u, \dots, D u, u, x\right) = 0.$$
Here the coefficients $a_\alpha$ of the highest-order derivatives depend on $x$ only, and $a_0$ is a given function, which may be nonlinear.
Here $\alpha$ runs over [[multi-indices|0PJXBR6QA3]], and $D^j u$ denotes the collection of all partial derivatives of order $j$.

## Remarks

Example: $\Delta u = u^3$ in $\R^3$, with $\Delta = \partial_1^2 + \partial_2^2 + \partial_3^2$, is semilinear of order $2$; its highest-order part $\Delta u$ has constant coefficients, and $a_0(u) = -u^3$.
Non-example: $\partial_t u + u \, \partial_x u = 0$ is not semilinear, because the coefficient $u$ of the highest-order derivative $\partial_x u$ depends on the unknown; it is [[quasilinear|7X9N9H3RK6]].
Every [[linear PDE|6DZETZ5T9G]] is semilinear, with $a_0$ affine in the lower-order derivatives.

## Explanations

### L1 human

Semilinear means linear in the highest derivatives, with coefficients that depend only on the position, and arbitrary in the rest.
