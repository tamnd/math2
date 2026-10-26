---
tag: 0V4DET59NW
kind: statement
role: theorem
name: Continuous real function on a compact set attains its bounds
aliases: [extreme-value-theorem]
msc: [54C30]
uses: [0K9AAJ8G51, 07PFYV65MB, 0BTMQ04556]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: Generalization to metric and topological spaces
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]], let $K \subseteq X$ be a nonempty [[compact set|00R0X1WGPX]] and let $f \colon X \to \mathbb{R}$ be a [[continuous map|0SY9ECQ19Q]].
Then there are points $a, b \in K$ with $f(a) \le f(x) \le f(b)$ for all $x \in K$.

## Remarks

Proof: the set $f(K)$ is compact in $\mathbb{R}$, because the [[continuous image of a compact set is compact|0K9AAJ8G51]]. By the [[Heine–Borel theorem|07PFYV65MB]], it is closed and bounded. Thus it contains its [[supremum|0BTMQ04556]] and its infimum.
For $K = [a, b]$, this is the extreme value theorem of calculus.
Compactness is needed: $f(x) = x$ on $(0, 1)$ has no maximum, and $f(x) = x$ on $\mathbb{R}$ is not bounded.

## Explanations

### L1 human

A continuous function on a compact set has a largest value and a smallest value, and it reaches them at some points.
On an open interval, the function can come closer and closer to a value without reaching it.
