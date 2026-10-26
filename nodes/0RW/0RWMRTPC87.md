---
tag: 0RWMRTPC87
kind: statement
role: theorem
name: Jensen's inequality
msc: [26D15]
uses: [0VV0HSW1ZS]
sources:
  - url: https://en.wikipedia.org/wiki/Jensen%27s_inequality
    locator: Finite form
same_as:
  wikidata: Q518131
  wikipedia: Jensen's inequality
---

## Statement

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be [[convex|0VV0HSW1ZS]].
Let $x_1, \dots, x_n \in I$, and let $w_1, \dots, w_n \ge 0$ with $w_1 + \cdots + w_n = 1$.
Then
$$f\Big( \sum_{i=1}^{n} w_i x_i \Big) \le \sum_{i=1}^{n} w_i f(x_i).$$

## Remarks

The case $n = 2$ is the definition of convexity. Induction on $n$ gives the general case.
For a concave function, the inequality is reversed. With $f = \ln$ this gives the [[AM–GM inequality|0DRF0F3XC9]].
Mathlib states it as `ConvexOn.map_sum_le`.

## History

Johan Jensen proved the inequality in 1906.

## Explanations

### L1 human

The value of a convex function at an average is at most the average of its values.
The weights $w_i$ say how much each point counts in the average.
