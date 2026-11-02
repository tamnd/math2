---
tag: MW5P4P4S9A
kind: definition
name: Locally finite measure
msc: [28C15]
defines: YQ5C1SRE0W
uses: [DYR1QFNGNJ, 02BH3MCBQB, 0R6EWFKRCF, 0FE2SB8WVJ]
sources:
  - url: https://en.wikipedia.org/wiki/Locally_finite_measure
---

## Definition

Let $X$ be a topological space and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
The measure $\mu$ is *locally finite* if every point $x \in X$ has an [[open|02BH3MCBQB]] neighbourhood $U$ with $\mu(U) < \infty$.

## Remarks

Example: Lebesgue measure $\lambda$ on $\R^n$ is locally finite.
The open ball of radius $1$ around $x$ has finite measure.

Non-example: counting measure on $\R$ is not locally finite.
Every open neighbourhood of a point is infinite, so it has measure $\infty$.

A locally finite measure is finite on every [[compact set|0R6EWFKRCF]] $K$: finitely many neighbourhoods of finite measure cover $K$.
Conversely, if $X$ is a Hausdorff [[locally compact space|0FE2SB8WVJ]] and $\mu$ is finite on compact sets, then $\mu$ is locally finite, since each point has a compact neighbourhood.
