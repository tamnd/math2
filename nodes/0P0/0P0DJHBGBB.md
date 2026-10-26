---
tag: 0P0DJHBGBB
kind: definition
name: Cesàro mean
msc: [40G05]
defines: 08R2V9GZF7
uses: [0CTV783HYT]
sources:
  - url: https://en.wikipedia.org/wiki/Cesàro_summation
    locator: Definition
---

## Definition

Let $(a_n)_{n \ge 1}$ be a [[real sequence|0CTV783HYT]].
For each integer $n \ge 1$, the $n$-th Cesàro mean of $(a_n)$ is the arithmetic mean of its first $n$ terms,
$$\sigma_n = \frac{a_1 + a_2 + \cdots + a_n}{n}.$$

## Remarks

The sequence $(-1)^{n+1}$ diverges, but its Cesàro means are $1, 0, 1/3, 0, 1/5, \dots$, and they tend to $0$.
If $(a_n)$ converges, the [[Cesàro means converge to the same limit|0RDRPBMNAC]].
Cesàro summation applies the Cesàro means to the partial sums of a series. A series is Cesàro summable with sum $A$ when the means of its partial sums tend to $A$.

## Explanations

### L1 human

The Cesàro mean is the running average of the sequence.
Averaging smooths out oscillations. The sequence $1, 0, 1, 0, \dots$ has no limit, but its running averages tend to $1/2$.
