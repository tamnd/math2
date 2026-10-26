---
tag: 0A3CK6DVVB
kind: definition
name: Uniform continuity on a set
msc: [26A15]
defines: 07RB7B04HX
uses: [0Q4DR37DVE]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Definition of uniform continuity
---

## Definition

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$ be a function, and let $S \subseteq D$.
The function $f$ is uniformly continuous on $S$ if the following holds.
For each $\varepsilon > 0$ there is $\delta > 0$ with $|f(x) - f(y)| < \varepsilon$ for all $x, y \in S$ with $|x - y| < \delta$.

## Remarks

So $f$ is uniformly continuous on $S$ when its restriction to $S$ is [[uniformly continuous|0Q4DR37DVE]].
A function can be uniformly continuous on a set but not on a larger set. For example, $x^2$ is uniformly continuous on $[0, 1]$ but not on $\mathbb{R}$.
Mathlib defines it as `UniformContinuousOn`.

## Explanations

### L1 human

Uniform continuity on $S$ only looks at pairs of points inside $S$.
Points outside $S$ play no role.
