---
tag: XEX7QZV1BS
kind: statement
role: theorem
name: Filippov's existence theorem
msc: [49J15, 34A60]
uses: [1J8TYT7C49, 8M31QKB0GW, ZPDTVZQN5K, 02AS45T3H9, 0R6EWFKRCF, 9ZSMF6NYKM, 7RPV2T29CF]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_inclusion
---

## Statement

Let $U \subseteq \R^m$ be a nonempty [[compact set|0R6EWFKRCF]], let $T > 0$, and let $f \colon [0, T] \times \R^n \times U \to \R^n$ be continuous.
Let $x_0 \in \R^n$, let $S \subseteq \R^n$ be a closed set, and let $\varphi \colon \R^n \to \R$ be continuous.
Call a measurable map $u \colon [0, T] \to U$ an [[admissible control|8M31QKB0GW]] if the [[control system|ZPDTVZQN5K]] $x'(t) = f(t, x(t), u(t))$ with $x(0) = x_0$ has an absolutely continuous solution $x$ on $[0, T]$ with $x(T) \in S$.
Assume that:

1. at least one admissible control exists;
2. there is a constant $R$ such that $\abs{x(t)} \le R$ for every $t \in [0, T]$ and every trajectory $x$ of an admissible control;
3. for every $(t, x) \in [0, T] \times \R^n$ the set of velocities $f(t, x, U) = \set{f(t, x, v) : v \in U}$ is [[convex|02AS45T3H9]].

Then the [[Mayer problem|1J8TYT7C49]] of minimizing $\varphi(x(T))$ over all admissible controls has a solution.
That is, there is an admissible control $u^*$ with trajectory $x^*$ such that $\varphi(x^*(T)) \le \varphi(x(T))$ for every admissible trajectory $x$.

## Remarks

The proof is a compactness argument.
Take a minimizing sequence of trajectories; they are uniformly bounded with uniformly bounded derivatives, so the Arzelà–Ascoli theorem gives a subsequence that converges uniformly to an absolutely continuous limit $x^*$.
The convexity of the velocity sets shows that $x^*$ solves the [[differential inclusion|9ZSMF6NYKM]] $x'(t) \in f(t, x(t), U)$ for almost every $t$.
A measurable selection result, known as Filippov's lemma, then gives a measurable control $u^*$ with $x^{*\prime}(t) = f(t, x^*(t), u^*(t))$, and continuity of $\varphi$ shows that $u^*$ is optimal.

Convexity cannot be dropped.
Take $n = 2$, $U = \set{-1, 1}$, $f(t, x, u) = (u, x_1^2)$, $x_0 = (0, 0)$, $T = 1$, $S = \set{0} \times \R$ and $\varphi(x) = x_2$, so that the cost is $\int_0^1 x_1(t)^2 \, dt$ with $x_1' = \pm 1$ and $x_1(1) = 0$.
Controls that switch faster and faster keep $x_1$ close to $0$, so the infimum of the cost is $0$.
A cost $0$ would need $x_1 \equiv 0$, hence $x_1' = 0 \notin \set{-1, 1}$, so no optimal control exists.
Here the velocity sets $\set{(-1, x_1^2), (1, x_1^2)}$ are not convex.

A Lagrange cost $\int_0^T L(t, x, u) \, dt$ is handled by adding the state $y' = L(t, x, u)$; the convexity hypothesis then concerns the sets $\set{(f(t, x, v), L(t, x, v) + \gamma) : v \in U, \gamma \ge 0}$.
Hypothesis 2 holds, for example, when $\abs{f(t, x, v)} \le C(1 + \abs{x})$ for a constant $C$, by Grönwall's inequality.

## Explanations

### L1 human

An optimal control problem can fail to have a best solution, because cheaper and cheaper controls may wiggle faster and faster without reaching a limit control.
Filippov's theorem says that this cannot happen when the control values form a compact set and, at each state, the possible velocities form a convex set.
Then a minimizing sequence settles down to a genuine optimal control.

### L2 human

The theorem is the optimal control version of the direct method of the calculus of variations.
Compactness comes from bounded velocities, and convexity of the velocity sets plays the role of lower semicontinuity.
When convexity fails, one passes to relaxed controls, which convexify the velocity sets.
The relaxed problem then has a minimizer, and under mild extra hypotheses its value is the infimum of the original problem.
Existence is the first step before using necessary conditions such as [[Pontryagin's maximum principle|7RPV2T29CF]], which only describe minimizers that exist.
For linear systems $x' = A x + B u$ with $U$ compact and convex, the velocity sets are automatically convex.
