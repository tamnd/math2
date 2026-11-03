---
tag: B7SN6E6NAC
kind: definition
name: Robust optimization
msc: [90C17, 90C47]
defines: MRNW9644HH
uses: [NS0Q42Y3FX, 0BTMQ04556, 0RFWW56Y22]
sources:
  - url: https://en.wikipedia.org/wiki/Robust_optimization
---

## Definition

Let $X \subseteq \R^n$ be a set of decisions and let $U$ be a nonempty set, the *uncertainty set*.
Let $f \colon X \times U \to \R$ and $g_1, \dots, g_m \colon X \times U \to \R$.
The *robust counterpart* of the uncertain [[optimization problem|NS0Q42Y3FX]] of minimizing $f(x, u)$ subject to $g_i(x, u) \le 0$ is the problem
$$\min_{x \in X} \; \sup_{u \in U} f(x, u) \quad \text{subject to} \quad g_i(x, u) \le 0 \ \text{ for all } u \in U \text{ and } i = 1, \dots, m.$$
A point that satisfies these constraints is *robust feasible*, and *robust optimization* is the solution of such robust counterparts.

## Remarks

Here $\sup$ is the [[supremum|0BTMQ04556]].
Replacing the objective by a new variable $t$ and the constraint $f(x, u) \le t$ for all $u \in U$, one may assume that only the constraints are uncertain.

Example: a linear constraint $a^T x \le b$ whose vector $a$ is only known to lie in the ball $U = \set{\bar a + \rho v : \norm{v}_2 \le 1}$, with $\rho > 0$.
By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], $\sup_{u \in U} u^T x = \bar a^T x + \rho \norm{x}_2$, attained at $v = x / \norm{x}_2$ when $x \ne 0$.
So the robust constraint is $\bar a^T x + \rho \norm{x}_2 \le b$, a second-order cone constraint.

Non-example: the problem with the constraint $\bar a^T x \le b$ only for the nominal value $\bar a$ is not the robust counterpart.
A point with $\bar a^T x = b$ and $x \ne 0$ violates $a^T x \le b$ for $a = \bar a + \rho x / \norm{x}_2 \in U$.
