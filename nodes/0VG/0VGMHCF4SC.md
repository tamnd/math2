---
tag: 0VGMHCF4SC
kind: statement
role: proposition
name: Product of continuous functions is continuous
msc: [26A15]
uses: [0P27W9RW0G, 0734RSVF2V, 0PAQM3H57X]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Rules for continuity
---

## Statement

Let $D \subseteq \mathbb{R}$ and let $f, g \colon D \to \mathbb{R}$ be [[continuous|0P27W9RW0G]] functions.
Then the sum $f + g$ and the product $f g$, given by $(f g)(x) = f(x) g(x)$, are continuous.

## Remarks

The proof uses [[sequential continuity|0PAQM3H57X]] and the [[product rule for limits|0734RSVF2V]] of sequences.
In particular, $c f$ is continuous for each constant $c$.
Mathlib states it for topological monoids, as `Continuous.mul`.

## Explanations

### L1 human

If $f(x)$ and $g(x)$ change only a little when $x$ changes a little, so does $f(x) g(x)$.
