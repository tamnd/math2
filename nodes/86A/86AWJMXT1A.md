---
tag: 86AWJMXT1A
kind: statement
role: proposition
name: Reduction of an initial value problem to a Volterra equation
msc: [45D05, 34A12, 34A30]
uses: [0FXDW992DS, 0QQRP17Z7S, DND8CBEVXT, 015KK993C5, 0NHGY0N0JB]
about: [DND8CBEVXT, 0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Statement

Let $a < b$, let $n \ge 1$, let $p_1, \ldots, p_n, F \colon [a, b] \to \R$ be continuous, and let $c_0, \ldots, c_{n-1} \in \R$.
Consider the [[initial value problem|0FXDW992DS]] for the [[linear differential equation of order n|0QQRP17Z7S]]
$$y^{(n)} + p_1(x) y^{(n-1)} + \cdots + p_n(x) y = F(x), \qquad y^{(j)}(a) = c_j \text{ for } 0 \le j \le n - 1.$$
Define, for $x, t \in [a, b]$,
$$K(x, t) = -\sum_{i=1}^{n} p_i(x) \frac{(x - t)^{i-1}}{(i-1)!}, \qquad f(x) = F(x) - \sum_{i=1}^{n} p_i(x) \sum_{j=n-i}^{n-1} c_j \frac{(x - a)^{j - n + i}}{(j - n + i)!}.$$
Then the following hold.

1. If $y \in C^n[a, b]$ solves the initial value problem, then $u = y^{(n)}$ is a continuous solution of the [[Volterra integral equation|DND8CBEVXT]] of the second kind
$$u(x) = f(x) + \int_a^x K(x, t) u(t) \, dt, \quad x \in [a, b].$$
2. If $u \in C[a, b]$ solves this Volterra equation, then
$$y(x) = \sum_{j=0}^{n-1} c_j \frac{(x - a)^j}{j!} + \int_a^x \frac{(x - t)^{n-1}}{(n-1)!} u(t) \, dt$$
is in $C^n[a, b]$, satisfies $y^{(n)} = u$, and solves the initial value problem.

## Remarks

Proof idea: for $y \in C^n[a, b]$ with the given initial values, Taylor's formula with integral remainder, a repeated use of the [[fundamental theorem of calculus|0NHGY0N0JB]], gives for $0 \le k \le n - 1$
$$y^{(k)}(x) = \sum_{j=k}^{n-1} c_j \frac{(x - a)^{j-k}}{(j-k)!} + \int_a^x \frac{(x - t)^{n-k-1}}{(n-k-1)!} y^{(n)}(t) \, dt.$$
Substituting these for $y^{(n-i)}$, $1 \le i \le n$, in the differential equation gives the Volterra equation.
Conversely, differentiating the formula for $y$ gives $y^{(n)} = u$ and the initial values, and the Volterra equation turns back into the differential equation.

Example: for $y'' + y = 0$, $y(0) = 0$, $y'(0) = 1$, one has $p_1 = 0$, $p_2 = 1$, $K(x, t) = -(x - t)$ and $f(x) = -x$.
The equation $u(x) = -x - \int_0^x (x - t) u(t) \, dt$ has the solution $u = -\sin x$, and indeed $y = \sin x$ has $y'' = -\sin x$.

The kernel $K$ is continuous, so the Volterra equation has a unique continuous solution; this gives the existence and uniqueness theorem for linear initial value problems.
For the first-order nonlinear problem $y' = g(x, y)$, $y(a) = c_0$, the analogous reduction is the [[integral equation form of an initial value problem|015KK993C5]].

## Explanations

### L1 human

A differential equation with initial values can be traded for an integral equation.
The unknown becomes the highest derivative $y^{(n)}$, and the lower derivatives are recovered from it by integration.
The initial values are built into the equation, so no side conditions remain.

### L2 human

This reduction is the bridge between linear ordinary differential equations and the theory of Volterra equations.
Volterra equations of the second kind with continuous kernels are uniquely solvable for every right side.
So the reduction proves that a linear initial value problem with continuous coefficients has exactly one solution on the whole interval $[a, b]$.
For a first-order equation, taking $y$ itself as the unknown gives the integral form used in Picard iteration.
