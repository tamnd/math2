---
tag: 0R7BTEWCJ2
kind: statement
role: proposition
name: Compact subsets of a metric space are bounded
msc: ["54E45"]
uses: [0P6PMJB4MA, 0P953MG05E, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_space
    locator: Metric spaces
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]] and let $K$ be a [[compact subset|00R0X1WGPX]] of $X$.
Then $K$ is [[bounded|0P953MG05E]].

## Remarks

Proof: if $K$ is empty, it is bounded. Otherwise fix $x \in K$. The [[open balls|0DC3MPR7C9]] $B(x, n)$ for $n \ge 1$ cover $K$, so finitely many of them do. The largest of these balls contains $K$.
A compact subset of a metric space is also [[closed|0G5AV9Q4RR]], because metric spaces are Hausdorff.
The converse fails in general: a closed bounded set need not be compact. With the metric $\min(|x - y|, 1)$, the real line is closed and bounded, but not compact.

## Explanations

### L1 human

A compact set can be covered by finitely many balls about one point, and then it fits in the largest of them.
