---
tag: 0G3DBXRRQJ
kind: statement
role: theorem
name: Continuous dependence on initial data
msc: [34A12]
uses: [055VVSN00V, 04SW7WECS8, 07EJHQYR9A]
sources:
  - url: https://en.wikipedia.org/wiki/Well-posed_problem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: Integral form for continuous functions
---

## Statement

Let $J$ be an interval, let $U$ be an open subset of $\mathbb{R}^n$, let $K \ge 0$, and let $f : J \times U \to \mathbb{R}^n$ be continuous.
Assume that $\|f(t, x) - f(t, y)\| \le K \|x - y\|$ for all $t \in J$ and $x, y \in U$.
Let $a < b$ with $[a, b] \subseteq J$, and let $\gamma_1, \gamma_2 : [a, b] \to U$ be [[solutions|04SW7WECS8]] of $x' = f(t, x)$.
Then
$$\|\gamma_1(t) - \gamma_2(t)\| \le \|\gamma_1(a) - \gamma_2(a)\|\, e^{K (t - a)} \quad \text{for each } t \in [a, b].$$

## Remarks

So the solution at time $t$ is a Lipschitz function of the initial value, with constant $e^{K(t - a)}$.
The proof applies [[Grönwall's inequality|07EJHQYR9A]] to $u(t) = \|\gamma_1(t) - \gamma_2(t)\|$.
Existence, uniqueness and continuous dependence together make the initial value problem well posed, in the sense of Jacques Hadamard.
For equal initial values, the bound gives [[uniqueness|025PKW8AMR]] again.

## Explanations

### L1 human

If two solutions start close together, they stay close for a while.
Their distance can grow, but at most exponentially, with rate given by the Lipschitz constant.
So a small error in the initial value gives a small error in the solution over a bounded time.
