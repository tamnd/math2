---
tag: 011HV2GAWF
kind: statement
role: theorem
name: A convex function on an open interval is continuous
msc: [26A51]
uses: [0BY5FTHEEE, 0P27W9RW0G]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
    locator: Functions of one variable
---

## Statement

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$ be convex.
Then $f$ is [[continuous|0P27W9RW0G]] on $I$.

## Remarks

Fix $y \in I$ and points $x < y < z$ in $I$. By the [[slope inequalities|0BY5FTHEEE]], the slopes of chords from $y$ are bounded for points near $y$. So $|f(w) - f(y)| \le C |w - y|$ near $y$.
On a closed interval this fails. The function on $[0, 1]$ with $f(0) = 1$ and $f(x) = 0$ for $x > 0$ is convex but not continuous at $0$.
A convex function on an open interval has one-sided derivatives at every point. Mathlib states continuity as `ConvexOn.continuousOn`, for open sets.

## Explanations

### L1 human

A convex function cannot jump inside an open interval.
A jump would break the condition that the chords lie above the graph.
