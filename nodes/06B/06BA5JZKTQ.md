---
tag: 06BA5JZKTQ
kind: definition
name: Strictly convex function
msc: [26A51]
defines: 0AEAHMFSCA
uses: [0VV0HSW1ZS]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
    locator: Definition
---

## Definition

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be a function.
The function $f$ is strictly convex if
$$f(t x + (1 - t) y) < t f(x) + (1 - t) f(y)$$
for all $x, y \in I$ with $x \ne y$ and all $t \in (0, 1)$.

## Remarks

Each strictly convex function is [[convex|0VV0HSW1ZS]]. A linear function is convex but not strictly convex.
A strictly convex function has at most one minimum point.
For example, $x^2$ and $e^x$ are strictly convex. Mathlib defines strict convexity as `StrictConvexOn`.

## Explanations

### L1 human

A strictly convex function bends upward everywhere, with no straight pieces in its graph.
The chords lie strictly above the graph, except at their ends.
