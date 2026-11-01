---
tag: N4QZS912MT
kind: statement
role: theorem
name: Minkowski inequality
msc: [26D15, "46E30", 28A25]
uses: [JQ9WXC729D]
about: [08NYZ2FS6B]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_inequality
same_as:
  wikidata: Q755092
  wikipedia: Minkowski inequality
---

## Statement

Let $(S, \Sigma, \mu)$ be a measure space and let $p \in [1, \infty)$.
Let $f, g \colon S \to \R$ be measurable functions with $\int_S \abs{f}^p \, d\mu < \infty$ and $\int_S \abs{g}^p \, d\mu < \infty$.
Then
$$\Big( \int_S \abs{f + g}^p \, d\mu \Big)^{1/p} \le \Big( \int_S \abs{f}^p \, d\mu \Big)^{1/p} + \Big( \int_S \abs{g}^p \, d\mu \Big)^{1/p}.$$

## Remarks

Proof idea: the case $p = 1$ follows from $\abs{f + g} \le \abs{f} + \abs{g}$.
For $p > 1$, first $\abs{f + g}^p \le 2^{p-1}(\abs{f}^p + \abs{g}^p)$ shows that the left side is finite.
Then write $\abs{f + g}^p \le \abs{f} \abs{f + g}^{p-1} + \abs{g} \abs{f + g}^{p-1}$ and apply [[Hölder's inequality|JQ9WXC729D]] to each term with $q = p / (p - 1)$.

With the counting measure on $\set{1, \dots, n}$ it shows that the [[p-norm on R^n|0KNJWEVSMG]] satisfies the triangle inequality.
In general it is the triangle inequality for the [[norm|08NYZ2FS6B]] of the Lp space $L^p(\mu)$.

The hypothesis $p \ge 1$ is needed.
For $p = 1/2$ on $\R^2$ with the counting measure, take $f = (1, 0)$ and $g = (0, 1)$: the left side is $(1 + 1)^2 = 4$ and the right side is $1 + 1 = 2$.

## Explanations

### L1 human

The Minkowski inequality is the triangle inequality for the $p$-size of functions or vectors.
The size of a sum is at most the sum of the sizes.
For $p = 2$ and vectors in the plane, it says that one side of a triangle is at most the sum of the other two.

### L2 human

This inequality is what makes $\norm{f}_p = (\int \abs{f}^p \, d\mu)^{1/p}$ a norm for $p \ge 1$, so that $L^p$ is a normed space.
Its proof is a short application of Hölder's inequality.
For $0 < p < 1$ the inequality fails, and the quantity $\norm{f}_p$ is then not a norm.
