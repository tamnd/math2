---
tag: 0EF2VG8XKQ
kind: definition
name: Concave function
msc: [26A51]
defines: 0GCM7B6PBK
uses: [0VV0HSW1ZS]
sources:
  - url: https://en.wikipedia.org/wiki/Concave_function
    locator: Definition
inventory: [GVHNVWFQKX]
---

## Definition

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be a function.
The function $f$ is concave if
$$f(t x + (1 - t) y) \ge t f(x) + (1 - t) f(y)$$
for all $x, y \in I$ and all $t \in [0, 1]$.

## Remarks

So $f$ is concave exactly when $-f$ is [[convex|0VV0HSW1ZS]].
For example, $\sqrt{x}$ and $\ln x$ are concave on $(0, \infty)$.
Mathlib defines concavity on a set as `ConcaveOn`.

## Explanations

### L1 human

A concave function bends downward, like a dome.
Each chord of the graph lies on or below the graph.
