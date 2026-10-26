---
tag: ~5bb8bca4
kind: definition
name: Local maximum
aliases: [relative-maximum]
msc: [26A24]
defines: ~4b285a2f
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_and_minimum
    locator: Definition
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, and let $a \in D$.
The function $f$ has a local maximum at $a$ if there is $\delta > 0$ with $f(x) \le f(a)$ for all $x \in D$ with $|x - a| < \delta$.
It is a strict local maximum if $f(x) < f(a)$ for all such $x \ne a$.

## Remarks

A global maximum, where $f(x) \le f(a)$ for all $x \in D$, is also a local maximum.
A [[local minimum|~3ed4ce3a]] is defined with $f(x) \ge f(a)$. Local maxima and minima are local extrema.
At an interior local extremum, a differentiable function has [[derivative zero|~f405b82b]].
Mathlib defines it as `IsLocalMax`.

## Explanations

### L1 human

A local maximum is a hilltop of the graph.
Nearby values are not higher, although values far away may be higher.
