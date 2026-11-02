---
tag: B54GEJWQAV
kind: definition
name: Linear PDE
msc: [35A99]
defines: 6DZETZ5T9G
uses: [GC5BDZ6QBC, E7JDFDPM1X, 0PJXBR6QA3]
sources:
  - url: https://en.wikipedia.org/wiki/Partial_differential_equation
---

## Definition

Let $\Omega$ be an open set in $\R^n$ and let $m \ge 1$.
A *linear partial differential equation* of [[order|E7JDFDPM1X]] $m$ in $\Omega$ is a [[partial differential equation|GC5BDZ6QBC]] of the following form.
$$\sum_{\abs{\alpha} \le m} a_\alpha(x) \, \partial^\alpha u(x) = f(x), \quad x \in \Omega.$$
Here the sum runs over [[multi-indices|0PJXBR6QA3]] $\alpha$.
The coefficients $a_\alpha$ and the right-hand side $f$ are given functions on $\Omega$, and $a_\alpha$ is not identically zero for some $\alpha$ with $\abs{\alpha} = m$.
The map $P = \sum_{\abs{\alpha} \le m} a_\alpha \partial^\alpha$ is the associated *linear differential operator*.
The equation is *homogeneous* if $f = 0$ and *inhomogeneous* otherwise.
It has *constant coefficients* if every $a_\alpha$ is constant.

## Remarks

Example: $\partial_x^2 u + x^2 \partial_y^2 u + e^y u = \sin x$ on $\R^2$ is linear of order $2$, with coefficients $1$, $x^2$ and $e^y$.
Non-example: $\partial_x^2 u + u^3 = 0$ is not linear, because the term $u^3$ is not a coefficient times $u$.
For a homogeneous linear equation the solutions in $C^m(\Omega)$ form a vector space.
For an inhomogeneous equation, any two solutions differ by a solution of the homogeneous equation.
In short notation the equation reads $P u = f$.

## Explanations

### L1 human

A linear PDE is a weighted sum of derivatives of the unknown, with weights that depend only on the point, set equal to a known function.
