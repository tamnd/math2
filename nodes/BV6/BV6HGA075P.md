---
tag: BV6HGA075P
kind: definition
name: Value function
msc: [49L20, 49L12, "93E20"]
defines: K6G0DRQ3CP
uses: [T3V6ZNAMDN, 8M31QKB0GW, ZPDTVZQN5K, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Value_function
---

## Definition

Let $U \subseteq \R^m$ be a nonempty [[compact set|0R6EWFKRCF]] and $T > 0$.
Let $f \colon [0, T] \times \R^n \times U \to \R^n$ be continuous and Lipschitz in $x$ uniformly in $(t, u)$.
Let $L \colon [0, T] \times \R^n \times U \to \R$ and $g \colon \R^n \to \R$ be continuous.
For $(t, x) \in [0, T] \times \R^n$ and a measurable control $u \colon [t, T] \to U$, let $y$ be the trajectory of the [[control system|ZPDTVZQN5K]] $y' = f(s, y, u)$ with $y(t) = x$, and set
$$J(t, x; u) = \int_t^T L(s, y(s), u(s)) \, ds + g(y(T)).$$
The *value function* of this [[optimal control|T3V6ZNAMDN]] problem is the function $V \colon [0, T] \times \R^n \to \R$ given by
$$V(t, x) = \inf \set{ J(t, x; u) : u \colon [t, T] \to U \text{ measurable} }.$$

## Remarks

Under these hypotheses the trajectories from $(t, x)$ stay in a bounded set, so $V$ is finite.
By definition $V(T, x) = g(x)$, and a control $u$ is optimal from $(t, x)$ exactly when $J(t, x; u) = V(t, x)$.
Example: $n = m = 1$, $U = [-1, 1]$, $f(t, x, u) = u$, $L = 0$ and $g(x) = \abs{x}$.
From $(t, x)$ one can move toward $0$ at speed at most $1$, so $V(t, x) = \max(\abs{x} - (T - t), 0)$.
This $V$ is Lipschitz but not differentiable where $\abs{x} = T - t$ and $t < T$.
Non-example: the cost $J(t, x; u_0)$ of one fixed control $u_0$ is in general not the value function.
For $u_0 = 0$ in the example it is $\abs{x}$, which is larger than $V(t, x)$ when $x \ne 0$ and $t < T$.
For maximization problems the infimum is replaced by a supremum.
For infinite-horizon problems with discounting, $V$ depends only on the initial state.
