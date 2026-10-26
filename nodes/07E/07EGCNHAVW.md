---
tag: 07EGCNHAVW
kind: definition
name: Limit point of a set
aliases: [accumulation-point, cluster-point-of-a-set]
msc: [26A03]
defines: 0E3X7TXS67
sources:
  - url: https://en.wikipedia.org/wiki/Accumulation_point
    locator: Accumulation points of a set
---

## Definition

Let $S$ be a subset of $\mathbb{R}$ and let $a$ be a real number.
The point $a$ is a limit point of $S$ if for each $\delta > 0$ there is $x \in S$ with $0 < |x - a| < \delta$.

## Remarks

A limit point of $S$ need not belong to $S$. For example, $0$ is a limit point of $\{1/n : n \ge 1\}$.
Each point of an interval with more than one point is a limit point of the interval. So are its endpoints.
Limit points of the domain are the points where the [[limit of a function|0TXTSEMHR5]] makes sense.
Mathlib uses the general form `AccPt`.

## Explanations

### L1 human

A limit point of $S$ is a point that we can approach by other points of $S$.
Points of $S$ lie as close to it as we like, not counting the point itself.
