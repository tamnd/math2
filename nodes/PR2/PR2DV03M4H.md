---
tag: PR2DV03M4H
kind: definition
name: Separation of variables
msc: [34A05, 35C05]
defines: 47NFRVB564
uses: [0V4E623THY, 0BW9N5CDSB]
sources:
  - url: https://en.wikipedia.org/wiki/Separation_of_variables
---

## Definition

*Separation of variables* is the following method, in two standard settings.

1. Ordinary equations. Let $g$ be continuous on an open interval $I$ and $h$ continuous on an open interval $J$, and consider the [[separable equation|0V4E623THY]] $y' = g(x)\, h(y)$. Let $H$ be an [[antiderivative|0BW9N5CDSB]] of $1/h$ and $G$ an antiderivative of $g$. On an interval where $h(y(x)) \ne 0$, $y$ is a solution if and only if $H(y(x)) = G(x) + C$ for a constant $C$. The constant functions $y = c$ with $h(c) = 0$ are further solutions.
2. Linear partial equations. For a linear homogeneous equation in $u(x, t)$, one looks for solutions of product form $u(x, t) = X(x)\, T(t)$. Sometimes the equation can then be rewritten with one side depending only on $x$ and the other only on $t$. Then both sides equal a common constant $\lambda$, which gives an ordinary differential equation for $X$ and one for $T$.

## Remarks

Example for 1: $y' = x y$ gives $\ln\abs{y} = x^2/2 + C$, so $y = A e^{x^2/2}$ with $A \ne 0$, and $y = 0$ comes from the zero of $h(y) = y$.
Check: $(A e^{x^2/2})' = x \cdot A e^{x^2/2}$.
Example for 2: for the heat equation $u_t = k u_{xx}$ with $k > 0$, the product $X T$ gives $X(x) T'(t) = k X''(x) T(t)$, so $T'/(kT) = X''/X = \lambda$.
With $\lambda = -1$ one finds $X = \sin x$ and $T = e^{-kt}$, and $u = e^{-kt} \sin x$ indeed satisfies $u_t = -k e^{-kt}\sin x = k u_{xx}$.
Non-example: $y' = x + y$ is not separable, since $x + y = g(x) h(y)$ for all $x, y$ is impossible.
Indeed, $x = 0$ gives $y = g(0) h(y)$ for all $y$, so $h(0) = 0$; then $y = 0$ gives $x = g(x) h(0) = 0$ for all $x$, which is false.
In the partial differential setting, superposition of product solutions and boundary conditions lead to eigenvalue problems and Fourier series.
