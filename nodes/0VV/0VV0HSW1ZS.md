---
tag: 0VV0HSW1ZS
kind: definition
name: Convex function
msc: [26A51]
defines: 07Q7CNM5WF
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
    locator: Definition
---

## Definition

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be a function.
The function $f$ is convex if
$$f(t x + (1 - t) y) \le t f(x) + (1 - t) f(y)$$
for all $x, y \in I$ and all $t \in [0, 1]$.

## Remarks

Geometrically, each chord of the graph lies on or above the graph.
For example, $x^2$, $|x|$, and $e^x$ are convex on $\mathbb{R}$. Linear functions are convex.
A twice differentiable function with [[$f'' \ge 0$ is convex|0Z41C17TGP]].
Mathlib defines convexity on a set as `ConvexOn`.

## Explanations

### L1 human

A convex function bends upward, like a bowl.
The straight segment between two points of the graph never goes below the graph.
