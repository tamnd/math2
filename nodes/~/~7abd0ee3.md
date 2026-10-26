---
tag: ~7abd0ee3
kind: definition
name: Isolated singularity
aliases: [isolated-singular-point]
msc: [30D30]
defines: ~a6d06502
uses: [~1a187203]
sources:
  - url: https://en.wikipedia.org/wiki/Isolated_singularity
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Isolated_singularity
    locator: Examples
---

## Definition

Let $c \in \mathbb{C}$ and let $f$ be a complex function.
The point $c$ is an isolated singularity of $f$ if there is $r > 0$ such that $f$ is defined and [[holomorphic|~1a187203]] on the punctured disc $\{z : 0 < |z - c| < r\}$.
The value of $f$ at $c$, if there is one, plays no role.

## Remarks

Each isolated singularity is of exactly one of three types: [[removable|~88345558]], a [[pole|~28935b89]], or [[essential|~75d899a4]].
For example, $0$ is an isolated singularity of $1/z$, of $\frac{\sin z}{z}$ and of $e^{1/z}$.
The point $0$ is not an isolated singularity of $\frac{1}{\sin(1/z)}$, because the poles $\frac{1}{k\pi}$ accumulate at $0$. It is not an isolated singularity of $\operatorname{Log} z$ either, because $\operatorname{Log}$ is not holomorphic on any punctured disc around $0$.

## Explanations

### L1 human

An isolated singularity is a single bad point of a function, with only good points around it.
The function is holomorphic on a small disc around the point, with only the center removed.
