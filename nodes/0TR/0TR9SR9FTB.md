---
tag: 0TR9SR9FTB
kind: definition
name: Strictly monotone function
aliases: [strictly-increasing-function, strictly-decreasing-function]
msc: [26A48]
defines: 011EJQWWJS
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: In calculus and analysis
---

## Definition

Let $D \subseteq \mathbb{R}$ and let $f \colon D \to \mathbb{R}$ be a function.
The function $f$ is strictly increasing if $f(x) < f(y)$ for all $x, y \in D$ with $x < y$.
It is strictly decreasing if $f(x) > f(y)$ for all $x, y \in D$ with $x < y$.
It is strictly monotone if it is strictly increasing or strictly decreasing.

## Remarks

With $\le$ and $\ge$ in place of $<$ and $>$, we get increasing, decreasing, and monotone functions.
A strictly monotone function is injective.
For example, $x^3$ is strictly increasing on $\mathbb{R}$, and $x^2$ is strictly increasing on $[0, \infty)$.
Mathlib defines strictly increasing maps as `StrictMono`.

## Explanations

### L1 human

A strictly increasing function always goes up: a larger input gives a larger output.
Its graph rises from left to right, with no flat parts.
