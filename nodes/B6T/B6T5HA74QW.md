---
tag: B6T5HA74QW
kind: concept
name: Line search
msc: [90C30, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Line_search
same_as:
  wikidata: Q3278015
  wikipedia: Line search
---

## Summary

A line search is a step of an optimization method.
Given a current point and a descent direction, it chooses how far to move along that direction.
It reduces a problem in many variables to a problem in one variable, the step length.
Exact line searches minimize the function along the ray; practical ones accept any step that satisfies conditions such as the Armijo or Wolfe conditions.
Line searches make methods like [[Newton's method in optimization|TNQZVR6TFN]] and quasi-Newton methods converge from distant starting points.

## Explanations

### L1 human

Imagine standing on a hillside in fog, knowing only which way is downhill.
You choose a direction, then decide how many steps to take before looking again.
Too short wastes effort; too long may take you past the valley floor and uphill again.
For $f(x, y) = x^2 + 10 y^2$ at $(1, 1)$, the downhill direction $(-2, -20)$ is steep in $y$, and a full step $(-1, -19)$ overshoots badly, so the step must be shortened.
