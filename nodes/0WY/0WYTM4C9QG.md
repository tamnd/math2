---
tag: 0WYTM4C9QG
kind: statement
role: theorem
name: A monotone function has countably many discontinuities
aliases: [froda-theorem]
msc: [26A48]
uses: [0KJXHN0TW0, 05B0FKFXQA]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: Some basic applications and results
---

## Statement

Let $I$ be an interval and let $f \colon I \to \mathbb{R}$ be monotone.
Then the set of points of $I$ where $f$ is not continuous is countable.

## Remarks

Assume $f$ increasing. By [[the existence of one-sided limits|0KJXHN0TW0]], each discontinuity $c$ inside $I$ gives an open interval $(f(c^-), f(c^+))$.
These intervals are disjoint. Each contains a rational number, so there are only countably many of them.
All these discontinuities are [[jumps|05B0FKFXQA]].
Mathlib states it as `Monotone.countable_not_continuousAt`.

## Explanations

### L1 human

Each discontinuity of an increasing function is a jump up.
The jumps take disjoint pieces of the vertical axis, so there can be only countably many.
