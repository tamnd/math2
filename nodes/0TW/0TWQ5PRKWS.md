---
tag: 0TWQ5PRKWS
kind: definition
name: Equivalent metrics
aliases: [topologically-equivalent-metrics]
msc: ["54E35"]
defines: 09V3NASXND
uses: [063W5JMY85, 01ZQQDCERP, 0A6YRNZB2R]
sources:
  - url: https://en.wikipedia.org/wiki/Equivalence_of_metrics
    locator: Topological equivalence
  - url: https://en.wikipedia.org/wiki/Equivalence_of_metrics
    locator: Strong equivalence
---

## Definition

Let $X$ be a set and let $d_1$ and $d_2$ be metrics on $X$.
The metrics $d_1$ and $d_2$ are equivalent when they have the same [[open sets|01ZQQDCERP]], that is, when they give the same [[metric topology|0A6YRNZB2R]] on $X$.
The metrics are strongly equivalent when there are real numbers $a > 0$ and $b > 0$ with
$$a \, d_1(x, y) \le d_2(x, y) \le b \, d_1(x, y) \quad \text{for all } x, y \in X.$$

## Remarks

Strongly equivalent metrics are equivalent: each ball for one metric contains a ball with the same centre for the other metric.
On $\mathbb{R}^n$, the [[taxicab metric|07CJNE6ZAQ]], the [[Euclidean metric|0E1MMCAY5B]] and the [[sup metric|0VTAXQEWQD]] are strongly equivalent.
On $\mathbb{R}$, the metrics $|x - y|$ and $\min(|x - y|, 1)$ are equivalent but not strongly equivalent, because only the second one is bounded.
Equivalent metrics have the same convergent sequences and the same continuous maps. Completeness can change: see the Remarks of [[complete metric space|08EWT7J0SC]].

## Explanations

### L1 human

Equivalent metrics can give different numbers for distances, but they agree on which points are near each other.
For example, on the plane, the taxicab distance is never more than $\sqrt{2}$ times the straight distance, and never less than it.
