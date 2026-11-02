---
tag: EPXNCSP2MN
kind: statement
role: theorem
name: Mountain pass theorem
msc: ["58E05", 35J20, 47J30]
uses: [06GZ956657, 06EH97V2A7, 4724KRNHAT, 0YTCMFB4HC]
about: [0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Mountain_pass_theorem
same_as:
  wikidata: Q6925496
  wikipedia: Mountain pass theorem
---

## Statement

Let $X$ be a real [[Banach space|06GZ956657]] and let $I \colon X \to \R$ be a continuously [[Fréchet differentiable|06EH97V2A7]] functional that satisfies the [[Palais–Smale condition|4724KRNHAT]].
Assume that:

1. $I(0) = 0$;
2. there are $r > 0$ and $a > 0$ such that $I(u) \ge a$ for every $u \in X$ with $\norm{u} = r$;
3. there is $e \in X$ with $\norm{e} > r$ and $I(e) \le 0$.

Let $\Gamma$ be the set of continuous paths $\gamma \colon [0, 1] \to X$ with $\gamma(0) = 0$ and $\gamma(1) = e$, and let
$$c = \inf_{\gamma \in \Gamma} \max_{t \in [0, 1]} I(\gamma(t)).$$
Then $c \ge a$, and $c$ is a critical value of $I$: there is $u \in X$ with $I(u) = c$ and $I'(u) = 0$.
In particular $u$ is a [[critical point|0YTCMFB4HC]] of $I$ different from $0$ and from $e$.

## Remarks

Every path from $0$ to $e$ crosses the sphere $\norm{u} = r$, so its maximum is at least $a$, which gives $c \ge a$.
Suppose $c$ were not a critical value.
Then a deformation lemma, which uses the Palais–Smale condition, would push the sublevel set $\set{I \le c + \varepsilon}$ into $\set{I \le c - \varepsilon}$ while fixing $0$ and $e$.
This would produce a path with maximum below $c$.
The Palais–Smale condition cannot be dropped, even in $\R^2$.
The function $f(x, y) = x^2 + (1 - x)^3 y^2$ has a strict local minimum at the origin with value $0$, so it is at least some $a > 0$ on a small circle around it.
It also takes negative values, for example at $(2, 3)$, but its only critical point is the origin.
Indeed, $\partial_y f = 2(1 - x)^3 y$ vanishes only for $x = 1$ or $y = 0$; at $x = 1$ one has $\partial_x f = 2$, and for $y = 0$ one needs $x = 0$.
Antonio Ambrosetti and Paul Rabinowitz proved the theorem.
A typical application gives a nonzero weak solution of $-\Delta u = \abs{u}^{p-1} u$ with zero boundary values on a bounded domain of $\R^n$, for $1 < p < (n+2)/(n-2)$ when $n \ge 3$.

## Explanations

### L1 human

Picture a valley surrounded by a ring of mountains, with lower ground somewhere beyond the ring.
Any route from the valley to that lower ground has to climb, and the best route goes through the lowest mountain pass.
The theorem says that this pass is a point where the ground is flat, that is, a critical point.
For functionals on infinite-dimensional spaces one needs a compactness condition, the Palais–Smale condition, to make the argument work.

### L2 human

The theorem is a basic tool of critical point theory and of variational methods for nonlinear elliptic equations.
It finds solutions that are neither minima nor maxima of the energy, but saddle points.
For semilinear problems, $0$ is often a trivial solution and a local minimum, and the theorem gives a second, nontrivial solution.
It is the starting point of minimax methods, such as the linking theorems and Lusternik–Schnirelmann theory.
