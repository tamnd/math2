---
tag: NAD3RQNJ7V
kind: definition
name: Trajectory optimization
msc: [49M37, 49M05, 49J15]
defines: 58895A7T4H
uses: [ZPDTVZQN5K, T3V6ZNAMDN, 7RPV2T29CF]
sources:
  - url: https://en.wikipedia.org/wiki/Trajectory_optimization
---

## Definition

Let $U \subseteq \R^m$ be nonempty, and let $f \colon \R^n \times U \times \R \to \R^n$, $L \colon \R^n \times U \times \R \to \R$, $\phi \colon \R \times \R^n \times \R \times \R^n \to \R$ be continuous.
Let $c \colon \R^n \times U \times \R \to \R^q$ give path constraints and $b \colon \R \times \R^n \times \R \times \R^n \to \R^r$ give boundary conditions.
A *trajectory optimization problem* asks for times $t_0 < t_f$, a measurable control $u \colon [t_0, t_f] \to U$ and an absolutely continuous state $x \colon [t_0, t_f] \to \R^n$ that minimise
$$\phi(t_0, x(t_0), t_f, x(t_f)) + \int_{t_0}^{t_f} L(x(t), u(t), t) \, dt$$
subject to:

1. the [[control system|ZPDTVZQN5K]] $x'(t) = f(x(t), u(t), t)$ for almost every $t$;
2. the path constraints $c(x(t), u(t), t) \le 0$ componentwise for almost every $t$;
3. the boundary conditions $b(t_0, x(t_0), t_f, x(t_f)) = 0$.

*Trajectory optimization* is the numerical solution of such problems, which yields an open-loop control and its trajectory.

## Remarks

The problem is an [[optimal control|T3V6ZNAMDN]] problem in Bolza form with constraints; the word stresses the computation of one optimal trajectory.
Indirect methods solve the conditions of [[Pontryagin's maximum principle|7RPV2T29CF]]; direct methods discretise $x$ and $u$ and solve a finite-dimensional nonlinear program.

Example: $n = 2$, $x = (x_1, x_2)$, $f = (x_2, u)$, $U = \R$, $L = u^2$, $\phi = 0$, no path constraints, $t_0 = 0$, $t_f = 1$, and boundary conditions $x(0) = (0, 0)$, $x(1) = (1, 0)$.
The control $u(t) = 6 - 12t$ gives $x_2(t) = 6t - 6t^2$ and $x_1(t) = 3t^2 - 2t^3$, which meet the boundary conditions, with cost $\int_0^1 (6 - 12t)^2 \, dt = 12$.
The maximum principle forces the optimal $u$ to be affine in $t$, and this is the only affine control that meets the boundary conditions, so it is the solution.

Non-example: finding a feedback law $u = \kappa(x)$ that is good for all initial states is a synthesis problem, not a trajectory optimization problem in this sense.

## Explanations

### L1 human

Trajectory optimization finds one best motion of a system, together with the controls that produce it, from given start and end conditions.
