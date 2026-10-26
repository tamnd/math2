---
tag: ~e7cdf5d2
kind: statement
role: proposition
name: Open sets of a metric space
msc: ["54E35"]
uses: [~200ea42b, ~43faf552, ~159c5927, ~2852bf47]
sources:
  - url: https://en.wikipedia.org/wiki/Open_set
    locator: Metric space
---

## Statement

Let $(X, d)$ be a [[metric space|~200ea42b]] and let $U \subseteq X$.
Then $U$ is [[open|~159c5927]] in the [[metric topology|~2852bf47]] if and only if for each $x \in U$ there is a real $\varepsilon > 0$ with $B(x, \varepsilon) \subseteq U$.
Here $B(x, \varepsilon)$ is the [[open ball|~43faf552]] with centre $x$ and radius $\varepsilon$.

## Remarks

The number $\varepsilon$ can depend on $x$.
In $\mathbb{R}$, the set $(0, \infty)$ is open: for $x > 0$, take $\varepsilon = x$.
The set $\mathbb{Q}$ is not open in $\mathbb{R}$, because each ball about a rational number contains an irrational number.

## Explanations

### L1 human

This is the test for open sets that you use in practice.
You pick any point of the set, and you find a small ball about it inside the set.
