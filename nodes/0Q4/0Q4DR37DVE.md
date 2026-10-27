---
tag: 0Q4DR37DVE
kind: definition
name: Uniform continuity
msc: [26A15]
defines: 0M4JJT780X
uses: [0W8YHHGCJG]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Definition of uniform continuity
inventory: [7ZJYA8EKE9]
---

## Definition

Let $D \subseteq \mathbb{R}$ and let $f \colon D \to \mathbb{R}$ be a function.
The function $f$ is uniformly continuous if the following holds.
For each $\varepsilon > 0$ there is $\delta > 0$ with $|f(x) - f(y)| < \varepsilon$ for all $x, y \in D$ with $|x - y| < \delta$.

## Remarks

Each uniformly continuous function is continuous. In the [[epsilon-delta form|0W8YHHGCJG]] of continuity, $\delta$ may depend on the point. Here one $\delta$ works for all points.
The function $x^2$ is continuous on $\mathbb{R}$ but [[not uniformly continuous|0A8JXHYTJC]].
Mathlib defines it for uniform spaces, as `UniformContinuous`.
Eduard Heine published the first definition of uniform continuity, in 1870.

## Explanations

### L1 human

For a uniformly continuous function, one input tolerance works everywhere in the domain.
The graph has no places where it becomes steeper and steeper without bound.
