---
tag: JP9DCG1ZW4
kind: statement
role: theorem
name: Second-order sufficient optimality conditions
msc: [90C46, 90C30]
uses: [HDWEPH4YG4, 0693Y2METT, 0ABK9V9Y64]
about: [HDWEPH4YG4]
sources:
  - url: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
---

## Statement

Let $U \subseteq \R^n$ be open and let $f, g_1, \dots, g_m, h_1, \dots, h_p \colon U \to \R$ be twice continuously differentiable.
Let $S = \set{x \in U : g_i(x) \le 0 \text{ for all } i,\ h_j(x) = 0 \text{ for all } j}$ and $L(x, \mu, \lambda) = f(x) + \sum_i \mu_i g_i(x) + \sum_j \lambda_j h_j(x)$.
Let $x^* \in S$, and let $\mu \in \R^m$, $\lambda \in \R^p$ satisfy the [[Karush–Kuhn–Tucker conditions|HDWEPH4YG4]] at $x^*$.
Let $C$ be the set of $d \in \R^n$ such that:

1. $\nabla h_j(x^*) \cdot d = 0$ for all $j$.
2. $\nabla g_i(x^*) \cdot d = 0$ for every $i$ with $g_i(x^*) = 0$ and $\mu_i > 0$.
3. $\nabla g_i(x^*) \cdot d \le 0$ for every $i$ with $g_i(x^*) = 0$ and $\mu_i = 0$.

If $d^{T} \nabla_x^2 L(x^*, \mu, \lambda)\, d > 0$ for every nonzero $d \in C$, then $x^*$ is a strict local minimizer of $f$ on $S$.

## Remarks

Here $\nabla_x^2 L$ is the [[Hessian matrix|0693Y2METT]] of $L$ in $x$, and $C$ is the critical cone.
The proof is by contradiction: a sequence of feasible points $x_k \to x^*$ with $f(x_k) \le f(x^*)$ has limiting directions in $C$, and a second-order Taylor expansion of $L$ along them contradicts the positivity.
No constraint qualification is needed, since multipliers are assumed to exist.
Without constraints, the theorem says that a critical point with a positive definite Hessian is a strict local minimizer.

Example: minimize $f(x) = x_1^2 - x_2^2$ subject to $h(x) = x_2 = 0$.
At $x^* = 0$, $\lambda = 0$ satisfies the KKT conditions, and $C = \set{d : d_2 = 0}$.
The Hessian of $L$ is $\mathrm{diag}(2, -2)$, and $d^{T} \mathrm{diag}(2, -2) d = 2 d_1^2 > 0$ for nonzero $d \in C$.
So $0$ is a strict local minimizer on the line $x_2 = 0$, although the Hessian is not positive definite on all of $\R^2$.

## Explanations

### L1 human

The first-order conditions only say that a point is flat in all allowed directions; it could still be a maximum or a saddle.
The second-order test checks that the function curves upward in every allowed direction that the first-order test cannot decide.
If it does, the point is a genuine local minimum.

### L2 human

This is the constrained version of the second derivative test.
The key point is that curvature is tested only on the critical cone, not on all of $\R^n$.
The curvature is that of the Lagrangian, which includes the curvature of the constraints.
The matching necessary condition says that, under LICQ, a local minimizer has $d^{T} \nabla_x^2 L\, d \ge 0$ on the critical cone.
These conditions also guarantee fast local convergence of Newton-type methods such as sequential quadratic programming.
