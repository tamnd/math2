---
tag: QZYB0HEPZ8
kind: definition
name: Push–relabel maximum flow algorithm
msc: [90C35, 05C21, 05C85]
defines: HNH4C6DV46
uses: [ZSNXTW5E2K, EXMR7RYRTP, 0KFYGSHHF5]
sources:
  - url: https://en.wikipedia.org/wiki/Push%E2%80%93relabel_maximum_flow_algorithm
---

## Definition

Let $(V, E)$ be a finite [[directed graph|0KFYGSHHF5]] with $n = \abs{V}$ vertices, a source $s$ and a sink $t \ne s$.
Extend the capacity to all ordered pairs by a function $c \colon V \times V \to [0, \infty)$ with $c(u, v) = 0$ when $(u, v) \notin E$; this is a [[flow network|ZSNXTW5E2K]].
A *preflow* is a function $f \colon V \times V \to \R$ such that:

1. $f(u, v) = -f(v, u)$ for all $u, v$.
2. $f(u, v) \le c(u, v)$ for all $u, v$.
3. The *excess* $e(v) = \sum_{u \in V} f(u, v)$ satisfies $e(v) \ge 0$ for every $v \ne s$.

The *residual capacity* is $r(u, v) = c(u, v) - f(u, v)$, and $(u, v)$ is a *residual edge* if $r(u, v) > 0$.
A vertex $v \notin \set{s, t}$ is *active* if $e(v) > 0$.
A *height function* is a map $h \colon V \to \Z_{\ge 0}$ with $h(s) = n$, $h(t) = 0$, and $h(u) \le h(v) + 1$ for every residual edge $(u, v)$.

The *push–relabel algorithm* starts with $h(s) = n$, $h(v) = 0$ for $v \ne s$, $f(s, v) = c(s, v) = -f(v, s)$ for all $v$, and $f = 0$ on the other pairs.
While some vertex is active, it applies one of two operations to an active vertex $u$:

1. *Push* along $(u, v)$, allowed when $r(u, v) > 0$ and $h(u) = h(v) + 1$: let $\delta = \min(e(u), r(u, v))$, add $\delta$ to $f(u, v)$ and subtract $\delta$ from $f(v, u)$.
2. *Relabel* $u$, allowed when no push from $u$ is allowed: set $h(u) = 1 + \min\set{h(v) : r(u, v) > 0}$.

When no vertex is active, it returns $f$.

## Remarks

Each operation keeps $f$ a preflow and $h$ a height function.
An active vertex always has a residual edge, so relabel is well defined.
Since $h(s) = n$, no residual path leads from $s$ to $t$ at any time.
At the end there is no active vertex, so $f$ is a flow with no augmenting path, and by the [[max-flow min-cut theorem|4HMR4KQ01T]] it is a maximum flow.
Heights stay below $2n$, which bounds the number of operations; the generic algorithm uses $O(n^2 \abs{E})$ operations, and the first-in first-out choice of active vertices gives $O(n^3)$.

Example: let $V = \set{s, a, t}$ with $c(s, a) = 3$ and $c(a, t) = 2$.
Initially $f(s, a) = 3$, so $e(a) = 3$ and $a$ is active with $h(a) = 0 = h(t)$.
No push is allowed, so relabel gives $h(a) = 1$, and a push sends $2$ to $t$.
Now $e(a) = 1$, the only residual edge from $a$ is $(a, s)$, and relabel gives $h(a) = n + 1 = 4$.
A push returns $1$ to $s$, no vertex is active, and the flow of value $2$ is maximum.

Non-example: the function with $f(s, a) = 1$ and $f(a, t) = 2$ (and the opposite values on reversed pairs) is not a preflow.
The excess at $a$ is $1 - 2 = -1 < 0$, so clause 3 fails.
