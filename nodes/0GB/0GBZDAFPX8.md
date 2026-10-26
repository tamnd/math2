---
tag: 0GBZDAFPX8
kind: statement
role: proposition
name: Epsilon-delta definition of a limit
msc: [26A03]
uses: [0TXTSEMHR5]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: (ε, δ)-definition of limit
---

## Statement

Let $D \subseteq \mathbb{R}$, let $f \colon D \to \mathbb{R}$, let $a$ be a limit point of $D$, and let $L$ be a real number.
Then $\lim_{x \to a} f(x) = L$ if and only if the following holds.
For each $\varepsilon > 0$ there is $\delta > 0$ such that $|f(x) - L| < \varepsilon$ for all $x \in D$ with $0 < |x - a| < \delta$.

## Remarks

Each open interval around a point contains an interval $(L - \varepsilon, L + \varepsilon)$, and each such interval is open. This gives the equivalence with the [[definition|0TXTSEMHR5]].
Many texts take this condition as the definition of the limit.
Mathlib states a form for metric spaces as `Metric.tendsto_nhds_nhds`.

## Explanations

### L1 human

For each error tolerance $\varepsilon$, we can force $f(x)$ within $\varepsilon$ of $L$.
We do this by taking $x$ within a suitable distance $\delta$ of $a$.
