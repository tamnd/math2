---
tag: H0MZB0DPP2
kind: statement
role: proposition
name: Exponential integrator
msc: [65L05, 65F60, 65L04]
uses: [0FXDW992DS, 020M04FN1H, RR5FCG92PN]
about: [020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_integrator
---

## Statement

Let $A$ be a real $d \times d$ matrix, let $N \colon \R^d \to \R^d$ be continuous, and consider the [[initial value problem|0FXDW992DS]] $y' = A y + N(y)$, $y(t_0) = y_0$.
Put $\varphi_1(z) = (e^z - 1)/z$ for $z \ne 0$ and $\varphi_1(0) = 1$, so that $\varphi_1(hA) = \sum_{k \ge 0} \frac{(hA)^k}{(k+1)!}$.

1. The exact solution satisfies the variation-of-constants formula
$$y(t_0 + h) = e^{hA} y_0 + \int_0^h e^{(h - s)A} N(y(t_0 + s))\, ds,$$
where $e^{hA}$ is the [[matrix exponential|020M04FN1H]].
2. The exponential Euler method is the step
$$y_{n+1} = e^{hA} y_n + h\, \varphi_1(hA)\, N(y_n).$$
If $N$ is constant, it gives the exact solution at every step, for every $h > 0$.

## Remarks

Clause 1 follows by differentiating $e^{-tA} y(t)$.
For clause 2, if $N \equiv b$, the integral in clause 1 equals $\int_0^h e^{(h-s)A} b\, ds = h \varphi_1(hA) b$, which is the method.
In general, the exponential Euler method replaces $N(y(t_0 + s))$ by $N(y_n)$ in the integral; it has order $1$ when $N$ is Lipschitz and the solution is smooth.
Example: for the scalar equation $y' = -100 y + 1$ the method reproduces $y(t) = 1/100 + (y_0 - 1/100) e^{-100 t}$ exactly, whatever the step size.
Higher-order exponential Runge–Kutta and Rosenbrock-type methods use the functions $\varphi_k(z) = \sum_{j \ge 0} z^j / (j + k)!$.

## Explanations

### L1 human

Many equations split into a simple linear part, which may be very fast, and a slower remainder.
An exponential integrator solves the linear part exactly with a matrix exponential and approximates only the remainder.
So the fast part does not force tiny time steps.
When the remainder is constant, the method is exact.

### L2 human

Exponential integrators are a tool for [[stiff equations|RR5FCG92PN]] where the stiffness sits in a known linear operator, such as the discretised Laplacian of a semilinear parabolic equation.
They are explicit in $N$ and do not need the solution of nonlinear equations.
They need products of $\varphi_k(hA)$ with vectors, computed with Krylov methods, Padé approximants or contour integrals.
Their error analysis for parabolic problems uses that the bounds do not depend on the norm of $A$.
