---
tag: 8GZK8NC3VQ
kind: concept
name: Lévy–Prokhorov metric
msc: [60B10, 28A33]
sources:
  - url: https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Prokhorov_metric
same_as:
  wikidata: Q421945
  wikipedia: Lévy–Prokhorov metric
---

## Summary

The Lévy–Prokhorov metric is a distance between Borel [[probability measures|059TJN0NZ1]] on a [[metric space|0VKD1TP7F3]].
Two measures are close when each gives to every set little more mass than the other gives to a slight enlargement of it.
On a separable metric space, convergence in this metric is the same as [[weak convergence|MBW9JCGZC1]].
So weak convergence of probability measures comes from a metric.

## Explanations

### L1 human

Moving mass a short distance should count as a small change, and so should changing a small amount of mass.
The Lévy–Prokhorov distance allows both kinds of error at once, with the same tolerance $\varepsilon$.
For two point masses at $x$ and $y$, the distance is the smaller of $d(x, y)$ and $1$.
So point masses at $1/n$ and at $0$ are at distance $1/n$, which tends to $0$.
