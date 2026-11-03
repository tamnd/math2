---
tag: WY2PMTVNZ1
kind: definition
name: Constraint
msc: [90C30, 90C05]
defines: X3663P90AE
uses: [0BSJ7RQ9BW, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_(mathematics)
---

## Definition

Let $X$ be a [[set|0BSJ7RQ9BW]], the set of candidate points of an optimization problem.
A *constraint* on $X$ is a condition on $x \in X$, given by a [[function|0EPAT51DXQ]] $g \colon X \to \R$ in one of these forms:

1. an *equality constraint* $g(x) = 0$;
2. an *inequality constraint* $g(x) \le 0$.

A point $x \in X$ *satisfies* the constraint if the condition holds at $x$.
An inequality constraint $g(x) \le 0$ is *active* (or *binding*) at a point $x$ that satisfies it if $g(x) = 0$, and *inactive* if $g(x) < 0$.

## Remarks

More general constraints are written as $x \in S$ for a subset $S \subseteq X$, for example an integrality constraint $x \in \Z^n$ with $X = \R^n$.
A constraint $g(x) \ge 0$ is the inequality constraint $-g(x) \le 0$, and $g(x) = c$ is the equality constraint $g(x) - c = 0$.

Example: on $X = \R^2$, take $g(x, y) = x^2 + y^2 - 1$ and the constraint $g \le 0$.
The point $(1, 0)$ satisfies it with $g(1, 0) = 0$, so the constraint is active there.
The point $(0, 0)$ satisfies it with $g(0, 0) = -1 < 0$, so it is inactive there.

Non-example: the point $(1, 1)$ does not satisfy this constraint, since $g(1, 1) = 1 > 0$.
