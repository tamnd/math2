---
tag: 0VTAXQEWQD
kind: example
name: Sup metric on R^n
aliases: [chebyshev-distance, maximum-metric]
msc: ["54E35"]
instance_of: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_distance
    locator: Definition
same_as:
  wikidata: Q573482
  wikipedia: Chebyshev distance
---

## Example

Let $n \ge 1$ be an integer.
For $x = (x_1, \ldots, x_n)$ and $y = (y_1, \ldots, y_n)$ in $\mathbb{R}^n$, let
$$d_\infty(x, y) = \max_{1 \le i \le n} |x_i - y_i|.$$
Then $d_\infty$ is a [[metric|063W5JMY85]] on $\mathbb{R}^n$, the sup metric.

## Remarks

It is also called the Chebyshev distance or the maximum metric.
For all $x, y$ in $\mathbb{R}^n$, $d_\infty(x, y) \le d_2(x, y) \le d_1(x, y) \le n \, d_\infty(x, y)$, where $d_2$ is the [[Euclidean metric|0E1MMCAY5B]] and $d_1$ is the [[taxicab metric|07CJNE6ZAQ]].
It is the limit of the [[p-metric|0TFDZN6AXP]] $d_p$ as $p \to \infty$.

## Explanations

### L1 human

The sup metric takes only the largest difference of the coordinates.
On a chessboard, it is the number of moves that a king needs to go from one square to another.
