---
tag: ~74edbbfc
kind: statement
role: proposition
name: Lipschitz functions are uniformly continuous
msc: [26A16]
uses: [~c5cffb2c, ~746bfcb1]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
    locator: Properties
---

## Statement

Let $D \subseteq \mathbb{R}$ and let $f \colon D \to \mathbb{R}$ be [[Lipschitz|~c5cffb2c]].
Then $f$ is [[uniformly continuous|~746bfcb1]].

## Remarks

Let $K > 0$ be a Lipschitz constant. Given $\varepsilon > 0$, take $\delta = \varepsilon / K$.
The converse fails. The function $\sqrt{x}$ is uniformly continuous on $[0, 1]$ but not Lipschitz.
Mathlib states it as `LipschitzWith.uniformContinuous`.

## Explanations

### L1 human

A Lipschitz bound controls the change of $f$ in the same way at every point.
So one input tolerance works for the whole domain.
