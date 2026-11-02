---
tag: 4XGQD57EWF
kind: definition
name: Nonexpansive map
msc: [47H09, "54E40"]
defines: VF6CA0VE41
uses: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Metric_map
---

## Definition

Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|0VKD1TP7F3]].
A map $f \colon X \to Y$ is *nonexpansive* if
$$d_Y(f(x), f(x')) \le d_X(x, x') \quad \text{for all } x, x' \in X.$$

## Remarks

Equivalently, $f$ is [[Lipschitz|0AW1E6YTJY]] with Lipschitz constant at most $1$.
In operator theory, $X = Y = C$ is often a subset of a Banach space with the norm distance, and the condition reads $\norm{f(x) - f(x')} \le \norm{x - x'}$.

Example: let $H$ be a real Hilbert space, $C \subseteq H$ a nonempty closed convex set, and $P_C(x)$ the nearest point of $C$ to $x$.
The variational inequality $\ip{x - P_C x}{c - P_C x} \le 0$ for $c \in C$ gives $\norm{P_C x - P_C y}^2 \le \ip{x - y}{P_C x - P_C y} \le \norm{x - y}\norm{P_C x - P_C y}$, so $P_C$ is nonexpansive.

Non-example: $f(x) = 2x$ on $\R$ gives $\abs{f(1) - f(0)} = 2 > 1 = \abs{1 - 0}$.

Every [[contraction mapping|0QN69YA357]] is nonexpansive, but not conversely.
The Browder–Göhde–Kirk theorem gives fixed points: a nonexpansive map of a nonempty bounded closed convex subset of a uniformly convex Banach space into itself has a fixed point.
