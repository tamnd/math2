---
tag: VCHJVR9NGH
kind: concept
name: Word metric
msc: ["20F65"]
specializes: [0VKD1TP7F3]
sources:
  - url: https://en.wikipedia.org/wiki/Word_metric
same_as:
  wikidata: Q4423782
  wikipedia: Word metric
---

## Summary

The word metric on a [[group|G5S1M9]] with a generating set $S$ is a distance on the group.
The distance from $g$ to $h$ is the least number of generators and their inverses whose product is $g^{-1} h$.
It turns the group into a [[metric space|0VKD1TP7F3]], and it equals the path distance in the [[Cayley graph|0GYQK9NDJF]].
For a [[finitely generated group|082DWWXMRJ]], changing the finite generating set changes the metric only up to bounded factors.
So the metric is well defined up to [[quasi-isometry|6FKYSH729T]].
It is the starting point of [[geometric group theory|2T3218RXTD]].

## Explanations

### L1 human

Think of the generators as the allowed steps.
The length of an element is the fewest steps needed to reach it from the identity.
The distance between two elements is the fewest steps from one to the other.
In $\Z$ with the steps $\pm 1$, the distance between $m$ and $n$ is $\abs{m - n}$.
With the steps $\pm 2$ and $\pm 3$ instead, the number $1$ is at distance $2$ from $0$, since $1 = 3 - 2$ and $1$ itself is not a step.
