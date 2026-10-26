---
tag: 02EEX96DFS
kind: statement
role: proposition
name: Open balls form a basis of the metric topology
msc: ["54E35"]
uses: [06EX0FHBTF, 0A6YRNZB2R, 0B2305GNAZ, 0DC3MPR7C9]
sources:
  - url: https://en.wikipedia.org/wiki/Base_(topology)
    locator: Examples
---

## Statement

Let $(X, d)$ be a [[metric space|063W5JMY85]].
Then the set of all [[open balls|0DC3MPR7C9]] $B(x, r)$, with $x \in X$ and real $r > 0$, is a [[basis|06EX0FHBTF]] of the [[metric topology|0A6YRNZB2R]] of $X$.
Also, the balls $B(x, 1/n)$ with $x \in X$ and integer $n \ge 1$ form a basis.

## Remarks

Proof: each ball is open, by [[open balls are open|0B2305GNAZ]]. If $U$ is open and $x \in U$, then some ball $B(x, r)$ lies in $U$, and $B(x, 1/n) \subseteq B(x, r)$ for $n > 1/r$.
For each point $x$, the balls $B(x, 1/n)$ form a countable neighbourhood basis at $x$. Thus each metric space is [[first-countable|0HG11FW8MJ]].
In $\mathbb{R}$, the open balls are the bounded open intervals.

## Explanations

### L1 human

Each open set of a metric space is a union of open balls.
So, to check a property for all open sets, it is often enough to check it for balls.
