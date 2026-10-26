---
tag: 026FDZFRXS
kind: statement
role: proposition
name: Uniformly continuous functions map Cauchy sequences to Cauchy sequences
msc: [26A15]
uses: [0Q4DR37DVE, 0QZMTN5AXX]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_continuity
    locator: Properties
---

## Statement

Let $D \subseteq \mathbb{R}$ and let $f \colon D \to \mathbb{R}$ be [[uniformly continuous|0Q4DR37DVE]].
Let $(x_n)$ be a [[Cauchy sequence|0QZMTN5AXX]] in $D$.
Then $(f(x_n))$ is a Cauchy sequence.

## Remarks

Given $\varepsilon > 0$, take $\delta$ from uniform continuity, and then $N$ with $|x_m - x_n| < \delta$ for $m, n \ge N$.
Continuity alone is not enough. The function $1/x$ on $(0, 1)$ maps the Cauchy sequence $1/n$ to the sequence $n$.
Mathlib states it as `UniformContinuous.comp_cauchySeq`.

## Explanations

### L1 human

Points of a Cauchy sequence crowd closer and closer together.
A uniformly continuous function keeps their images crowding together too.
