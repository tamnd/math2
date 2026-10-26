---
tag: 0DC3MPR7C9
kind: definition
name: Open ball
msc: ["54E35"]
defines: 0YE5868HZB
uses: [063W5JMY85]
sources:
  - url: https://en.wikipedia.org/wiki/Ball_(mathematics)
    locator: In general metric spaces
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]], let $x \in X$ and let $r > 0$ be a real number.
The open ball with centre $x$ and radius $r$ is the set
$$B(x, r) = \{ y \in X : d(x, y) < r \}.$$

## Remarks

The centre is in the ball: $x \in B(x, r)$, because $d(x, x) = 0 < r$.
In $\mathbb{R}$ with the usual metric, $B(x, r)$ is the open interval $(x - r, x + r)$.
In the [[discrete metric|0NA4FK7B8S]], $B(x, r) = \{x\}$ for $r \le 1$ and $B(x, r) = X$ for $r > 1$.
Some authors also allow $r \le 0$. Then $B(x, r)$ is empty.

## Explanations

### L1 human

The open ball $B(x, r)$ is the set of points that are less than $r$ away from $x$.
In the plane with the Euclidean metric, it is the inside of the circle of radius $r$ about $x$, without the circle itself.
