---
tag: 7RPV2T29CF
kind: statement
role: theorem
name: Pontryagin's maximum principle
msc: [49K15, 93C15]
uses: [ZPDTVZQN5K, ZT6F4C2YHK]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin's_maximum_principle
same_as:
  wikidata: Q3491629
  wikipedia: Pontryagin's maximum principle
---

## Statement

Let $U \subseteq \R^m$ be a nonempty set, and let $f \colon \R^n \times U \to \R^n$ and $L \colon \R^n \times U \to \R$ be continuous, with partial derivatives $\partial f / \partial x$ and $\partial L / \partial x$ that are continuous on $\R^n \times U$.
Let $T > 0$ and $x_0, x_1 \in \R^n$ be fixed.
Consider the [[optimal control|T3V6ZNAMDN]] problem: minimize
$$J(u) = \int_0^T L(x(t), u(t)) \, dt$$
over the measurable bounded controls $u \colon [0, T] \to U$ whose trajectory of the [[control system|ZPDTVZQN5K]] $x' = f(x, u)$ with $x(0) = x_0$ satisfies $x(T) = x_1$.
For $\lambda_0 \in \R$ and $p \in \R^n$, let $H(x, u, p, \lambda_0) = p \cdot f(x, u) - \lambda_0 L(x, u)$.
Let $u^*$ be an optimal control with trajectory $x^*$.
Then there are a number $\lambda_0 \in \set{0, 1}$ and an [[absolutely continuous|ZT6F4C2YHK]] function $p \colon [0, T] \to \R^n$, with $(\lambda_0, p(t)) \ne (0, 0)$ for all $t$, such that:

1. $p'(t) = -\dfrac{\partial H}{\partial x}(x^*(t), u^*(t), p(t), \lambda_0)$ for almost every $t \in [0, T]$;
2. $H(x^*(t), u^*(t), p(t), \lambda_0) = \max_{v \in U} H(x^*(t), v, p(t), \lambda_0)$ for almost every $t \in [0, T]$;
3. the function $t \mapsto H(x^*(t), u^*(t), p(t), \lambda_0)$ is equal almost everywhere to a constant.

## Remarks

The proof compares the optimal control with needle variations, which replace $u^*$ by a constant value $v \in U$ on a short interval.
The first-order effects of these variations on the endpoint and the cost form a convex cone.
Optimality means that this cone does not meet a certain direction.
A separating hyperplane gives $(\lambda_0, p(T))$, and $p$ is then transported backward by the adjoint equation of condition 1.
Example: minimize $\int_0^1 \frac{1}{2} u^2 \, dt$ for $x' = u$, $x(0) = 0$, $x(1) = 1$, $U = \R$.
Here $H = p u - \lambda_0 u^2 / 2$ and $p' = 0$, so $p$ is constant; if $\lambda_0 = 0$, condition 2 forces $p = 0$, which is excluded, so $\lambda_0 = 1$ and $u = p$ is constant, which gives $u \equiv 1$ and $x(t) = t$.
The theorem gives necessary conditions only: an extremal that satisfies them need not be optimal.
The case $\lambda_0 = 0$, called abnormal, can occur, and then the conditions do not involve the cost at all.

## Explanations

### L1 human

To steer a system in the cheapest way, one cannot test every possible control.
The maximum principle says that an optimal control must, at each moment, maximize a single function $H$ over the allowed control values.
The function $H$ combines the dynamics and the cost with a vector $p(t)$ of shadow prices that solves its own differential equation.
This turns an optimization over functions into a pointwise maximization plus a boundary value problem.

### L2 human

The maximum principle extends the Euler–Lagrange equations of the calculus of variations to controls with values in a constraint set $U$, such as $[-1, 1]$.
When $H$ is linear in $u$ and $U$ is a box, condition 2 forces $u$ to take extreme values, which gives [[bang–bang controls|GK1Z3Q1WRZ]] except on singular arcs.
The state equation $x' = \partial H / \partial p$ and the adjoint equation form a Hamiltonian system with boundary conditions at both ends, usually solved by shooting methods.
Variants with free final time add the condition that the constant in condition 3 is zero.
Variants with a free endpoint and no terminal cost add the transversality condition $p(T) = 0$.
