---
tag: FWKSHEJ9RP
kind: statement
role: theorem
name: Karamata's inequality
msc: [26D15, 26A51]
uses: [0TK8Y3J5RW, 0VV0HSW1ZS, 5K7VT2VKZT]
about: [07Q7CNM5WF, 5K7VT2VKZT]
sources:
  - url: https://en.wikipedia.org/wiki/Karamata%27s_inequality
same_as:
  wikidata: Q3656857
  wikipedia: Karamata's inequality
---

## Statement

Let $I$ be an [[interval|0TK8Y3J5RW]] of $\R$ and let $f \colon I \to \R$ be a [[convex function|0VV0HSW1ZS]].
Let $x_1 \ge x_2 \ge \dots \ge x_n$ and $y_1 \ge y_2 \ge \dots \ge y_n$ be numbers in $I$ such that $(x_1, \dots, x_n)$ [[majorizes|5K7VT2VKZT]] $(y_1, \dots, y_n)$, that is,
$$\sum_{i=1}^{k} x_i \ge \sum_{i=1}^{k} y_i \quad \text{for } k = 1, \dots, n - 1, \qquad \sum_{i=1}^{n} x_i = \sum_{i=1}^{n} y_i.$$
Then
$$\sum_{i=1}^{n} f(x_i) \ge \sum_{i=1}^{n} f(y_i).$$

## Remarks

Proof idea: let $c_i$ be the slope of the chord of $f$ between $x_i$ and $y_i$, or a [[subderivative|9C5WXYYQEK]] at $x_i$ when $x_i = y_i$.
Since [[the slopes of a convex function increase|0BY5FTHEEE]] and both sequences decrease, $c_1 \ge c_2 \ge \dots \ge c_n$.
Then $\sum_i \big(f(x_i) - f(y_i)\big) = \sum_i c_i (x_i - y_i)$, and summation by parts writes this as a sum of products of the nonnegative numbers $c_k - c_{k+1}$ with the nonnegative partial sums $\sum_{i \le k} (x_i - y_i)$.

Example: $(2, 0)$ majorizes $(1, 1)$, so $f(2) + f(0) \ge 2 f(1)$, which is midpoint convexity.
More generally $(x_1, \dots, x_n)$ majorizes the constant vector $(\bar x, \dots, \bar x)$ with $\bar x$ the mean, which gives [[Jensen's inequality|0RWMRTPC87]] with equal weights.

The equality of the total sums is needed.
With $n = 1$, $f(x) = -x$, $x_1 = 1$ and $y_1 = 0$, one has $x_1 \ge y_1$ but $f(x_1) = -1 < 0 = f(y_1)$.

## Explanations

### L1 human

Karamata's inequality compares two lists of numbers with the same total.
If one list is more spread out than the other, then summing a convex function over it gives a larger result.
A convex function rewards spreading out, because its graph bends upward.

### L2 human

The inequality says that $x \mapsto \sum_i f(x_i)$ is a [[Schur-convex function|A72XTVF2GK]] whenever $f$ is convex.
It contains Jensen's inequality with equal weights and implies many symmetric inequalities, for instance by comparing a vector with a less spread out one.
A converse also holds: if the conclusion is true for every convex $f$, then $x$ majorizes $y$.
