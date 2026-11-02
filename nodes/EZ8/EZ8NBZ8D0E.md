---
tag: EZ8NBZ8D0E
kind: definition
name: Optimal control
msc: [49J15, 49K15, 93C15]
defines: T3V6ZNAMDN
uses: [8M31QKB0GW, SBQVGQPXT1, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
---

## Definition

Let $x' = f(x, u)$ be a [[control system|SBQVGQPXT1]] on $\R^n$ with control set $U \subseteq \R^m$.
Fix a time horizon $T > 0$, an initial state $x_0 \in \R^n$ and a closed target set $S \subseteq \R^n$.
Let $L \colon \R^n \times U \to \R$ and $\varphi \colon \R^n \to \R$ be [[continuous functions|0X3WGX95FE]], the running cost and the terminal cost.
For an [[admissible control|8M31QKB0GW]] $u$ for $(x_0, T, S)$ with trajectory $x_u$, the *cost* is
$$J(u) = \varphi\big(x_u(T)\big) + \int_0^T L\big(x_u(t), u(t)\big) \, dt.$$
An admissible control $u^*$ is an *optimal control* if $J(u^*) \le J(u)$ for every admissible control $u$ for $(x_0, T, S)$.
The pair $(u^*, x_{u^*})$ is then an optimal pair, and $x_{u^*}$ is an optimal trajectory.

## Remarks

The integral exists, because $x_u$ is continuous and $u$ is essentially bounded, so the integrand is a bounded measurable function.
A cost with both terms is in Bolza form; $L = 0$ gives the Mayer form and $\varphi = 0$ the Lagrange form.
An optimal control need not exist, and when it exists it need not be unique.

Example: $x' = u$ on $\R$ with $U = [-1, 1]$, $x_0 = 0$, $T = 1$, $S = \R$, $L = 0$ and $\varphi(x) = -x$.
Every admissible $u$ gives $x_u(1) = \int_0^1 u(t) \, dt \le 1$, so $J(u) \ge -1$.
The control $u^* = 1$ gives $J(u^*) = -1$, so it is optimal.

Non-example: the control $u = 0$ in the same problem is admissible but not optimal, since $J(0) = 0 > -1 = J(u^*)$.
