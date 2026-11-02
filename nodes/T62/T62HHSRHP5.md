---
tag: T62HHSRHP5
kind: statement
role: theorem
name: Maximum principle for harmonic functions
msc: [31B05, 35B50]
uses: [0DEB0JMN0W, 0HYPR64JM2, D2JF19HF91]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_principle
---

## Statement

Let $U \subseteq \R^n$ be a domain, that is, a connected open set, and let $u \colon U \to \R$ be [[harmonic|0DEB0JMN0W]].

1. (Strong maximum principle.) If there is $a \in U$ with $u(a) = \sup_U u$, then $u$ is constant on $U$.
2. (Weak maximum principle.) If $U$ is bounded and $u$ extends continuously to the closure $\overline{U}$, then $\max_{\overline{U}} u = \max_{\partial U} u$.

## Remarks

Proof idea for part 1: the set $A = \set{x \in U : u(x) = \sup_U u}$ is closed in $U$ by continuity.
It is open: if $x \in A$ and $\overline{B}(x, r) \subseteq U$, the [[mean value property|0HYPR64JM2]] over the ball makes $u(x)$ the average of values $\le u(x)$, which forces $u = u(x)$ on the ball.
As $U$ is connected and $A$ is not empty, $A = U$.
Part 2 follows: the maximum of $u$ on the compact set $\overline{U}$ is attained, and if it were attained only inside, part 1 would make $u$ constant.
Example: $u(x, y) = x^2 - y^2$ on the unit disc takes its maximum $1$ on the boundary, at $(\pm 1, 0)$, and the value $0$ at the centre.
Boundedness is needed in part 2: on the half-plane $\set{x > 0}$, $u = x$ is $0$ on the boundary and positive inside.
Connectedness is needed in part 1.
On two disjoint discs, the function equal to $0$ on one and $1$ on the other is harmonic and attains its maximum without being constant.
This is the harmonic case of the general [[maximum principle|D2JF19HF91]] for elliptic operators.

## Explanations

### L1 human

A harmonic function cannot have a peak inside its domain.
Its largest values on a bounded region are reached on the edge.
Think of the height of a soap film spanned on a wire frame: the highest point lies on the wire.

### L2 human

The weak maximum principle gives uniqueness for the Dirichlet problem.
Two harmonic functions with the same boundary values differ by a harmonic function that is $0$ on the boundary, hence $0$ inside.
It also gives stability: if the boundary values of two solutions differ by at most $\varepsilon$, then the solutions differ by at most $\varepsilon$ everywhere.
Subharmonic functions satisfy the same maximum principle, and Perron's method builds solutions of the Dirichlet problem from it.
