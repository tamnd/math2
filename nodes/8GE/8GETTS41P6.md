---
tag: 8GETTS41P6
kind: definition
name: Admissible control
msc: [49J15, 93C15]
defines: 8M31QKB0GW
uses: [SBQVGQPXT1, YYNCJSR0PJ, ZT6F4C2YHK]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
---

## Definition

Let $x' = f(x, u)$ be a [[control system|SBQVGQPXT1]] on $\R^n$ with control set $U \subseteq \R^m$.
Fix a time horizon $T > 0$, an initial state $x_0 \in \R^n$ and a closed target set $S \subseteq \R^n$.
An *admissible control* for $(x_0, T, S)$ is a function $u \colon [0, T] \to \R^m$ such that:

1. $u$ is [[measurable|YYNCJSR0PJ]] and essentially bounded, and $u(t) \in U$ for almost every $t \in [0, T]$;
2. there is an [[absolutely continuous|ZT6F4C2YHK]] trajectory $x \colon [0, T] \to \R^n$ with $x(0) = x_0$ and $x'(t) = f(x(t), u(t))$ for almost every $t$;
3. this trajectory satisfies $x(T) \in S$.

## Remarks

By the local Lipschitz condition on $f$, the trajectory in clause 2 is unique when it exists.
Clause 2 can fail because the solution blows up before time $T$.
Many authors call any control satisfying clause 1 admissible, as in the [[control system|SBQVGQPXT1]] definition, and add clauses 2 and 3 as constraints of the problem.
Problems with free final time, state constraints or other control classes, such as piecewise continuous controls, change the clauses accordingly.

Example: $x' = u$ on $\R$ with $U = [-1, 1]$, $x_0 = 0$, $T = 1$ and $S = \set{\tfrac12}$.
The constant control $u = \tfrac12$ is admissible: it is bounded with values in $U$, and $x(t) = t/2$ gives $x(1) = \tfrac12$.

Non-example: the constant control $u = 1$ in the same setting satisfies clauses 1 and 2, with $x(t) = t$.
It fails clause 3, since $x(1) = 1 \notin S$.
