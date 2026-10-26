---
tag: ~c5cffb2c
kind: definition
name: Lipschitz continuity
aliases: [lipschitz-function]
msc: [26A16]
defines: ~62d723be
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
    locator: Definitions
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$ be a function, and let $K \ge 0$ be real.
The function $f$ is Lipschitz with constant $K$ if
$$|f(x) - f(y)| \le K |x - y| \quad \text{for all } x, y \in D.$$
It is Lipschitz if it is Lipschitz with some constant $K$.

## Remarks

[[Lipschitz functions are uniformly continuous|~74edbbfc]].
A differentiable function on an interval with $|f'| \le K$ is [[Lipschitz with constant $K$|~360e4d86]].
For example, $|x|$ and $\sin x$ are Lipschitz with constant $1$. The function $\sqrt{x}$ on $[0, 1]$ is not Lipschitz.
A Lipschitz map with constant $K < 1$ from a set to itself is a [[contraction|~cc02ff51]]. Mathlib defines it as `LipschitzWith`.

## Explanations

### L1 human

The slope of each chord of the graph of a Lipschitz function is at most $K$ in absolute value.
So the function never changes faster than a fixed rate.
