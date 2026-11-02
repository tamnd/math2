---
tag: E2ZFQ76N7F
kind: statement
role: proposition
name: Rosenbrock methods
msc: [65L04, 65L06]
uses: [0FXDW992DS, 047NDTEPCV, 7DBPJKYC6C, RR5FCG92PN]
about: [RR5FCG92PN]
sources:
  - url: https://en.wikipedia.org/wiki/Rosenbrock_methods
---

## Statement

Let $f \colon \R^d \to \R^d$ be continuously differentiable, and consider the autonomous [[initial value problem|0FXDW992DS]] $y' = f(y)$, $y(t_0) = y_0$.
Let $J = f'(y_n)$ be the [[Jacobian matrix|047NDTEPCV]] of $f$ at the current value $y_n$.
An $s$-stage Rosenbrock method with real coefficients $\alpha_{ij}$, $\gamma_{ij}$, $b_i$ and $\gamma_{ii} = \gamma > 0$ computes, for $i = 1, \ldots, s$,
$$(I - h \gamma J)\, k_i = h f\Big(y_n + \sum_{j<i} \alpha_{ij} k_j\Big) + h J \sum_{j<i} \gamma_{ij} k_j,$$
and sets $y_{n+1} = y_n + \sum_{i=1}^s b_i k_i$.

1. Each step requires only the solution of $s$ linear systems, all with the same matrix $I - h\gamma J$, and no nonlinear equation.
2. Applied to the test equation $y' = \lambda y$ with $\lambda \in \C$, the method gives $y_{n+1} = R(h\lambda)\, y_n$, where $R$ is a rational function whose denominator is $(1 - \gamma z)^s$.
3. For $s = 1$, $\gamma = 1$ and $b_1 = 1$ (the linearly implicit Euler method), $R(z) = 1/(1 - z)$; the method has order $1$, and it is A-stable and L-stable.

## Remarks

Clause 1 holds because the right-hand side of the $i$-th equation involves only $k_1, \ldots, k_{i-1}$, so the stages are computed one after the other.
For clause 2, with $f(y) = \lambda y$ and $J = \lambda$, each $k_i$ is $y_n$ times a rational function of $z = h\lambda$ with denominator $(1 - \gamma z)^i$.
For clause 3, $(1 - h\lambda) k_1 = h\lambda y_n$ gives $y_{n+1} = y_n / (1 - h\lambda)$, the same as the [[backward Euler method|M7XKVNATFA]]: $\abs{R(z)} \le 1$ when $\operatorname{Re} z \le 0$, and $R(z) \to 0$ as $\abs{z} \to \infty$.
The order conditions of Rosenbrock methods use the exact Jacobian; methods that allow an approximate $J$ are called W-methods.

## Explanations

### L1 human

[[Stiff equations|RR5FCG92PN]] need implicit methods, but implicit methods need the solution of a nonlinear equation at every step.
A Rosenbrock method replaces this nonlinear equation by a few linear ones, built from the derivative of $f$.
In effect, it does one Newton step per stage and builds the error control into the coefficients.
The simplest one has the same behaviour as backward Euler on linear problems.

### L2 human

Rosenbrock methods are linearly implicit [[Runge–Kutta methods|7DBPJKYC6C]]: the coefficients are chosen so that the order conditions hold when $J$ is the exact Jacobian.
One LU factorisation of $I - h\gamma J$ per step serves all stages, which is why all diagonal coefficients are equal.
They are popular for moderately stiff problems of medium size, for example in chemical kinetics, and embedded pairs give error estimates for step size control.
