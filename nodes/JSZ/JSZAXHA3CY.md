---
tag: JSZAXHA3CY
kind: definition
name: Bellman equation
msc: [90C39, 90C40, 49L20]
defines: Z94Z6BY8JG
uses: [R3FXF08WBH, K6G0DRQ3CP, 0VK6VEH345, 0QN69YA357]
sources:
  - url: https://en.wikipedia.org/wiki/Bellman_equation
---

## Definition

Let $S$ and $A$ be finite nonempty sets of states and actions.
For $s, s' \in S$ and $a \in A$, let $r(s, a) \in \R$ be a reward and let $p(s' \mid s, a) \ge 0$ be transition probabilities with $\sum_{s'} p(s' \mid s, a) = 1$.
Fix a discount factor $\gamma \in [0, 1)$.
The *Bellman optimality equation* for a function $V \colon S \to \R$ is
$$V(s) = \max_{a \in A} \left( r(s, a) + \gamma \sum_{s' \in S} p(s' \mid s, a) \, V(s') \right) \quad \text{for all } s \in S.$$
For a policy $\pi \colon S \to A$, the *Bellman equation of $\pi$* is the same system with $a = \pi(s)$ in place of the maximum.

## Remarks

The right-hand side defines an operator $T$ on $\R^S$, the Bellman operator.
It is a [[contraction|0QN69YA357]] of factor $\gamma$ for the maximum norm, since $\abs{\max_a u_a - \max_a w_a} \le \max_a \abs{u_a - w_a}$.
By the [[Banach fixed point theorem|0VK6VEH345]], the equation has a unique solution $V^*$, and it is the optimal [[value function|K6G0DRQ3CP]] of the discounted problem.
A policy that attains the maximum in every state is optimal.
Finite-horizon versions read $V_t(s) = \max_a \left( r_t(s, a) + \sum_{s'} p_t(s' \mid s, a) V_{t+1}(s') \right)$, solved backward from a terminal value $V_T$.

Example: one state $s$, one action, $r(s, a) = 1$ and $p(s \mid s, a) = 1$.
The equation reads $V(s) = 1 + \gamma V(s)$, so $V(s) = 1 / (1 - \gamma) = \sum_{t \ge 0} \gamma^t$, the total discounted reward.

Non-example: with $\gamma = 1$ in this example, the equation $V(s) = 1 + V(s)$ has no solution.
The hypothesis $\gamma < 1$ fails, and the total reward is infinite.
