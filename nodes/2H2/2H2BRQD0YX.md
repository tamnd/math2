---
tag: 2H2BRQD0YX
kind: definition
name: Chain recurrence
msc: [37B20, 37B35]
defines: 6MX5R482KJ
uses: [0VKD1TP7F3, 0VGFHTM75Y, EY2W34JZA4]
sources:
  - url: https://en.wikipedia.org/wiki/Conley%27s_fundamental_theorem_of_dynamical_systems
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
For $\varepsilon > 0$ and $x, y \in X$, an *$\varepsilon$-chain* from $x$ to $y$ is a finite sequence $x = x_0, x_1, \ldots, x_n = y$ with $n \ge 1$ and $d(f(x_{i-1}), x_i) < \varepsilon$ for $i = 1, \ldots, n$.
A point $x \in X$ is *chain recurrent* if for every $\varepsilon > 0$ there is an $\varepsilon$-chain from $x$ to $x$.
The *chain recurrent set* $\mathcal{R}(f)$ is the set of chain recurrent points.

## Remarks

For a continuous flow $\varphi_t$, an $(\varepsilon, T)$-chain from $x$ to $y$ is a sequence $x = x_0, \ldots, x_n = y$ with times $t_1, \ldots, t_n \ge T$.
It must satisfy $d(\varphi_{t_i}(x_{i-1}), x_i) < \varepsilon$ for each $i$.
A point $x$ is chain recurrent for the flow if such chains from $x$ to $x$ exist for all $\varepsilon > 0$ and $T > 0$.
The set $\mathcal{R}(f)$ is closed and contains the [[non-wandering set|EY2W34JZA4]] $\Omega(f)$.
Example: for the identity map, $x_0 = x_1 = x$ is an $\varepsilon$-chain from $x$ to $x$ for every $\varepsilon$, so every point is chain recurrent.
Non-example: let $f(x) = x/2$ on $[0, 1]$ and $x > 0$, $0 < \varepsilon < x/2$.
If $x_{i-1} \le x$, then $x_i < x_{i-1}/2 + \varepsilon < x$, so by induction every $x_i$ with $i \ge 1$ is less than $x$; no $\varepsilon$-chain returns to $x$.
For this map $\mathcal{R}(f) = \set{0}$.

## Explanations

### L1 human

An $\varepsilon$-chain is an orbit with small errors allowed at each step.
A point is chain recurrent if it can come back to itself along such chains, for every size of error.
