---
tag: 0JTPMCCZT2
kind: statement
role: theorem
name: Estimate for approximate solutions
msc: [34A12, 34A45]
uses: [0FRX8JD7QH, 055VVSN00V, 07EJHQYR9A]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: lead section
---

## Statement

Let $J$ be an interval, let $U$ be an open subset of $\mathbb{R}^n$ and let $K \ge 0$. Let $f : J \times U \to \mathbb{R}^n$ satisfy $\|f(t, x) - f(t, y)\| \le K \|x - y\|$ for all $t \in J$ and $x, y \in U$.
Let $a < b$ with $[a, b] \subseteq J$, and let $\delta, \varepsilon_1, \varepsilon_2 \ge 0$.
Let $\gamma_1, \gamma_2 : [a, b] \to U$ be continuous on $[a, b]$ and differentiable on $(a, b)$, with $\|\gamma_i'(t) - f(t, \gamma_i(t))\| \le \varepsilon_i$ for $i = 1, 2$ and $t \in (a, b)$.
If $\|\gamma_1(a) - \gamma_2(a)\| \le \delta$, then for each $t \in [a, b]$,
$$\|\gamma_1(t) - \gamma_2(t)\| \le G_{\delta, K, \varepsilon_1 + \varepsilon_2}(t - a),$$
where $G$ is the [[Grönwall bound|0FRX8JD7QH]].

## Remarks

A curve with $\|\gamma'(t) - f(t, \gamma(t))\| \le \varepsilon$ is an $\varepsilon$-approximate solution.
For $\varepsilon_1 = \varepsilon_2 = 0$, the result is [[continuous dependence on initial data|0G3DBXRRQJ]].
The proof applies the derivative form of [[Grönwall's inequality|07EJHQYR9A]] with the additional term $\varepsilon_1 + \varepsilon_2$ to $\|\gamma_1 - \gamma_2\|$.

## Explanations

### L1 human

A curve that almost solves the equation stays close to a true solution.
The error has two sources: the difference of initial values and the defects $\varepsilon_i$.
Both can grow at most exponentially in time.
