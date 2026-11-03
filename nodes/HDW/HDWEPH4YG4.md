---
tag: HDWEPH4YG4
kind: statement
role: theorem
name: Karush–Kuhn–Tucker conditions
msc: [90C46, 90C30]
uses: [2WGB8R9SAD, 0ABK9V9Y64, 0VW90BBSJ4, 07Q7CNM5WF]
about: [2WGB8R9SAD]
sources:
  - url: https://en.wikipedia.org/wiki/Karush%E2%80%93Kuhn%E2%80%93Tucker_conditions
same_as:
  wikidata: Q2075125
  wikipedia: Karush–Kuhn–Tucker conditions
---

## Statement

Let $U \subseteq \R^n$ be open and let $f, g_1, \dots, g_m, h_1, \dots, h_p \colon U \to \R$ be [[continuously differentiable|0VW90BBSJ4]].
Let $S = \set{x \in U : g_i(x) \le 0 \text{ for all } i,\ h_j(x) = 0 \text{ for all } j}$.
For $x^* \in S$, the *KKT conditions* ask for $\mu \in \R^m$ and $\lambda \in \R^p$ such that:

1. $\nabla f(x^*) + \sum_{i=1}^m \mu_i \nabla g_i(x^*) + \sum_{j=1}^p \lambda_j \nabla h_j(x^*) = 0$.
2. $\mu_i \ge 0$ for all $i$.
3. $\mu_i g_i(x^*) = 0$ for all $i$.

Necessity: if $x^*$ is a local minimizer of $f$ on $S$ and a [[constraint qualification|2WGB8R9SAD]] holds at $x^*$, then such $\mu$ and $\lambda$ exist.
Sufficiency: assume that $U$ is convex, that $f$ and all $g_i$ are [[convex|07Q7CNM5WF]], and that all $h_j$ are affine.
If the KKT conditions hold at $x^* \in S$, then $x^*$ minimizes $f$ on $S$.

## Remarks

For necessity under the linear independence constraint qualification, one shows that no direction $d$ with $\nabla f(x^*) \cdot d < 0$ is tangent to $S$, and then applies Farkas' lemma to the linearized constraints.
For sufficiency, convexity gives $f(x) \ge L(x, \mu, \lambda) \ge L(x^*, \mu, \lambda) = f(x^*)$ for every $x \in S$, where $L$ is the Lagrangian.
Here $\nabla$ is the [[gradient|0ABK9V9Y64]], and condition 3 is complementary slackness: a multiplier can be positive only for an active constraint.
With no inequality constraints, the theorem reduces to the rule of [[Lagrange multipliers|0VKKP8X6Q6]].

Example: minimize $f(x) = x_1^2 + x_2^2$ subject to $g(x) = 1 - x_1 - x_2 \le 0$.
At $x^* = (1/2, 1/2)$, $\nabla f = (1, 1)$ and $\nabla g = (-1, -1)$, so $\mu = 1$ works and $g(x^*) = 0$.
By sufficiency, $x^*$ is the global minimizer.

The constraint qualification is needed.
For minimize $x$ subject to $x^2 \le 0$ on $\R$, the minimizer is $0$, but $1 + \mu \cdot 0 = 0$ has no solution.

## Explanations

### L1 human

At a constrained minimum, the downhill direction of the objective must be blocked by the active constraints.
The KKT conditions say this with numbers: the gradient of the objective is balanced by a nonnegative combination of the gradients of the constraints that are tight.
Constraints that are not tight get weight zero.

### L2 human

The theorem extends Lagrange multipliers to inequality constraints and is the central optimality condition of nonlinear programming.
Algorithms such as sequential quadratic programming and interior-point methods solve the KKT system.
The weaker [[Fritz John conditions|6X8P5AXP60]] need no constraint qualification but allow a zero multiplier on the objective.
For convex problems under Slater's condition, KKT points are exactly the primal parts of saddle points of the Lagrangian, and the multipliers solve the dual.
