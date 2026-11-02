---
tag: F64JX05VJX
kind: definition
name: Dynamic programming in continuous time
msc: [49L20, 49L12, "93E20"]
defines: QPS8VSJGMJ
uses: [K6G0DRQ3CP, T3V6ZNAMDN, SJP9HW82VX]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_programming
---

## Definition

Consider a finite-horizon [[optimal control|T3V6ZNAMDN]] problem on $[0, T]$ with dynamics $y' = f(s, y, u)$, controls with values in a set $U$, running cost $L$ and terminal cost $g$.
Let $V$ be its [[value function|K6G0DRQ3CP]].
The *dynamic programming principle* for the problem is the identity, for all $0 \le t \le s \le T$ and $x \in \R^n$,
$$V(t, x) = \inf_{u} \Big( \int_t^s L(r, y(r), u(r)) \, dr + V(s, y(s)) \Big).$$
Here the infimum is over measurable controls $u \colon [t, s] \to U$, and $y$ is the trajectory with $y(t) = x$.
*Dynamic programming in continuous time* is the method that derives from this principle a partial differential equation for $V$.
That equation is the [[Hamilton–Jacobi–Bellman equation|SJP9HW82VX]] $V_t + \min_{u \in U} \big( L(t, x, u) + \nabla_x V \cdot f(t, x, u) \big) = 0$ with $V(T, x) = g(x)$.
One then obtains optimal controls by choosing, at each $(t, x)$, a minimizer $u$ of this expression.

## Remarks

The principle holds under the standing hypotheses of the value function: $U$ compact, $f$ continuous and Lipschitz in the state, and $L$, $g$ continuous.
Its proof splits a control on $[t, T]$ into its parts on $[t, s]$ and $[s, T]$.
Example: for $y' = u$, $U = [-1, 1]$, $L = 0$ and $g(x) = \abs{x}$, the value function is $V(t, x) = \max(\abs{x} - (T - t), 0)$.
Where $\abs{x} > T - t$ it equals $\abs{x} - (T - t)$, so $V_t = 1$ and $\min_{\abs{u} \le 1} V_x u = -1$, and the equation holds.
The minimizer $u = -\sgn(x)$ is the optimal feedback.
Non-example: a greedy rule that minimizes only the running cost $L$ at each instant, ignoring $V$, does not follow the principle and is in general not optimal.
