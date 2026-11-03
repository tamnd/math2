---
tag: Y4HPJXFS0D
kind: definition
name: Bilevel optimization
msc: [90C26, 91A65, 90C30]
defines: 3VE9BSJQJA
uses: [NS0Q42Y3FX, 1TTKMRW8PD]
sources:
  - url: https://en.wikipedia.org/wiki/Bilevel_optimization
---

## Definition

Let $X$ and $Y$ be nonempty sets.
Let $F, f \colon X \times Y \to \R$ be the *upper-level* and *lower-level objectives*.
For each $x \in X$, let $Y(x) \subseteq Y$ be the lower-level [[feasible set|1TTKMRW8PD]], and let
$$S(x) = \arg\min_{y \in Y(x)} f(x, y)$$
be the set of solutions of the *lower-level problem*.
A *bilevel optimization problem*, in its optimistic form, is the [[optimization problem|NS0Q42Y3FX]]
$$\min_{x \in X, \; y \in Y} F(x, y) \quad \text{subject to} \quad y \in S(x).$$
In the *pessimistic form*, the leader minimizes $\sup_{y \in S(x)} F(x, y)$ over the $x \in X$ with $S(x) \ne \emptyset$.

## Remarks

Upper-level constraints $G(x, y) \le 0$ may be added.
The two forms agree when $S(x)$ has exactly one point for each $x$.

Example: $X = [0, 1]$, $Y = \R$, $f(x, y) = (y - x)^2$ and $F(x, y) = (x - 1)^2 + y$.
The lower level gives $S(x) = \set{x}$, so the problem becomes minimizing $(x - 1)^2 + x$ over $[0, 1]$.
Its derivative $2(x - 1) + 1$ vanishes at $x = 1/2$, so the solution is $(x, y) = (1/2, 1/2)$ with value $3/4$.

Non-example: minimizing $F(x, y)$ over all $(x, y) \in [0, 1] \times \R$ ignores the condition $y \in S(x)$.
In the example, $F$ is unbounded below in $y$, so this single-level problem has no solution.
