---
tag: ~f6a5aaba
kind: definition
name: Bounded set
msc: ["54E35"]
defines: ~54b3af6b
uses: [~200ea42b, ~ec6373a9]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_set
    locator: Definition in a metric space
---

## Definition

Let $(X, d)$ be a [[metric space|~200ea42b]] and let $S \subseteq X$.
The set $S$ is bounded when there is a real number $M$ such that $d(x, y) \le M$ for all $x, y \in S$.

## Remarks

The empty set and each finite set are bounded.
If $X$ is not empty, then $S$ is bounded if and only if $S$ lies in some [[closed ball|~ec6373a9]] $\bar{B}(x, r)$ with $x \in X$ and $r \ge 0$.
In $\mathbb{R}$ with the usual metric, $S$ is bounded in this sense if and only if $S$ is bounded above and bounded below.
Boundedness depends on the metric: $\mathbb{R}$ is not bounded for $|x - y|$, but it is bounded for $\min(|x - y|, 1)$.

## Explanations

### L1 human

A set is bounded when you can put all of it inside one large ball.
For example, the interval $(0, 1)$ is bounded, but the set $\mathbb{N}$ of natural numbers is not bounded in $\mathbb{R}$.
