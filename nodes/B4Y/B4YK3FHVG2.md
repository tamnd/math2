---
tag: B4YK3FHVG2
kind: statement
role: theorem
name: Sion's minimax theorem
msc: [90C47, 49J35, 91A05]
uses: [T32W553W95, 02AS45T3H9, 0R6EWFKRCF, RN4G8SGP6P, S4RMH7JQB8, 7MFNVVJHTE]
about: [7MFNVVJHTE]
sources:
  - url: https://en.wikipedia.org/wiki/Minimax_theorem
---

## Statement

Let $X$ be a [[compact|0R6EWFKRCF]] [[convex|02AS45T3H9]] subset of a [[topological vector space|T32W553W95]], and let $Y$ be a convex subset of a topological vector space.
Let $f \colon X \times Y \to \R$ be a function such that:

1. For each $y \in Y$, the function $x \mapsto f(x, y)$ is lower [[semicontinuous|RN4G8SGP6P]] and [[quasiconvex|S4RMH7JQB8]] on $X$.
2. For each $x \in X$, the function $y \mapsto f(x, y)$ is upper semicontinuous and quasiconcave on $Y$.

Then
$$\min_{x \in X} \sup_{y \in Y} f(x, y) = \sup_{y \in Y} \min_{x \in X} f(x, y).$$

## Remarks

A function $\varphi$ is quasiconcave when $-\varphi$ is quasiconvex.
The inequality $\ge$ holds for every function, since $\min_x f(x, y') \le f(x', y') \le \sup_y f(x', y)$ for all $x', y'$.
The minima exist because a supremum of lower semicontinuous functions is lower semicontinuous and $X$ is compact.
Sion's proof (1958) uses the Knaster–Kuratowski–Mazurkiewicz lemma.
Komiya later gave an elementary proof.

If $Y$ is also compact, the supremum is a maximum, and $f$ has a [[saddle point|7MFNVVJHTE]] on $X \times Y$.
For bilinear $f$ on two simplices this is [[von Neumann's minimax theorem|GJ8VTBFNP2]] for mixed strategies of a zero-sum game.

Example: $X = Y = [0, 1]$ and $f(x, y) = (x - y)^2$ fails the hypotheses, since $y \mapsto (x - y)^2$ is not quasiconcave.
Here $\min_x \max_y f = 1/4$ at $x = 1/2$, while $\max_y \min_x f = 0$.
In contrast, $f(x, y) = x^2 - y^2$ satisfies them, and both sides equal $0$.

Compactness of $X$ cannot be dropped.
For $X = Y = \R$ and $f(x, y) = x + y$, the left side is $+\infty$ and the right side is $-\infty$.

## Explanations

### L1 human

Two players choose $x$ and $y$; the first wants $f$ small and the second wants it large.
The theorem says that, under convexity conditions, it does not matter who has to move first.
Without convexity, the player who moves second has an advantage.

### L2 human

Sion's theorem generalizes von Neumann's theorem from bilinear functions on simplices to quasiconvex-quasiconcave functions on convex sets, with only semicontinuity.
It is used to exchange a minimum and a maximum in robust optimization, statistics and learning theory.
In convex programming it gives strong duality when the set of primal points is compact.
Related results are the [[Ky Fan minimax inequality|QM2EBW5CD9]] and the saddle point theorems for Lagrangians.
