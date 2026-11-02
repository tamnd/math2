---
tag: X5R7FV9KWH
kind: concept
name: Nörlund mean
msc: ["40G05"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Divergent_series
---

## Summary

A Nörlund mean is a weighted average of the first terms of a sequence.
Its weights are read backwards from a fixed sequence $p_0, p_1, p_2, \dots$.
It defines a [[summability method|8X25Q4XYMN]] for sequences and, through partial sums, for series.
With all weights equal to $1$ it is the [[Cesàro mean|08R2V9GZF7]].
The method gives the usual limit to every convergent sequence exactly when $p_n$ is small compared with $p_0 + \cdots + p_n$.

## Explanations

### L1 human

To average $s_0, \dots, s_n$, the Nörlund mean gives the weight $p_0$ to the newest term $s_n$, the weight $p_1$ to $s_{n-1}$, and so on back to $p_n$ for $s_0$.
Then it divides by the total weight.
With all weights equal it is the plain average.
Weights that grow, such as $p_k = k + 1$, give more weight to the early terms of the sequence than the plain average does.
