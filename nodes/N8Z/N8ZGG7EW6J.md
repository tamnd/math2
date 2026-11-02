---
tag: N8ZGG7EW6J
kind: concept
name: Cesàro summation
msc: ["40G05"]
specializes: [8X25Q4XYMN]
sources:
  - url: https://en.wikipedia.org/wiki/Cesàro_summation
same_as:
  wikidata: Q2082317
  wikipedia: Cesàro summation
---

## Summary

Cesàro summation is the [[summability method|8X25Q4XYMN]] that assigns to a series the limit of the averages of its partial sums, when this limit exists.
These averages are the [[Cesàro means|08R2V9GZF7]] of the sequence of partial sums.
Every convergent series is Cesàro summable to its sum, and some divergent series, such as $1 - 1 + 1 - \cdots$, become summable.
Weighted versions of the averaging give the Cesàro methods $(C, \alpha)$ of higher order.
The method of order $1$ is used for Fourier series in [[Fejér's theorem|TPJZCSXSVN]].

## Explanations

### L1 human

Take the running totals of a series and then average them.
For $1 - 1 + 1 - 1 + \cdots$, the running totals are $1, 0, 1, 0, \dots$, which never settle down.
Their averages are $1, 1/2, 2/3, 1/2, 3/5, \dots$, and these tend to $1/2$.
So Cesàro summation gives the value $1/2$ to this series.
Averaging smooths out the oscillation while leaving the limit of a convergent series unchanged.
