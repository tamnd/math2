---
tag: 0E1MMCAY5B
kind: example
name: Euclidean metric
aliases: [euclidean-distance]
msc: [51M05]
instance_of: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_distance
    locator: Higher dimensions
---

## Example

Let $n \ge 1$ be an integer.
For points $x = (x_1, \ldots, x_n)$ and $y = (y_1, \ldots, y_n)$ in $\mathbb{R}^n$, let
$$d_2(x, y) = \sqrt{\sum_{i=1}^{n} (x_i - y_i)^2}.$$
Then $d_2$ is a [[metric|063W5JMY85]] on $\mathbb{R}^n$, the Euclidean metric.

## Remarks

For $n = 1$, $d_2(x, y) = |x - y|$, the [[usual metric on the real line|0KXJTZSW9B]].
For $n = 2$, the formula is the theorem of Pythagoras for the segment from $x$ to $y$.
The triangle inequality for $d_2$ follows from the Cauchy–Schwarz inequality.

## Explanations

### L1 human

The Euclidean metric is the length of the straight segment between two points.
In the plane, the distance from $(0, 0)$ to $(3, 4)$ is $\sqrt{9 + 16} = 5$.
