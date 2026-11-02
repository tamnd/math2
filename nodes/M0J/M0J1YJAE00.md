---
tag: M0J1YJAE00
kind: statement
role: theorem
name: Widder's theorem
msc: [35K05, 35K15, 35B09]
uses: [VP2HN86VAG, KD404MF042]
about: [VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Heat_equation
---

## Statement

Let $n \ge 1$ and $T > 0$.
Let $u \colon \R^n \times [0, T) \to \R$ be continuous, with $\partial_t u$ and the second partial derivatives in $x$ continuous on $\R^n \times (0, T)$.
Assume that $u$ solves the [[heat equation|VP2HN86VAG]] $\partial_t u = \Delta u$ on $\R^n \times (0, T)$ and that $u \ge 0$.
Let $g(x) = u(x, 0)$.
Then for all $x \in \R^n$ and $0 < t < T$,
$$u(x, t) = \int_{\R^n} \Phi(x - y, t) \, g(y) \, dy,$$
where $\Phi$ is the [[heat kernel|KD404MF042]] of $\R^n$.

## Remarks

In particular, a nonnegative solution with initial value $0$ is identically $0$, so nonnegative solutions of the Cauchy problem are unique.
No growth condition at infinity is needed, which is the point of the theorem.
The sign condition cannot be dropped: [[Tychonoff's example|RN4J24CD83]] is a nonzero solution with initial value $0$, and it changes sign.
One half of the proof is a comparison on large balls with the maximum principle, which gives $u \ge \int \Phi(x - y, t) g(y) \, dy$.
The main work is to show that the difference, a nonnegative solution with initial value $0$, vanishes.
David Widder proved the theorem for $n = 1$; the version stated holds in every dimension.

## Explanations

### L1 human

Temperatures measured from absolute zero are never negative.
Widder's theorem says that for such physical temperatures on all of space, the initial temperature determines the future completely.
The future is then given by the usual formula, which spreads the initial heat with Gaussian bells.

### L2 human

Without a sign condition, uniqueness for the Cauchy problem needs a growth bound such as $\abs{u} \le A e^{a \abs{x}^2}$.
Widder's theorem replaces this bound by positivity, which is often easier to check in applications, for example for probability densities.
It is related to the parabolic Harnack inequality for nonnegative solutions.
