---
tag: 0HBQC2GJXT
kind: definition
name: Limit point
msc: [54A05]
defines: 0E3X7TXS67
uses: [0CNQXVBHCX, 01ZQQDCERP]
sources:
  - url: https://en.wikipedia.org/wiki/Accumulation_point
    locator: Definition
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]], let $S \subseteq X$ and let $x \in X$.
The point $x$ is a limit point of $S$ when each [[open set|01ZQQDCERP]] $U$ with $x \in U$ contains a point of $S$ other than $x$.

## Remarks

The point $x$ need not be in $S$. In $\mathbb{R}$, the point $0$ is a limit point of $\{1/n : n \ge 1\}$.
In a metric space, $x$ is a limit point of $S$ if and only if each ball $B(x, \varepsilon)$ contains a point of $S \setminus \{x\}$.
The [[closure|0DRKT1QJR7]] of $S$ is the union of $S$ and the set of its limit points.
A point of $S$ that is not a limit point of $S$ is an [[isolated point|01PKQYTTMT]] of $S$.

## Explanations

### L1 human

A limit point is a point that other points of the set crowd around.
For the set $\{1, 1/2, 1/3, \ldots\}$, the points crowd around $0$, so $0$ is a limit point, but $1$ is not.
