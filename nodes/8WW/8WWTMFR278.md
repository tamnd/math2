---
tag: 8WWTMFR278
kind: statement
role: theorem
name: Cartan's theorem on fine continuity of superharmonic functions
msc: [31C40, 31B05]
uses: [X4V2S56YQQ, 7DGF6MMEGX, W2ZD4XP74R]
about: [X4V2S56YQQ, W2ZD4XP74R]
sources:
  - url: https://en.wikipedia.org/wiki/Fine_topology_(potential_theory)
---

## Statement

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be an open set, let $u$ be a [[superharmonic function|X4V2S56YQQ]] on $\Omega$, and let $x \in \Omega$.
Then there is a set $E \subseteq \Omega \setminus \set{x}$ that is [[thin|7DGF6MMEGX]] at $x$ such that
$$\lim_{y \to x,\ y \in \Omega \setminus E} u(y) = u(x).$$

## Remarks

Equivalently, $u$ is continuous at $x$ for the [[fine topology|W2ZD4XP74R]], once the finely open sets are described as the sets whose complement is thin at each of their points.
Idea of the proof: if $u(x) = +\infty$, lower semicontinuity already gives $u(y) \to +\infty$ as $y \to x$, and one takes $E = \emptyset$.
If $u(x) < \infty$, then for each $\varepsilon > 0$ the set $\set{y : u(y) > u(x) + \varepsilon}$ is thin at $x$, with $u$ itself as the witness.
These sets, cut down to suitable shrinking balls about $x$, combine into a single set $E$ that is still thin at $x$.
This step uses the description of thinness by capacity.
Example: in $\R^3$, the potential $u(y) = \sum_{k \ge 1} 4^{-k} \abs{y - 2^{-k} e_1}^{-1}$ is superharmonic with $u(0) = 1$ and $u = +\infty$ at the points $2^{-k} e_1$.
So $u$ is not continuous at $0$.
It tends to $1$ as $y \to 0$ outside the union $E$ of the balls of radius $k^2 4^{-k}$ about the points $2^{-k} e_1$, by dominated convergence.
This $E$ is thin at $0$ by Wiener's criterion, since $\sum_k 2^k k^2 4^{-k} < \infty$.
The exceptional set cannot be dropped in general, as this example shows.

## Explanations

### L1 human

A superharmonic function can jump up at points arbitrarily close to $x$.
The theorem says that these jumps happen only on a set that is negligible near $x$ in the sense of potential theory.
Outside that set, the function behaves continuously at $x$.

### L2 human

This is the result that makes the fine topology useful.
It shows that the topology defined abstractly by superharmonic functions has a concrete description by thin sets, so fine limits can be checked with capacities through Wiener's criterion.
Fine limits then appear in the boundary theory of harmonic functions, for instance in the fine form of Fatou-type theorems on the Martin boundary.
