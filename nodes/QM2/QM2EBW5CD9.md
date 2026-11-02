---
tag: QM2EBW5CD9
kind: statement
role: theorem
name: Ky Fan minimax inequality
msc: [49J35, 47J20, 91A10]
uses: [T32W553W95, 0R6EWFKRCF, 02AS45T3H9, RN4G8SGP6P, S4RMH7JQB8]
sources:
  - url: https://en.wikipedia.org/wiki/Ky_Fan_inequality_(game_theory)
    locator: Statement
---

## Statement

Let $E$ be a real Hausdorff [[topological vector space|T32W553W95]], and let $C \subseteq E$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $f \colon C \times C \to \R$ be a function such that:

1. for every $y \in C$, the function $x \mapsto f(x, y)$ is lower [[semicontinuous|RN4G8SGP6P]] on $C$;
2. for every $x \in C$, the function $y \mapsto f(x, y)$ is quasiconcave on $C$, that is, $y \mapsto -f(x, y)$ is [[quasiconvex|S4RMH7JQB8]].

Then there is $\bar x \in C$ with
$$\sup_{y \in C} f(\bar x, y) \le \sup_{y \in C} f(y, y).$$
In particular, if $f(y, y) \le 0$ for all $y \in C$, then there is $\bar x \in C$ with $f(\bar x, y) \le 0$ for all $y \in C$.

## Remarks

It suffices to prove the second form, applied to $f - c$ with $c = \sup_y f(y, y)$ when $c$ is finite; the first form is trivial when $c = +\infty$.
For each $y$ the set $S(y) = \set{x \in C : f(x, y) \le 0}$ is closed by clause 1.
If a point $x$ of the convex hull of $y_1, \dots, y_k$ lay outside every $S(y_i)$, clause 2 would give $f(x, x) \ge \min_i f(x, y_i) > 0$, which is impossible.
So the sets $S(y)$ satisfy the hypothesis of the Knaster–Kuratowski–Mazurkiewicz lemma in Fan's form, and by compactness of $C$ they have a common point $\bar x$.

Example: let $\Delta_k$ be the set of probability vectors in $\R^k$, and let $A$ be a real $m \times n$ matrix.
The payoff of the matrix game is $g(p, q) = p^T A q$ for $p \in \Delta_m$ and $q \in \Delta_n$, as in [[von Neumann's minimax theorem|GJ8VTBFNP2]].
Let $C = \Delta_m \times \Delta_n$, and for $z = (p, q)$ and $w = (p', q')$ in $C$ let $f(z, w) = g(p', q) - g(p, q')$.
This $f$ is continuous, affine in $w$, and $f(z, z) = 0$.
The point $\bar z = (\bar p, \bar q)$ given by the theorem satisfies $g(p', \bar q) \le g(\bar p, q')$ for all $p', q'$, so $(\bar p, \bar q)$ is a pair of optimal strategies.

Compactness cannot be dropped: on $C = [0, \infty) \subseteq \R$, the function $f(x, y) = y - x$ satisfies both clauses and $f(y, y) = 0$, but for every $x$ there is $y > x$ with $f(x, y) > 0$.

## Explanations

### L1 human

The inequality gives a point $\bar x$ that no other point $y$ can beat, as measured by $f(\bar x, y)$.
It asks only that comparing a point with itself gives no gain, and that $f$ has some mild continuity and convexity.
Many existence results for equilibria have this form, so they all follow from this one statement.

### L2 human

Ky Fan proved the inequality in 1972 as a common source of minimax theorems, fixed-point theorems and existence theorems for equilibria.
From it one derives the minimax theorems of von Neumann and Sion, Nash equilibria of games with convex strategy sets, and solutions of [[variational inequalities|6QS7X5GVMY]] on compact convex sets.
Its proof rests on the KKM lemma, which is equivalent to the Brouwer fixed-point theorem.
