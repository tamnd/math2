---
tag: 0W8YHHGCJG
kind: statement
role: proposition
name: Epsilon-delta definition of continuity
msc: [26A15]
uses: [0EEE2CZB2A]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous_function
    locator: Weierstrass and Jordan definitions (epsilon–delta) of continuous functions
---

## Statement

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, and let $a \in D$.
Then $f$ is [[continuous at|0EEE2CZB2A]] $a$ if and only if the following holds.
For each $\varepsilon > 0$ there is $\delta > 0$ with $|f(x) - f(a)| < \varepsilon$ for all $x \in D$ with $|x - a| < \delta$.

## Remarks

Each open interval around a point contains an interval of the form $(c - r, c + r)$ with $r > 0$. This gives the equivalence.
Many texts take this condition as the definition of continuity.
Mathlib states a form for metric spaces as `Metric.continuousAt_iff`.

## Explanations

### L1 human

For each allowed error $\varepsilon$ in the output, there is a tolerance $\delta$ in the input.
Inputs within $\delta$ of $a$ give outputs within $\varepsilon$ of $f(a)$.
