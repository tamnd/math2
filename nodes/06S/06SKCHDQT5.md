---
tag: 06SKCHDQT5
kind: definition
name: Continuously differentiable function
aliases: [c1-function, ck-function]
msc: [26A24]
defines: 0VW90BBSJ4
uses: [0A61B60B5R, 0P27W9RW0G, 084NGSTWM7]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothness
    locator: Differentiability classes
inventory: [KQZ8H9DM9F]
---

## Definition

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$.
The function $f$ is continuously differentiable, or of class $C^1$, if $f$ is [[differentiable|0A61B60B5R]] on $I$ and $f'$ is [[continuous|0P27W9RW0G]] on $I$.
More generally, for $k \ge 1$, $f$ is of class $C^k$ if its [[higher derivative|084NGSTWM7]] $f^{(k)}$ exists and is continuous on $I$.
The class $C^0$ consists of the continuous functions.

## Remarks

Each $C^{k+1}$ function is $C^k$.
A differentiable function need not be $C^1$. See [[x^2 sin(1/x)|0WDAKKN4NC]].
The function $x |x|$ is $C^1$ but not twice differentiable at $0$.
Mathlib defines the class as `ContDiff ℝ k f`.

## Explanations

### L1 human

A $C^1$ function has a slope at each point, and the slope changes without jumps.
The class $C^k$ asks the same of the first $k$ derivatives.
