---
tag: Z0K8AXW8Z1
kind: definition
name: Semicontinuity
msc: [54C08, 26A15]
defines: RN4G8SGP6P
uses: [0CQHFPGJ45, 0GSZ7B0CGR, 0ZCY0Z80B6, 02BH3MCBQB, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Semi-continuity
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]], let $f \colon X \to [-\infty, +\infty]$ be a function with values in the [[extended real line|0GSZ7B0CGR]], and let $x_0 \in X$.

1. $f$ is *upper semicontinuous* at $x_0$ if for every real $y > f(x_0)$ there is a [[neighbourhood|0ZCY0Z80B6]] $U$ of $x_0$ with $f(x) < y$ for all $x \in U$.
2. $f$ is *lower semicontinuous* at $x_0$ if for every real $y < f(x_0)$ there is a neighbourhood $U$ of $x_0$ with $f(x) > y$ for all $x \in U$.

The function $f$ is upper (lower) semicontinuous if it is upper (lower) semicontinuous at every point of $X$.

## Remarks

The function $f$ is upper semicontinuous if and only if $\set{x : f(x) < y}$ is [[open|02BH3MCBQB]] for every real $y$.
It is lower semicontinuous if and only if $\set{x : f(x) > y}$ is open for every real $y$.
In terms of limits, $f$ is upper semicontinuous at $x_0$ if and only if $\limsup_{x \to x_0} f(x) \le f(x_0)$, and lower semicontinuous at $x_0$ if and only if $\liminf_{x \to x_0} f(x) \ge f(x_0)$.
A real-valued $f$ is [[continuous|0VGFHTM75Y]] at $x_0$ if and only if it is both upper and lower semicontinuous at $x_0$.

Example: the [[floor function|08GR54CKEA]] $\floor{\cdot} \colon \R \to \R$ is upper semicontinuous.
At an integer $n$ and for $y > n$, the neighbourhood $(n - 1, n + 1)$ works, since $\floor{x} \le n < y$ there.
At a non-integer, the floor function is locally constant.

Non-example: the indicator function $f$ of $[0, 1]$ in $\R$ is not lower semicontinuous at $0$.
Here $f(0) = 1$; for $y = 1/2$, every neighbourhood of $0$ contains some $x < 0$ with $f(x) = 0 < y$.
