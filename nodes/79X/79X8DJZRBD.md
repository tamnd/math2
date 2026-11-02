---
tag: 79X8DJZRBD
kind: definition
name: Space of functions vanishing at infinity
msc: ["46E15", 54C35, 46B25]
defines: N59BW1QFD1
uses: [0FE2SB8WVJ, 0S1FJ8VEX9, 0TVJZYB6SH, 0X3WGX95FE, MG3X8Y1VT4]
sources:
  - url: https://en.wikipedia.org/wiki/Vanish_at_infinity
---

## Definition

Let $X$ be a [[locally compact|0FE2SB8WVJ]] [[Hausdorff space|0S1FJ8VEX9]] and let $\mathbb{K}$ be $\R$ or $\C$.
A [[continuous function|0X3WGX95FE]] $f \colon X \to \mathbb{K}$ *vanishes at infinity* if, for every $\varepsilon > 0$, the set $\set{x \in X : \abs{f(x)} \ge \varepsilon}$ is [[compact|0TVJZYB6SH]].
The *space of functions vanishing at infinity* $C_0(X)$ is the set of these functions, with pointwise operations and the norm $\norm{f}_\infty = \sup_{x \in X} \abs{f(x)}$.

## Remarks

Example: $f(x) = e^{-x^2}$ on $\R$.
For $0 < \varepsilon \le 1$, the set $\set{\abs{f} \ge \varepsilon}$ is the closed bounded interval $\abs{x} \le \sqrt{\log(1/\varepsilon)}$, which is compact.
For $\varepsilon > 1$ it is empty.

Non-example: the constant function $1$ on $\R$.
For $\varepsilon = 1/2$, the set $\set{\abs{f} \ge 1/2}$ is all of $\R$, which is not compact.

Each $f \in C_0(X)$ is bounded: $\abs{f} < 1$ off the compact set $\set{\abs{f} \ge 1}$, and $\abs{f}$ attains a maximum on that set if it is nonempty.
So $C_0(X)$ is a subspace of the [[space of bounded continuous functions|MG3X8Y1VT4]], and it is closed there, so it is a Banach space.
If $X$ is compact, then $C_0(X) = C(X)$.
For $X = \N$ with the discrete topology, $C_0(\N)$ is the sequence space $c_0$.
The compactly supported continuous functions are dense in $C_0(X)$.
