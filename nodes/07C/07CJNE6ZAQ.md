---
tag: 07CJNE6ZAQ
kind: example
name: Taxicab metric
aliases: [manhattan-metric, l1-metric]
msc: [51F99]
instance_of: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Taxicab_geometry
    locator: Formal definition
same_as:
  wikidata: Q573509
  wikipedia: Taxicab geometry
---

## Example

Let $n \ge 1$ be an integer.
For $x = (x_1, \ldots, x_n)$ and $y = (y_1, \ldots, y_n)$ in $\mathbb{R}^n$, let
$$d_1(x, y) = \sum_{i=1}^{n} |x_i - y_i|.$$
Then $d_1$ is a [[metric|063W5JMY85]] on $\mathbb{R}^n$, the taxicab metric.

## Remarks

The triangle inequality for $d_1$ follows from the [[triangle inequality|03HF5PMY5T]] for real numbers in each coordinate.
In $\mathbb{R}^2$, the distance from $(0, 0)$ to $(3, 4)$ is $7$, but the [[Euclidean distance|0E1MMCAY5B]] is $5$.
It is the case $p = 1$ of the [[p-metric|0TFDZN6AXP]].

## Explanations

### L1 human

A taxi in a city with a grid of streets cannot drive through the blocks.
It must go along the streets, so it travels the sum of the east-west and the north-south distances.
