---
tag: 0WPQYW8MTE
kind: definition
name: Pole
aliases: [pole-of-a-function, simple-pole]
msc: [30D30]
defines: 066E7PJCYE
uses: [0TYB3HM9KE, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
    locator: lead section
---

## Definition

Let $c$ be an [[isolated singularity|0TYB3HM9KE]] of $f$, so that $f$ is holomorphic on $0 < |z - c| < r$ for some $r > 0$.
The singularity $c$ is a pole of $f$ if $|f(z)| \to \infty$ as $z \to c$: for each $K > 0$ there is $\delta > 0$ such that $|f(z)| > K$ for each $z$ with $0 < |z - c| < \delta$.

## Remarks

The point $c$ is a pole of $f$ if and only if $f(z) = \frac{g(z)}{(z - c)^m}$ near $c$, for an integer $m \ge 1$ and a function $g$ that is holomorphic near $c$ with $g(c) \neq 0$. The integer $m$ is the [[order of the pole|0YK27TJ4WF]].
Equivalently, $1/f$ extends to a holomorphic function near $c$ with a [[zero|0CEGEASY49]] at $c$.
For example, $\frac{1}{z^2 (z - 1)}$ has a pole of order $2$ at $0$ and a pole of order $1$, a simple pole, at $1$.

## Explanations

### L1 human

A pole is a point where the function goes to infinity, in the way $1/z$ or $1/z^3$ does at $0$.
Near a pole, $1/f$ is a holomorphic function with a zero there.
